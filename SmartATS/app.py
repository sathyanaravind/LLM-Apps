import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Gemini pro response
def get_response(input_text):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_text)
    return response.text

# Function to extract text from PDF
def pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() if page.extract_text() else ""
    return text

# Streamlit app
st.title("Smart ATS")
st.text("Improve your resume ATS score")
jd = st.text_area("Paste your Job Description")
uploaded_file = st.file_uploader("Upload your Resume", type="pdf", help="Please upload the pdf")
submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        resume_text = pdf_text(uploaded_file)
        input_prompt = f"""
        As a sophisticated Applicant Tracking System (ATS) with in-depth expertise in various technology domains such as software engineering, data science, data analysis, and big data engineering, your primary function is to execute a meticulous and nuanced appraisal of the applicant's resume against the specified job description (JD). In the context of a fiercely competitive job market, your analysis is expected to be exhaustive and insightful, with a focus on providing targeted feedback to refine and enhance the candidate's resume.

        Your evaluation must encompass the following components:

            1. Detailed Matching Score: Conduct a thorough analysis of the resume, assigning a percentage score to reflect its congruence with the job description's requirements and preferences. This score should encapsulate the candidate's aptitude, expertise, and qualifications in relation to the role.

            2. Identification of Key Gaps: Identify and list any pivotal skills, experiences, or qualifications that are critical for the role, as outlined in the job description, but are either missing or inadequately emphasized in the resume. This inventory will guide the candidate in understanding which essential elements to incorporate or accentuate.

            3. Actionable Improvement Feedback: Offer precise and practical advice on enhancing the resume to align more closely with the job description. This could include recommendations on content restructuring, spotlighting certain experiences, or incorporating specific keywords and industry-specific terminologies.

            Your analysis should be articulated in a straightforward and succinct manner, ensuring that the candidate can easily comprehend and implement your suggestions.

            Resume Content:
            {resume_text}

            Job Description:
            {jd}
            ---
            Please provide your evaluation in the following format:
            - JD Matching Score: [Percentage]
            - Missing Keywords/Elements: [List]
            - Improvement Suggestions: [Detailed Feedback]
            """

        response = get_response(input_prompt)
        st.subheader("ATS Analysis")
        st.text(response)
