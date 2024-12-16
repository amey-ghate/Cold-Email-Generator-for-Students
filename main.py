import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# Initialize Groq LLM
llm = ChatGroq(
    temperature=0,
    groq_api_key='<Your-API-Key>',
    model_name="llama-3.1-70b-versatile"
)

# Streamlit App Configuration
st.set_page_config(page_title="Cold Email Generator", page_icon="📧", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: #f0f8ff; /* Vibrant background color */
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
    Welcome to the **Cold Email Generator for Students**! This tool helps you craft professional and personalized cold emails tailored to job descriptions to help you apply for future job opportunities.
    Follow the steps below to generate your email.
    """
)

# Step 1: User Inputs
st.header("Step 1: Provide Input Details")
with st.form("user_inputs"):
    url_input = st.text_input("Enter the Job URL:", placeholder="e.g., https://www.example.com/job-posting")
    student_name = st.text_input("Your Name:", placeholder="e.g., Jane Doe")
    university_name = st.text_input("Your University/Current Organization:", placeholder="e.g., University of Example")
    generate_button = st.form_submit_button("Extract Job Details and Generate Email")

if generate_button:
    if not url_input.strip() or not student_name.strip() or not university_name.strip():
        st.error("Please provide all required inputs (Job URL, Your Name, and Your University/Organization Name).")
    else:
        try:
            # Scrape website content
            st.info("Scraping the job page content...")
            loader = WebBaseLoader([url_input])
            page_data = loader.load().pop().page_content

            # Define the prompt for extracting job details
            st.info("Extracting job details...")
            prompt_extract = PromptTemplate.from_template(
                """
                ### SCRAPED TEXT FROM WEBSITE:
                {page_data}
                ### INSTRUCTION:
                The scraped text is from the career's page of a website.
                Your job is to extract the job postings and return them in JSON format containing the
                following keys: `role`, `experience`, `skills`, and `description`.
                Only return the valid JSON.
                ### VALID JSON (NO PREAMBLE):
                """
            )

            # Extract job details
            chain_extract = prompt_extract | llm
            res = chain_extract.invoke({"page_data": page_data})

            # Parse JSON response
            json_parser = JsonOutputParser()
            job_details = json_parser.parse(res.content)

            # Display extracted job details
            st.success("Job details extracted successfully!")
            st.json(job_details)

            # Step 2: Generate Cold Email
            st.header("Step 2: Generate Cold Email")
            st.info("Generating cold email...")
            prompt_email = PromptTemplate.from_template(
                """
                ### JOB DESCRIPTION:
                {job_description}

                ### INSTRUCTIONS:
                You are {student_name}, a student or professional affiliated with {university_name}.
                Craft a cold email addressing the job description in four structured paragraphs:
                1. **Introduction**: A brief introduction about yourself and your current role/affiliation.
                2. **Experience and Skills**: Highlight your relevant academic achievements, internships, or projects related to the role.
                3. **Why Choose Me**: Explain why you are a great fit for the job and how your background aligns with the company’s goals.
                4. **Call to Action**: End with a clear and professional call to action to express interest in the position.

                Write the email directly, in a professional and persuasive tone, without a preamble or introductory notes.

                ### EMAIL (START HERE):
                """
            )

            chain_email = prompt_email | llm
            email_response = chain_email.invoke(
                {
                    "job_description": str(job_details),
                    "student_name": student_name,
                    "university_name": university_name,
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
