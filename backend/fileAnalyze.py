from IPython.display import Image
import google.generativeai as genai
import yaml
from flask import Flask
import filetype
import os
from gemini_fune_tune_util.oAuth import load_creds
from flask_cors import CORS
from flask import Flask, request, jsonify

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
UPLOAD_FOLDER = 'uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024 * 1024  # 限制文件大小为16MB

# 确保上传目录存在
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def read_yaml(yaml_file_path):

    with open(yaml_file_path, 'rb') as f:
        config_data = yaml.safe_load(f.read())
    return config_data

config_data = read_yaml("setting.yaml")
app.config.update(config_data)
GEMINI_API_KEY = app.config['COMMON']['GEMINI_API_KEY']
genai.configure(api_key=GEMINI_API_KEY)
# genai.configure(api_key=os.environ["GEMINI_API_KEY"])


# Create the model

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,

)

def geminiUploadFile(file_path):


    user_file = genai.upload_file(
    path=file_path, display_name="User finaical File")
    verify = genai.get_file(name=user_file.name)
    print(f"Retrieved file '{verify.display_name}' as: {user_file.uri}")
    return user_file


def fileAnalyze(file):
    # save file to a local path
    filename = file.filename
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    # upload file to gemini
    userFile = geminiUploadFile(file_path)

    if userFile is not None:
        print("Ready for analyze")
        summary = model.generate_content([userFile, "describe the file"])
       
        response = model.generate_content([userFile, "Find first 40 transactions information, it needs to include transaction_date (in YYYY-MM-DD format), description and amount (decimal number) information, return all the transactions in a valid json format without anything else"])
        return summary.text, response.text
    else:
        print("Upload file to gemini fail")

@app.route('/file_analyze', methods=['POST'])
def file_analyze():
    file = request.files['file']
    summary, response_ = fileAnalyze(file)

    return jsonify({
            "summary": summary,
            "response": response_
        }), 200
 
if __name__ == '__main__':
    app.run(debug=True, port=5001)