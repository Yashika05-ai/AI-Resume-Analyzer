import os
import re
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
from prompts import resume_prompt
from docx import Document

# Load API key
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("Groq API Key not found! Please check your .env file.")
    st.stop()

client = Groq(api_key=api_key)

# ----------------------------
# Streamlit Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)
st.markdown("""
<style>
.main {
    padding: 2rem;
}
.stButton > button {
    width: 100%;
    background-color: #4CAF50;
    color: white;
    border-radius: 8px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Title
# ----------------------------
st.title("📄 AI Resume Analyzer")
st.write("Analyze your resume using AI and receive personalized feedback.")

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("About")
st.sidebar.info(
    """
    **AI Resume Analyzer**
    
    This application uses:
    - Streamlit
    - Groq API
    - Prompt Engineering

    Developed as a college project.
    """
)

# ----------------------------
# Resume Input
# ----------------------------
uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

resume = ""

if uploaded_file:

    if uploaded_file.type == "application/pdf":
        from utils import extract_pdf_text
        resume = extract_pdf_text(uploaded_file)

    else:
        from utils import extract_docx_text
        resume = extract_docx_text(uploaded_file)

    st.success("Resume uploaded successfully!")

else:

    resume = st.text_area(
        "Or Paste Resume Here",
        height=300
    )

# ----------------------------
# Analyze Button
# ----------------------------
if st.button("Analyze Resume"):

    if resume.strip() == "":
        st.warning("Please paste your resume first.")
    else:

        prompt = resume_prompt.format(resume=resume)

        with st.spinner("Analyzing your resume..."):

            try:

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.3
                )

                result = response.choices[0].message.content

                st.success("Analysis Complete!")

                # Extract Resume Score
                resume_match = re.search(r"Resume Score.*?(\d+)", result)

                # Extract ATS Score
                ats_match = re.search(r"ATS Score.*?(\d+)", result)

                # Display Resume Score
                if resume_match:
                    score = int(resume_match.group(1))
                    st.subheader("📊 Resume Score")
                    st.progress(score / 100)
                    st.write(f"**{score}/100**")

                # Display ATS Score
                if ats_match:
                    score = int(ats_match.group(1))
                    st.subheader("🤖 ATS Score")
                    st.progress(score / 100)
                    st.write(f"**{score}/100**")

                # Display Full Analysis
                st.markdown(result)

                # Download Button
                st.download_button(
                    label="📥 Download Analysis",
                    data=result,
                    file_name="resume_analysis.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"Error: {e}")

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("Made with ❤️ using Streamlit + Groq API")