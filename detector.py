def analyze_email(email_text):

    score = 0

    reasons = []

    suspicious_words = [

        "urgent",
        "verify",
        "suspended",
        "click here",
        "password",
        "bank",
        "login",
        "account"
    ]

    for word in suspicious_words:

        if word in email_text.lower():

            score += 10

            reasons.append(
                f"Suspicious keyword: {word}"
            )

    if "http://" in email_text:

        score += 20

        reasons.append(
            "Non-secure URL detected"
        )

    if score > 100:
        score = 100

    if score >= 70:
        level = "HIGH"

    elif score >= 40:
        level = "MEDIUM"

    else:
        level = "LOW"

    return score, level, reasons