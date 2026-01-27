def model(alert_text: str):
    alert_text = alert_text.lower()

    if "failed login" in alert_text or "brute force" in alert_text:
        return {
            "classification": "True Positive",
            "risk": "High",
            "confidence": 0.87
        }

    if "scan" in alert_text or "nmap" in alert_text:
        return {
            "classification": "Suspicious",
            "risk": "Medium",
            "confidence": 0.65
        }

    return {
        "classification": "False Positive",
        "risk": "Low",
        "confidence": 0.92
    }

