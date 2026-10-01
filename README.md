# EduGenie

## Google Gemini Powered Learning Assistant

EduGenie is a lightweight AI-powered educational assistant designed to help students learn more effectively.

### Features

- Ask questions and get AI-generated answers
- Explain difficult topics in simple language
- Generate educational quizzes
- Summarize text
- Create personalized learning paths

### Technologies Used

- Python
- FastAPI
- Google Gemini API
- HTML
- CSS
- Jinja2
- Uvicorn

### Project Structure

```text
EduGenie/
├── main.py
├── qna.py
├── explanation_module.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── style.css

### How to Run

1. Create and activate a Python virtual environment.
2. Install the required packages.
3. Add your Gemini API key to the `.env` file.
4. Run the application using:

```bash
uvicorn main:app --reload
5. Open http://127.0.0.1:8000 in a browser

#Project Goal
EduGenie provides students with an easy-to-use AI learning assistant for question answering, explanations, quizzes, summaries, and personalized learning recommendations.

#Tested Screenshots
<img width="1440" height="900" alt="summary-text" src="https://github.com/user-attachments/assets/88ccd0ab-9db4-463d-9d8b-b07eb4a79cca" />
<img width="1440" height="900" alt="question-answer" src="https://github.com/user-attachments/assets/0f9e7599-2ace-4c6d-b82f-13983dae5424" />
<img width="1440" height="900" alt="learning-path" src="https://github.com/user-attachments/assets/f01e8baf-2c00-4be1-b34d-adb5d7116cc8" />
<img width="1440" height="900" alt="generate-quiz" src="https://github.com/user-attachments/assets/8ab2f9ed-1c42-4aca-b944-192ec9dda2ee" />
<img width="1440" height="900" alt="explain-topic" src="https://github.com/user-attachments/assets/c47960b4-4e32-4e0a-9153-f84680805653" />

