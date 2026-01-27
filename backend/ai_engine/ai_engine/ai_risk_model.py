class DummyRiskModel:
    def analyze_alert(self, alert: str):
        return {
            "alert": alert,
            "severity": "low",
            "false_positive": True,
            "confidence": 0.87
        }

model = DummyRiskModel()

