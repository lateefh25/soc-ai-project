from fastapi import FastAPI
from pydantic import BaseModel
from ai_engine.ai_risk_model import model

app = FastAPI(
    title="SOC AI SaaS",
    version="0.1.0"
)

class AlertRequest(BaseModel):
    alert: str

@app.get("/")
def home():
    return {"status": "SOC AI SaaS running"}

@app.post("/analyze")
def analyze_alert(data: AlertRequest):
    result = model(data.alert)
    return result

