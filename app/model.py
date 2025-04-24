from transformers import pipeline

# Load phishing detection model
classifier = pipeline("text-classification", model="bhadresh-savani/bert-base-uncased-emotion")

def predict(subject: str, body: str):
    text = f"{subject} {body}"
    result = classifier(text)[0]
    return {
        "label": result["label"],
        "confidence": round(result["score"] * 100, 2)
    }