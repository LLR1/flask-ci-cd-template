# 🚀 Flask CI/CD Template

[![CI](https://github.com/LLR1/flask-ci-cd-template/actions/workflows/ci.yml/badge.svg)](https://github.com/LLR1/flask-ci-cd-template/actions)
[![Deploy on Render](https://img.shields.io/badge/Deploy-Render-blue?logo=render)](https://render.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A minimal and developer-friendly template to kickstart Flask projects with automated CI/CD via **GitHub Actions** and **Render**.

---

## 📦 Features

- ✅ Lightweight [Flask](https://flask.palletsprojects.com/) app  
- ⚙️ CI via GitHub Actions  
- ☁️ Auto-deploy to [Render](https://render.com/)  
- 📁 Clean file structure and `.gitignore`  
- 📚 Developer-oriented documentation  

---

## 📂 Project Structure

```text
flask-ci-cd-template/
├── app.py
├── requirements.txt
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci.yml
├── README.md
└── LICENSE
```

---

## 🛠️ Getting Started

### 1. Clone this repository

```bash
git clone https://github.com/LLR1/flask-ci-cd-template.git
cd flask-ci-cd-template
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run locally

```bash
python app.py
```

The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000)  
(you can also use [http://localhost:5000](http://localhost:5000))

---

## ⚙️ CI: GitHub Actions

This project uses a simple CI workflow at `.github/workflows/ci.yml`. It installs dependencies and runs a basic check. Feel free to extend it with linting, unit tests, coverage reports, etc.

---

## ☁️ CD: Auto-Deploy with Render

1. Create a free account on [render.com](https://render.com/)  
2. Link your GitHub repo  
3. Set the build & start commands:

```bash
Build Command:    pip install -r requirements.txt
Start Command:    python app.py
```

Render will automatically redeploy your app on every `git push` to `master`.

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request to improve this template.

---

## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
