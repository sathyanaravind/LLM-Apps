import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

def create_streamlit_app(llm, portfolio, clean_text):
    st.set_page_config(layout="wide", page_title="Cold Email Generator")

    # Sidebar setup
    with st.sidebar:
        st.title("📧 Cold Email Generator")
        url_input = st.text_input("🔗 Enter Job URL", help="Enter the job listing URL.")
        submit_button = st.button("Generate Email")

    st.title("Welcome to Email Generator ✉️")
    st.markdown("Generate a personalized cold email for job applications by entering a job URL.")

    if submit_button:
        with st.spinner("Fetching job details and generating email..."):
            try:
                # Load job data from URL
                loader = WebBaseLoader([url_input])
                loaded_data = loader.load()
                if not loaded_data:
                    st.error("Failed to load data from the provided URL.")
                    return
                
                # Process text and extract job information
                data = clean_text(loaded_data.pop().page_content)
                portfolio.load_portfolio()
                jobs = llm.extract_jobs(data)
                if not jobs:
                    st.warning("No job information found. Please check the URL.")
                    return
                
                # Display job details and generated email
                for job in jobs:
                    st.write(f"**Position:** {job.get('role', 'Unknown')}")
                    st.write(f"**Company:** {job.get('company', 'Unknown')}")
                    st.write(f"**Experience:** {job.get('experience', 'Unknown')}")
                    st.write(f"**Skills Needed:** {', '.join(job.get('skills', []))}")

                    # Generate email and display
                    email = llm.write_mail(job, portfolio.query_links(job.get('skills', [])))
                    st.text_area("Generated Email", email, height=200)
                    
                    if st.button("Copy Email to Clipboard", key=job.get('role')):
                        st.experimental_set_query_params(email=email)
                        st.success("Email copied to clipboard!")

            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        chain = Chain()
        portfolio = Portfolio()
        create_streamlit_app(chain, portfolio, clean_text)
    except Exception as e:
        st.error(f"Initialization error: {e}")
