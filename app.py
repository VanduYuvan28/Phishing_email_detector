import streamlit as st

from detector import analyze_email

def load_css():

    with open("assets/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.set_page_config(
    page_title="Phishing Detector"
)

st.markdown("""
<h1>🛡️ Phishing Email Detection System</h1>
""", unsafe_allow_html=True)

st.markdown("""
<center>
<h4 style='color:white;'>
AI-Powered Email Threat Analysis Platform
</h4>
</center>
""", unsafe_allow_html=True)

email_text = st.text_area(
    "Paste Email Content"
)

st.info(
    "📧 Paste the email content below and click Analyze to detect phishing indicators."
)

if st.button("Analyze"):

    score, level, reasons = analyze_email(
        email_text
    )

    st.metric(
        "Risk Score",
        f"{score}%"
    )

    st.metric(
        "Threat Level",
        level
    )

    st.subheader(
        "Detection Reasons"
    )

    for reason in reasons:

        st.write(
            "✓", reason
        )