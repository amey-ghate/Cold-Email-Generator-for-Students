import json
import requests
from bs4 import BeautifulSoup
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import streamlit as st

# Streamlit App Configuration
st.set_page_config(page_title="Cold Email Generator for Students", page_icon="📧", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: #f0f8ff;
        }
        .generated-email {
            height: 400px !important;
            font-size: 14px;
            font-family: Arial, sans-serif;
        }
        .stTextArea label {
            font-size: 16px;
            font-weight: bold;
        }
        .stButton button {
            background-color: #ff4500;
            color: white;
            font-size: 16px;
        }
        .stTextInput label, .stJson label {
            font-size: 15px;
            color: #333;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit App Title and Description
st.title("📧 Cold Email Generator for Students")
st.markdown(
    """
    Welcome to the **Cold Email Generator for Students**! This tool helps you craft professional and tailored cold emails 
    for job applications by leveraging AI and your online profiles.
    """
)

# Step 1: User Inputs
st.header("Step 1: Provide Input Details")
with st.form("user_inputs"):
    url_input = st.text_input("Enter the Job URL:", placeholder="e.g., https://www.example.com/job-posting")
    student_name = st.text_input("Your Name:", placeholder="e.g., Jane Doe")
    university_name = st.text_input("Your University/Organization:", placeholder="e.g., University of Example")
    linkedin_url = st.text_input("Your LinkedIn Profile (Required):", placeholder="e.g., https://www.linkedin.com/in/yourprofile")
    portfolio_url = st.text_input("Portfolio Website (Optional):", placeholder="e.g., https://yourportfolio.com/projects")
    groq_api_key = st.text_input("Groq API Key (Required):", type="password")
    generate_button = st.form_submit_button("Extract Job Details and Generate Email")

if generate_button:
    if not url_input.strip() or not student_name.strip() or not university_name.strip() or not linkedin_url.strip() or not groq_api_key.strip():
        st.error("Please provide all required inputs (Job URL, Name, University/Organization, LinkedIn Profile, and Groq API Key).")
    else:
        try:
            # Step 1: Initialize Groq LLM
            llm = ChatGroq(
                temperature=0,
                groq_api_key=groq_api_key,
                model_name="llama-3.1-70b-versatile"
            )

            # Step 2: Scrape job description
            st.info("Scraping the job page content...")
            loader = WebBaseLoader([url_input])
            page_data = loader.load().pop().page_content

            prompt_extract = PromptTemplate.from_template(
                """
                ### SCRAPED TEXT FROM WEBSITE:
                {page_data}
                ### INSTRUCTION:
                Extract the job postings in JSON format with keys: `role`, `experience`, `skills`, and `description`.
                """
            )
            chain_extract = prompt_extract | llm
            res = chain_extract.invoke({"page_data": page_data})
            json_parser = JsonOutputParser()
            job_details = json_parser.parse(res.content)

            # Step 3: Scrape and summarize LinkedIn and portfolio content
            def fetch_and_summarize(url):
                try:
                    response = requests.get(url)
                    response.raise_for_status()
                    soup = BeautifulSoup(response.text, 'html.parser')
                    text = soup.get_text()
                    prompt_summary = PromptTemplate.from_template(
                        """
                        Summarize the following content to highlight key skills and achievements:
                        {content}
                        """
                    )
                    chain_summary = prompt_summary | llm
                    summary_response = chain_summary.invoke({"content": text})
                    return summary_response.content.strip()
                except requests.exceptions.RequestException as e:
                    return f"Error fetching data: {e}"

            st.info("Fetching and analyzing LinkedIn and portfolio content...")
            linkedin_summary = fetch_and_summarize(linkedin_url)
            portfolio_summary = fetch_and_summarize(portfolio_url) if portfolio_url.strip() else "No portfolio provided."

            # Step 4: Generate Cold Email
            st.header("Step 2: Generate Cold Email")
            st.info("Generating cold email...")
            prompt_email = ChatPromptTemplate.from_template(
                """
                ### JOB DESCRIPTION:
                {job_description}

                ### CANDIDATE DETAILS:
                Name: {student_name}
                University/Organization: {university_name}
                LinkedIn Summary: {linkedin_summary}
                Portfolio Summary: {portfolio_summary}

                ### INSTRUCTIONS:
                Write a professional cold email for the job description in four structured paragraphs:
                1. Introduction of the candidate (name, background, and current affiliation).
                2. Highlight relevant experiences and skills based on the LinkedIn and portfolio summaries.
                3. Explain why the candidate is an excellent fit for the job.
                4. End with a call to action for further discussion.

                ### EMAIL (START HERE):
                """
            )

            chain_email = prompt_email | llm
            email_response = chain_email.invoke(
                {
                    "job_description": str(job_details),
                    "student_name": student_name,
                    "university_name": university_name,
                    "linkedin_summary": linkedin_summary,
                    "portfolio_summary": portfolio_summary,
                }
            )

            # Display the generated email
            st.subheader("Generated Cold Email")
            st.text_area("Cold Email", email_response.content, height=400, key="generated_email", help="Copy and customize as needed.")
            st.download_button(
                label="📥 Download Email",
                data=email_response.content,
                file_name="cold_email.txt",
                mime="text/plain",
            )

        except Exception as e:
            st.error(f"An error occurred: {e}")
