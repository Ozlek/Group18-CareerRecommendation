# Group 18 - Career Recommendation Expert System

A web application using Flask, HTML, CSS, JavaScript, and a rule-based inference engine.

## Group Members & Roles
- Rafael Castillo - Project Leader (Handles project management & documentation)
- James Diaz - Data Analyst (Creates the knowledge base for the system)
- Kelzo Lumabas - Developer (Creates the inference engine logic & structural foundation of the system)
- Benedict Roxas - Backend Developer (Develops and handles the back-end of the system)
- Fritz Sablan - Frontend Developer (Develops and handles the front-end of the system)

## Project files

```text
career_recommendation_system/
├── knowledge_base.py       # 20 career profiles (expandable)
├── inference_engine.py     # IF-THEN matching and ranking logic
├── backend.py              # Flask routes and API logic
├── main.py                 # Application entry point
├── requirements.txt
├── templates/
│   └── index.html          # Frontend page structure
└── static/
    ├── style.css           # Frontend styling
    └── app.js              # Dynamic choices and API requests
```

## Project Setup

1. Open a terminal in this project folder.
2. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

   Windows PowerShell:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   Windows Command Prompt:

   ```bat
   venv\Scripts\activate.bat
   ```

3. Install Flask:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Start the application:

   ```bash
   python main.py
   ```

5. Open http://127.0.0.1:5000 in your browser.

## How it works

- `main.py` starts the Flask app defined in `backend.py`.
- The frontend requests available answer choices from `GET /api/options`.
- The user selects attributes and submits them to `POST /api/recommend`.
- `backend.py` validates the submitted facts and passes them to `infer_careers()`.
- `inference_engine.py` compares those facts against every profile in `knowledge_base.py`, activates matching rules, and ranks careers by weighted match score.
- The frontend displays the top five recommendations, matching attributes, and activated rules.

## Notes

- The five rule weights are defined in `inference_engine.py` and total 100%: interests 30%, skills 25%, work preferences 20%, personality 15%, and work nature 10%.
- Categories left unanswered are excluded and the remaining weights are normalized. The user must select at least one attribute.
- The score is a rule-based matching score, not a probability of career success.
- Flask debug mode is enabled for local development only. Turn it off before deploying publicly.
