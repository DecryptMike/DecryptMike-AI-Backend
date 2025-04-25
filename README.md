[![FastAPI](https://img.shields.io/badge/FastAPI-005F3C?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Transformers](https://img.shields.io/badge/Transformers-HuggingFace-yellow?style=flat-square&logo=huggingface)](https://huggingface.co/bhadresh-savani/bert-base-uncased-emotion)
[![BERT Emotion](https://img.shields.io/badge/Model-BERT--Emotion-yellowgreen?style=flat-square)](https://huggingface.co/bhadresh-savani/bert-base-uncased-emotion)
[![Render](https://img.shields.io/badge/Hosted_on-Render-46b946?style=flat-square&logo=render)](https://render.com/)
[![Swagger UI](https://img.shields.io/badge/Docs-Custom%20Matrix_UI-black?style=flat-square&logo=swagger)](https://decryptmike-backend.onrender.com/docs)
[![Live Backend](https://img.shields.io/badge/Backend-Live-brightgreen?style=flat-square)](https://decryptmike-backend.onrender.com)
[![Open Source](https://img.shields.io/badge/Open--Source-GitHub-blue?style=flat-square&logo=github)](https://github.com/DecryptMike/DecryptMike-AI-Backend)
[![MIT License](https://img.shields.io/badge/License-MIT-black?style=flat-square)](LICENSE)


<p align="center">
  <img src="DecryptMikeLogo.png" alt="DecryptMike Logo" style="max-width: 100%; height: auto;"/>
</p>

<h2 align="center">
  🧠 DecryptMike AI Phishing Detector - Backend
</h2>

<h5 align="center">A production-ready SaaS Starter Kit with authentication, RBAC, Stripe billing, PostgreSQL,<br> and a fully custom cyberpunk dashboard UI.
</h5>

---

## 📸 Screenshot

### Backend

<p align="center">
  <img src="DecryptMike Access.png" width="100%" alt="Sign In Page">
</p>

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
