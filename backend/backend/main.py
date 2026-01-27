from fastapi import FastAPI
from ai_engine.ai_risk_model import model

app = FastAPI()

@app.get("/")
def root():
    return {"status": "SOC AI SaaS running"}

@app.post("/analyze")
def analyze_alert(alert: str):
    return model(alert)
