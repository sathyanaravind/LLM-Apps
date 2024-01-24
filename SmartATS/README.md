## Smart ATS 

<img src="https://github.com/sathyanaravind/LLM-Apps/blob/main/SmartATS/ats.gif" width="500" height="300" />


SmartATS is a streamlit based application that help job seekers to align their resumes with specific job descriptions  

**Features**
1. Resume Analysis: Analyzes the uploaded resume against the job description
2. Detailed Matching Score: Provides a percentage score indicating how well the resume matches the job description
3. Identification of Key Gaps: Enumerates missing or inadequately emphasized skills, experiences, or qualifications
4. Improvement Suggestions: Offers specific and actionable feedback for resume enhancement

**Tech Stack**
- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) Python
- ![PyPDF2](https://img.shields.io/badge/PyPDF2-21759B?style=for-the-badge&logo=adobeacrobatreader&logoColor=white) PyPDF2
- ![Google Gemini Pro](https://img.shields.io/badge/Google%20Gemini%20Pro-4285F4?style=for-the-badge&logo=google&logoColor=white) Google Gemini Pro
- ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) Streamlit

### Installation Steps

1. Clone the repo   
`
git clone https://github.com/sathyanaravind/LLM-Apps/tree/main/SmartATS
`
2. Navigate to the project directory   
`
cd [project-directory]
`
3. Install requirements.txt  
`
pip -r install requirements.txt
`
4. Set up environment variable  
`
GOOGLE_API_KEY=your_api_key_here
`

### Usage
1. Start the streamlit app  
`
streamlit run app.py
`
2. Open the app  
3. Using the app  
- enter the job description
- upload your resume
- click the submit button

### Note
This application requires an API key from Google Generative AI for its functionality. Ensure you have the appropriate access and permissions from Google Cloud Platform.
   
