![FastAPI](https://img.shields.io/badge/FastAPI-API-059669?style=flat&logo=fastapi&logoColor=white&labelColor=3f3f46)
![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=flat&logo=python&logoColor=white&labelColor=3f3f46)
![Transformers](https://img.shields.io/badge/Transformers-HuggingFace-FBBF24?style=flat&logo=huggingface&logoColor=black&labelColor=3f3f46)
![Model-BERT-Emotion](https://img.shields.io/badge/Model-BERT--Emotion-EAB308?style=flat&labelColor=3f3f46)
![Hosted on-Render](https://img.shields.io/badge/Hosted%20on-Render-22C55E?style=flat&labelColor=3f3f46)
![Docs-Custom Matrix UI](https://img.shields.io/badge/Docs-Custom%20Matrix%20UI-000000?style=flat&labelColor=3f3f46)
![Backend-Live](https://img.shields.io/badge/Backend-Live-4ADE80?style=flat&labelColor=3f3f46)
![Open-Source-GitHub](https://img.shields.io/badge/Open--Source-GitHub-0078D4?style=flat&logo=github&logoColor=white&labelColor=3f3f46)
![License](https://img.shields.io/github/license/DecryptMike/DecryptMike-Web-Vuln-Scanner)


<p align="center">
  <img src="DecryptMikeLogo.png" alt="DecryptMike Logo" style="max-width: 100%; height: auto;"/>
</p>

<h2 align="center">
  🧠 DecryptMike AI Phishing Detector - Backend
</h2>

<h5 align="center">A FastAPI-powered backend for real-time phishing email analysis, using HuggingFace’s bert-base-uncased-emotion model. Provides secure API endpoints for emotion detection, with a custom Matrix-themed Swagger UI. Deployed on Render for live production access.
</h5>

---

## 🧪 API Endpoints

| Method | Endpoint       | Description                   |
|--------|----------------|-------------------------------|
| GET    | `/`            | Healthcheck                  |
| GET    | `/docs`        | Custom Swagger UI (Matrix)   |
| POST   | `/predict`     | Accepts email subject & body, returns emotion + confidence |

---

## 📦 Tech Stack

- `FastAPI` – lightweight web API
- `Transformers` – `bert-base-uncased-emotion`
- `Pydantic` – request validation
- `Uvicorn` – ASGI server
- `Render` – hosting the live API

---

## 📸 Screenshot

### Backend

<p align="center">
  <img src="DecryptMike Backend Render.png" width="100%" alt="Sign In Page">
</p>

---

## 🔗 Related Projects

- 🌐 [Live Frontend Demo](https://decrypt-mike-ai-frontend.vercel.app)
- 💻 [DecryptMike-AI-Frontend Repo](https://github.com/DecryptMike/DecryptMike-AI-Frontend)

---

## 🎯 Why I Built It

As part of my cybersecurity and AI engineering journey, I wanted to combine NLP and phishing detection into a live web tool. This backend powers the AI classifier using a fine-tuned BERT emotion model to analyze email content and return real-time emotional insight.

---

## ⚠️ Legal Disclaimer

This tool is intended for **educational and authorized personal use only**.  

---

## 💻 Built by [@DecryptMike](https://github.com/DecryptMike)

---

<p align="center">
  <img src="https://img.shields.io/badge/Built%20For-Web%20Development-blue?style=for-the-badge&logo=next.js"/>
  <img src="https://img.shields.io/badge/Made%20By-DecryptMike-limegreen?style=for-the-badge&logo=github"/>
  <img src="https://img.shields.io/badge/Inspired%20By-Cybersecurity-darkgreen?style=for-the-badge&logo=matrix"/>
</p>
