import React, { useState } from 'react';
import { FaFileUpload, FaGoogleDrive, FaConfluence, FaBook, FaImage, FaCalendar, FaSearch, FaGlobe, FaSlack } from 'react-icons/fa';
import { Redirect } from "react-router-dom";

export default function ChatbotCustomization() {
  const [selectedButtons, setSelectedButtons] = useState({});
  const [isLoading, setIsLoading] = useState(false);
  const [redirect, setRedirect] = useState(false);
  const [selectedFiles, setSelectedFiles] = useState([]);

  const toggleButton = (button) => {
    setSelectedButtons((prev) => ({
      ...prev,
      [button]: !prev[button],
    }));
  };

  const handleComplete = () => {
    setIsLoading(true);
    setTimeout(() => {
      setIsLoading(false);
      setRedirect(true);
    }, 5000);
  };

  const handleFileChange = (event) => {
    const files = Array.from(event.target.files);
    setSelectedFiles(files);
  };

  // Conditionally redirect if redirect state is true
  if (redirect) {
    return <Redirect to="/chatbot" />;
  }

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h2 style={styles.header}>Customize Your Chatbot Assistant</h2>

        <div style={styles.field}>
          <label style={styles.label}>Assistant Name</label>
          <input type="text" placeholder="Enter assistant name" style={styles.input} />
        </div>

        <div style={styles.field}>
          <label style={styles.label}>Assistant Instructions</label>
          <textarea placeholder="Enter assistant instructions" rows={4} style={styles.textarea}></textarea>
        </div>

        <div style={styles.field}>
          <h3 style={styles.subHeader}>Add Knowledge Sources</h3>
          <div style={styles.buttonContainer}>
            <label style={{ ...styles.button, cursor: 'pointer' }}>
              <FaFileUpload /> Upload Files
              <input
                type="file"
                multiple
                onChange={handleFileChange}
                style={{ display: 'none' }} // Hide the default file input
              />
            </label>
            <button
              onClick={() => toggleButton('googleDrive')}
              style={{
                ...styles.button,
                ...(selectedButtons.googleDrive ? styles.selectedButton : {}),
              }}
            >
              <FaGoogleDrive /> Google Drive
            </button>
            <button
              onClick={() => toggleButton('confluence')}
              style={{
                ...styles.button,
                ...(selectedButtons.confluence ? styles.selectedButton : {}),
              }}
            >
              <FaConfluence /> Confluence
            </button>
            <button
              onClick={() => toggleButton('notion')}
              style={{
                ...styles.button,
                ...(selectedButtons.notion ? styles.selectedButton : {}),
              }}
            >
              <FaBook /> Notion
            </button>
          </div>

          {/* Display selected file names */}
          {selectedFiles.length > 0 && (
            <div style={styles.fileList}>
              <h4>Selected Files:</h4>
              <ul>
                {selectedFiles.map((file, index) => (
                  <li key={index}>{file.name}</li>
                ))}
              </ul>
            </div>
          )}
        </div>

        <div style={styles.field}>
          <h3 style={styles.subHeader}>Actions</h3>
          <div style={styles.buttonContainer}>
            <button
              onClick={() => toggleButton('image')}
              style={{
                ...styles.button,
                ...(selectedButtons.image ? styles.selectedButton : {}),
              }}
            >
              <FaImage /> Image Interpretation
            </button>
            <button
              onClick={() => toggleButton('date')}
              style={{
                ...styles.button,
                ...(selectedButtons.date ? styles.selectedButton : {}),
              }}
            >
              <FaCalendar /> Current Date
            </button>
            <button
              onClick={() => toggleButton('web')}
              style={{
                ...styles.button,
                ...(selectedButtons.web ? styles.selectedButton : {}),
              }}
            >
              <FaSearch /> Web Search
            </button>
            <button
              onClick={() => toggleButton('url')}
              style={{
                ...styles.button,
                ...(selectedButtons.url ? styles.selectedButton : {}),
              }}
            >
              <FaGlobe /> URL Fetch
            </button>
            <button
              onClick={() => toggleButton('slack')}
              style={{
                ...styles.button,
                ...(selectedButtons.slack ? styles.selectedButton : {}),
              }}
            >
              <FaSlack /> Slack Search
            </button>
          </div>
        </div>

        <button onClick={handleComplete} style={styles.completeButton}>
          {isLoading ? 'Loading...' : 'Complete'}
        </button>
      </div>
    </div>
  );
}

const styles = {
  container: {
    display: 'flex',
    justifyContent: 'center',
    padding: '20px',
  },
  card: {
    width: '100%',
    maxWidth: '500px',
    border: '1px solid #ddd',
    borderRadius: '8px',
    padding: '20px',
    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
    backgroundColor: '#fff',
  },
  header: {
    fontSize: '1.5em',
    fontWeight: 'bold',
    marginBottom: '20px',
    textAlign: 'center',
  },
  field: {
    marginBottom: '20px',
  },
  label: {
    display: 'block',
    fontSize: '0.9em',
    fontWeight: 'bold',
    color: '#333',
    marginBottom: '5px',
  },
  input: {
    width: '100%',
    padding: '10px',
    fontSize: '1em',
    borderRadius: '4px',
    border: '1px solid #ddd',
  },
  textarea: {
    width: '100%',
    padding: '10px',
    fontSize: '1em',
    borderRadius: '4px',
    border: '1px solid #ddd',
  },
  subHeader: {
    fontSize: '1em',
    fontWeight: 'bold',
    color: '#333',
  },
  buttonContainer: {
    display: 'flex',
    flexWrap: 'wrap',
    gap: '10px',
    marginTop: '10px',
  },
  button: {
    padding: '10px 15px',
    fontSize: '0.9em',
    borderRadius: '4px',
    border: '1px solid #ddd',
    backgroundColor: '#f0f0f0',
    cursor: 'pointer',
    display: 'flex',
    alignItems: 'center',
    gap: '5px',
  },
  selectedButton: {
    backgroundColor: '#c0c0c0', // Darker color when selected
  },
  completeButton: {
    width: '100%',
    padding: '12px',
    fontSize: '1em',
    borderRadius: '4px',
    border: 'none',
    backgroundColor: '#007bff',
    color: '#fff',
    fontWeight: 'bold',
    cursor: 'pointer',
  },
  fileList: {
    marginTop: '10px',
  },
};
