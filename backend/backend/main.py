from fastapi import FastAPI
from ai_engine.ai_risk_model import model

app = FastAPI()

@app.get("/")
def home():
    return {"status": "SOC AI SaaS running"}

@app.post("/analyze")
def analyze_alert(score: int):
    risk = model.predict([[score]])[0]
    return {"risk_level": risk}
