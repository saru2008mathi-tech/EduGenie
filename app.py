import streamlit as st
import google.generativeai as genai

# Page settings
st.set_page_config(
    page_title="EduGenie",
    page_icon="📚"
)

# App title
st.title("📚 EduGenie - Your AI Learning Assistant")
st.markdown("Powered by Google Gemini for NASSCOM FSP")

# Get API key securely from Streamlit Secrets
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except (KeyError, FileNotFoundError):
    API_KEY = ""

if not API_KEY:
    st.error(
        "Gemini API key set pannala. "
        "Streamlit Secrets-la GEMINI_API_KEY add pannu."
    )
    st.stop()

# Configure Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

# Subject selection
subject = st.selectbox(
    "Subject select pannu",
    [
        "General",
        "Science",
        "Maths",
        "Coding",
        "History",
        "English"
    ]
)

# Student level
level = st.radio(
    "Level",
    [
        "School Student",
        "College Student",
        "Beginner"
    ]
)

# Question input
question = st.text_area(
    "Un kelvi enna? (Ex: Photosynthesis enna?)",
    height=100
)

# Generate answer
if st.button("🚀 Explain pannu"):
    if question.strip():

        prompt = f"""
        You are EduGenie, a friendly tutor for {level}.
        Subject: {subject}
        Question: {question}

        Explain in simple Tamil and English mix (Tanglish).
        Give one simple example.
        Add two quiz questions at the end.
        """

        try:
            with st.spinner("Gemini yosikuthu..."):
                response = model.generate_content(prompt)

            if response.text:
                st.success("Answer ready!")
                st.markdown(response.text)
            else:
                st.warning("Answer kidaikkala. Marubadiyum try pannu.")

        except Exception:
            st.error(
                "Gemini response varala. API key, model access, "
                "internet connection check pannu."
            )

    else:
        st.warning("Kelvi type pannu da!")
