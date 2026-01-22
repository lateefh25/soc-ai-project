
def calculate_risk(alert_type, failed_attempts):
    if alert_type == "malware":
        return "High"
    elif alert_type == "login_failure" and failed_attempts > 5:
        return "High"
    elif alert_type == "login_failure":
        return "Medium"
    else:
        return "Low"
