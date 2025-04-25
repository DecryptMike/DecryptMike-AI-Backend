from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(
    docs_url=None,
    redoc_url=None,
    openapi_url="/openapi.json"
)

# ✅ CORS Middleware (allows frontend to access backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Matrix Swagger UI
@app.get("/docs", include_in_schema=False)
async def custom_docs(request: Request):
    return templates.TemplateResponse("docs.html", {"request": request})

# ✅ Load classifier
classifier = pipeline("text-classification", model="bhadresh-savani/bert-base-uncased-emotion")

# ✅ Input Schema
class EmailInput(BaseModel):
    subject: str
    body: str

# ✅ Home route
@app.get("/")
def read_root():
    return {"status": "Phishing Detector API is live!"}

# ✅ Prediction route
@app.post("/predict")
def predict_phishing(email: EmailInput):
    text = f"{email.subject} {email.body}"
    prediction = classifier(text)[0]
    return {
        "label": prediction["label"],
        "confidence": round(prediction["score"] * 100, 2)
    }