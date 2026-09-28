# Student Feedback Web Application Using DevOps Tools

## 📌 Problem Statement
Develop a simple web-based student feedback application that allows a user to enter their **name**, **course**, and **feedback**. The application should display the submitted feedback on a webpage. Implement a basic **CI/CD pipeline** for the application using **GitHub Actions**.

---

## 📂 Project Structure
As per the lab requirements and demonstration:

```text
├── .github/
│   └── workflows/
│       ├── python-app.yml     # Complete CI/CD Pipeline (Test & GitHub Pages Deploy)
│       └── unittest.yml       # Automated Unit Testing Workflow
├── src/
│   ├── index.html             # Feedback form & dynamic display UI
│   ├── style.css              # Responsive modern design system
│   └── script.js              # Form validation & dynamic DOM rendering
├── tests/
│   ├── __init__.py            # Python package marker
│   └── test_operations.py     # Automated test suite for frontend integrity
├── README.md                  # Project documentation & setup instructions
└── requirements.txt           # Testing dependencies
```

---

## 🚀 Key Features

1. **User Input Form**:
   - **Student Name**: Text input for the student's name (with validation).
   - **Course / Department**: Course selector/input (e.g., Computer Science, Data Science, AI & ML).
   - **Experience Rating**: Interactive 1–5 star rating indicator.
   - **Feedback & Remarks**: Multi-line textarea with character counter.

2. **Real-time Feedback Display**:
   - Instant display of submitted feedback cards with student name, avatar initials, course badge, star rating, and timestamp.
   - Data persists across page reloads using browser `localStorage`.
   - Search & filter functionality to quickly look up feedback by student or course.
   - Individual delete and clear all options.

3. **DevOps & CI/CD Pipeline**:
   - **GitHub Actions**: Configured to run automated tests on every `push` and `pull_request` to the `main` branch.
   - **Automated Deployment**: Automatically deploys the frontend web application to **GitHub Pages**.

---

## 💻 How to Run Locally

### 1. View Web Application
Simply open `src/index.html` in any web browser, or serve it using Python's built-in HTTP server:

```bash
# From the project root directory
python -m http.server 8000 --directory src
```
Open your browser and navigate to: `http://localhost:8000`

---

## 🧪 How to Run Automated Tests

To run the unit tests locally using Python:

```bash
# Run unit tests
python -m unittest discover -s tests -v
```

All 5 tests should pass with `OK`:
- File existence verification (`index.html`, `style.css`, `script.js`).
- HTML form components validation (`studentName`, `courseName`, `feedbackText`, `submitBtn`).
- Webpage feedback display container validation (`feedbackList`, `feedbackCount`).
- CSS styling rules validation.
- JavaScript logic validation.

---

## ⚙️ CI/CD Pipeline Overview (GitHub Actions)

When pushed to GitHub, the workflow in `.github/workflows/python-app.yml` executes automatically:

1. **Continuous Integration (CI)**:
   - Sets up Ubuntu environment and Python 3.11.
   - Installs dependencies from `requirements.txt`.
   - Executes `python -m unittest discover -s tests -v` to ensure the application meets all criteria.

2. **Continuous Deployment (CD)**:
   - On successful tests, bundles the `src/` directory.
   - Deploys the static frontend to **GitHub Pages**.
   - Generates a live URL for immediate access.

---

## 📤 Git Push Instructions (To push to your GitHub)

If you haven't initialized Git yet:

```bash
# 1. Initialize git
git init

# 2. Add all files
git add .

# 3. Commit changes
git commit -m "Initial commit: Student feedback web app with CI/CD pipeline"

# 4. Set default branch to main
git branch -M main

# 5. Link to your remote GitHub repository
git remote add origin https://github.com/<YOUR-USERNAME>/<YOUR-REPO-NAME>.git

# 6. Push code
git push -u origin main
```
