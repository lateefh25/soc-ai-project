from fastapi import FastAPI
from ai_engine.ai_risk_model import model

app = FastAPI()

@app.get("/")
def root():
    return {"status": "SOC AI Backend Running"}

@app.post("/analyze")
def analyze(alert: str):
    return model.analyze_alert(alert)
