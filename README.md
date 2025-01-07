# NIA - Neural Intelligent Aide 🤖✨

Meet **NIA** (Neural Intelligent Aide), your new AI-powered sidekick! NIA is here to make your life easier by managing your Google Calendar, organizing your notes, and answering your questions with the power of an open-source LLM (like LLAMA 2). Think of NIA as your personal assistant, but without the coffee runs. ☕

---

## Features 🚀


- **Google Calendar Integration**:
  - Create, edit, and delete events like a pro.
  - Fetch upcoming events and reminders so you never miss a beat.
- **Notes Management**:
  - Add, view, and manage notes effortlessly.
- **Natural Language Processing**:
  - Ask NIA anything, and it’ll respond like a champ.
- **Task Automation**:
  - Schedule tasks, set reminders, and optimize your productivity.
---

## Technologies Used 🛠️

- **Frontend**: React
- **Backend**: Flask (Python)
- **Database**: MySQL
- **LLM**: Hugging Face Transformers (LLAMA 2)
- **Authentication**: Firebase
- **APIs**: Google Calendar API, Hugging Face API

---

## Setup Instructions 🛠️

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/nia-neural-intelligent-aide.git
cd nia-neural-intelligent-aide
```
### 2. Set Up the Backend
Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```
Set Up Environment Variables
Create a .env file in the backend folder and add the following:

```
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
FIREBASE_API_KEY=your-firebase-api-key
MYSQL_HOST=localhost
MYSQL_USER=yourusername
MYSQL_PASSWORD=yourpassword
MYSQL_DATABASE=ai_assistant
HUGGINGFACE_API_KEY=your-huggingface-api-key
Run the Backend
bash
Copy
python run.py
```
3. Set Up the Frontend
Install Dependencies
```bash
cd ../frontend
npm install`
```
Set Up Environment Variables
Create a .env file in the frontend folder and add the following:

```
REACT_APP_BACKEND_URL=http://localhost:5000
Run the Frontend
bash
Copy
npm start
```
## Usage 🎮

### 1. Start the Application

Run the backend:

```bash
Copy
cd backend
python run.py
```
Run the frontend:

```bash
cd ../frontend
npm start
```

### 2. Access the Application
Open your browser and go to:
```
http://localhost:3000
```


## Contributing 🤝
Contributions are welcome! Fork & Push
