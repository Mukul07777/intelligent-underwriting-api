def calculate_risk(text):
    # Dummy scoring logic - enhance as needed
    if "flood" in text.lower() or "fire" in text.lower():
        return "High Risk"
    elif "minor" in text.lower():
        return "Low Risk"
    else:
        return "Medium Risk"
