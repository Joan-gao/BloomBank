<h1 align="center"> BloomBank:<br/> Empowering Financial Independence with AI, Education, and Innovation 💸💡🌍 </h1>

## **Introduction**
BloomBank is an AI-powered financial management platform designed to empower individuals and families by simplifying budgeting, enhancing financial literacy, and fostering charitable giving. By aligning with the United Nations Sustainable Development Goals (SDGs) such as No Poverty (SDG 1), Quality Education (SDG 4), and Reduced Inequalities (SDG 10), BloomBank offers accessible, intelligent tools to bridge the gap in financial literacy and promote equitable economic opportunities.

With features like real-time budget tracking, family account collaboration, interactive education modules, and charitable savings integration, BloomBank addresses diverse financial challenges faced by underserved communities, young professionals, and families worldwide. By leveraging cutting-edge technologies such as Finetuned Gemini APIs and intuitive UI designs, our platform provides personalized advice and actionable insights to help users achieve financial stability and contribute to their communities.

<p align="center">
  <a href="https://www.youtube.com/watch?v=zQMfIDZ4vCg">
    <img src="https://img.youtube.com/vi/zQMfIDZ4vCg/maxresdefault.jpg" alt="Demo Video" width="600">
  </a>
</p>


## Links

- ([Demo Video](https://youtu.be/zQMfIDZ4vCg?si=wwHIk0QXNx9T3sgR))
- ([Bisness Plan](https://drive.google.com/file/d/1PhpbM9VifCUh-DzljVw2bDeStQYTY9KG/view))
- ([Devpost](https://devpost.com/software/bloombank))


## **Technologies Use**
1. **Frontend**: React, JavaScript
2. **UI Libraries**: Ant Design, ChatUI
3. **Backend**: Flask
4. **Database**: Firebase, Google Cloud MySQL
5. **AI Integration**: Finetuned Gemini APIs
6. **Hosting**: Firebase, Heroku

## **Core Features**

1. **SigninPage/SignupPage**

- **Functionality**: Require sign-in or sign-up for secure cloud storage of bill data. Collect personal details like age, gender, occupation, income sources, and financial goals to enable personalized financial advice from the AI bot. During registration, users can also choose a Family Account option, which allows them to invite family members via a QR code to collaborate on shared financial management.

2. **HomePage**

- **Functionality**: Display an overview of financial data, showing total income, expenses, and remaining budget by month and year. Provide a table for modifying or deleting individual expense and income entries.
  
3. **DashboardPage**

- **Functionality**: Provide detailed analysis of financial data. Users can select a month and year to view trends in income and expenses, with options to display data in line or bar charts.

4. **CalendarPage**

- **Functionality**: Display daily transaction data. By selecting a specific date on the calendar, users can view all income and expenses for that day in a table format, with options to modify or delete individual entries.

5. **DonationPage**

- **Functionality**: Provides donation options and free finance learning resources. Users can view monthly donations and access courses to build financial literacy.

6. **ChatbotPage**

- **Functionality**: Customizable AI chatbot for FAQs, bill data input, and file uploads. Users can personalize their chatbot with integrations (e.g., Google Drive, Notion) to import relevant documents. Finetuned Gemini APIs provide chatbot settings and personalized financial advice.

## Technical Highlights

1. **Secure User Authentication**: Utilize Firebase and Google Cloud SQL for secure sign-in/sign-up, ensuring data privacy and enabling CRUD operations for user information and bill records while providing personalized financial insights based on user-provided details.

2. **Comprehensive Data Visualization**: Offer a clear overview and detailed analysis of income, expenses, and budget trends with dynamic visualizations, allowing easy modifications and management of financial entries by month, year, or day.

3. **AI-Powered Chatbot**: Integrate a customized AI chatbot using finetuned Gemini models for real-time bill classification and personalized spending suggestions. Through prompt engineering, the chatbot is designed as a cute bookkeeping puppy that uses playful language to reduce financial management stress.

## Chatbot Use Examples (puppy version)

1. **Common Q&A**
- **User: What features does bloombank support?**
- **Response**: I can help you with voice input 🎤, image recognition 📸, and file text recognition 📄. I also love analyzing your bills based on your personal info, helping you understand your spending habits, and giving you pawsome suggestions, woof! 🐶✨
- **User: How to start bookkeeping with bloombank?**
- **Response**: First, fill in some basic info about yourself 💗. Then you can start bookkeeping! When you log an expense or income, just provide the date, event, and amount 📝. You can type it in or even bark it to me 🐾. Got a receipt? Snap a pic and upload it 📸. For bank statements, just upload the Excel or PDF file 📂. Let’s get your finances in order, woof! 🐶✨
- **User: How to view my bills?**
- **Response**: You can sniff out bill analysis on the dashboard page anytime to understand the proportion of spending categories, and daily, weekly, and monthly income and expenditure 📊. For detailed bills each day, just wag your way to the calendar page and click on the date 🗓️. Pawsome, woof! 🐶✨
- **User: How to edit or delete bills?**
- **Response**: Need to edit or delete bills? No worries! 🐾 If the bill was entered through conversation, just reply with the modification or deletion ✅. On the calendar page 📅, click on a specific date, find the bill entry, and then swipe left to edit or delete it manually 📝. Easy peasy, woof woof! 🐶✨

2. **CRUD Operations**
 - **User: Received $5000 salary yesterday, spent $50 on haircut, and $70 on groceries**
 - **Response**: Recorded. 🐾 Bill 1 Date: 2024-07-18, Category: Salary, Income: $5000, Description: salary, Account Book: Default account book; Bill 2 Date: 2024-07-18, Category: Beauty, Expense: $50, Description: haircut, Account Book: Default account book, Bill 3 Date: 2024-07-18, Category: Shopping, Expense: $70, Description: groceries, Account Book: Default account book.
 - **User: Edited $5000 salary yesterday to $3000**
 - **Response**: Edited. 🐾 Bill 1 Date: 2024-07-18, Category: Salary, Income: $5000, Description: salary yesterday, Account Book: Default account book.
 - **User: delete $5000 salary yesterday, spent $50 on haircut, and $70 on groceries**
 - **Response**: Deleted. 🐾

3. **Querying Detailed Income and Expense Data**
 - **User: How much did I spend on takeout this month?**
 - **Response**: You spent $300 on takeout this month, which is $50 more than your average spending this year, woof woof! 🐶✨
 - **User: How much did I earn on this year?**
 - **Response**: So far, you earned $80,000 from your job and $5,000 from your online e-shop business this year, which is $10,000 more than last year! **👩‍💻** Keep going, woof woof! 🐶✨

4. **Purchase Recommendations**
 - **User: I saw a pair of shoes on sale for $400, should I buy them?**
 - **Response1**:  Yes! You got a raise this month, and it’s been six months since your last big purchase. 💰 Your shopping expenses are in check, so if you love those shoes and the discount is great 👟, go for it,  woof! 🐶✨
 - **Response2**: No, you've already bought three pairs of shoes this month and overshot your shopping budget, that’s a lot! **😥** Plus, your goal is to save money, so it’s smarter to hold off on this purchase, woof! 🐶✨
 - **User: With my current savings, can I save $50,000 in three years?**
 - **Response1**: Yes! You’ve been saving $1,500 each month, so reaching your goal is totally doable. 💰 With your salary increase and lower rent, you might even save more! 💪 You’re on track to meet your goal in three years, woof! 🐶✨
 - **Response2**:  No, even though your salary increased, moving to a pricier city has doubled your expenses. 😥 Your monthly savings have dropped from $1500 to $800. 💸 If this trend continues, it will be tough to reach your goal in three years.  But don't worry, we'll find a way, woof! 🐶✨

## How to Run

1. **Frontend**

- Install dependencies

```bash
npm install
```

- Start the frontend server

```bash
npm run start
```

2. **Backend**

- Navigate to the backend directory

```bash
cd backend
```

- Create a virtual environment

```bash
python3 -m venv .venv
```

- Activate the virtual environment

```bash
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
```

- Install dependencies

```bash
pip install -r requirements.txt
```

- Run the Flask application

```bash
flask --app api run
```


## Contributors

- **Joan Gao** [[Linkedin](https://www.linkedin.com/in/xinyi-gao-cn/)][[GitHub](https://github.com/Joan-gao)]: Product Design, UI/UX Design, Full-stack Development
- **Li Cui** [[Linkedin](https://www.linkedin.com/in/li-cui-73809027b)][[GitHub](https://github.com/amandaliberaann)]: Full-Stack Development, Database Management
- **Jiacheng Li** [[Linkedin](https://www.linkedin.com/in/jiacheng-li-b17b41242/)][[GitHub](https://github.com/ljc0359)]: AI Fine-Tuning, Backend Development
- **Mustang Wu** [[Linkedin](https://linkedin.com/in/mustang-wu-10ab0520b/)]: Product Design, Full-stack Development
