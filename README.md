# 📧 Cold Email Generator for Students

This project is a **Cold Email Generator for Students**, designed to help students craft professional and tailored cold emails for job applications. By leveraging AI, this tool extracts job descriptions, analyzes the candidate's LinkedIn and portfolio links, and generates a personalized email highlighting why the candidate is an excellent fit for the role.

---

## Features

- **Job Description Extraction**: Automatically scrapes job descriptions from URLs.
- **LinkedIn and Portfolio Analysis**: Processes LinkedIn and optional portfolio links to extract relevant skills and achievements.
- **AI-Powered Personalization**: Generates a professional cold email with structured content:
  1. Introduction of the candidate.
  2. Highlighting relevant experiences and skills.
  3. Why the candidate is the perfect fit.
  4. Call to action.
- **User-Friendly UI**: Interactive and vibrant interface for seamless usage.
- **Download Option**: Download the generated email as a `.txt` file.

---

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.8 or later
- Streamlit
- Required Python libraries (listed in `requirements.txt`)

---

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/amey-ghate/Cold-Email-Generator-for-Students.git
   cd cold-email-generator
    ```   
2. Install the required Python libraries:
     ```bash
   pip install -r requirements.txt
    ```   
3. Obtain a Groq API key by signing up at Groq's API portal.(https://console.groq.com/keys)

---

## Usage
    
1. Run the application:
    ```bash
   streamlit run main.py
    ```

2. In the application, provide the following details:

    - **Enter the Job URL**: The URL of the job posting.
    - **Your Name**: Enter your full name.
    - **Your University/Organization**: Your current university or workplace.
    - **LinkedIn Profile**: A link to your LinkedIn profile (required).
    - **Portfolio Website**: A link to your portfolio or website (optional).
    - **Groq API Key**: Your Groq API Key (required).

3. Click the **Extract Job Details and Generate Email** button to start the process.
4. Once the job description is extracted:
    - The tool will analyze LinkedIn and portfolio links.
    - A **Cold Email** is generated, which can be previewed in the app.
    - Download the email as a `.txt` file for further use.

---
## File Structure

- `main.py`: The main script to run the Streamlit application.
- `requirements.txt`: Lists the required Python dependencies for the project.
- `README.md`: This documentation file.
---

## Example Workflow

### Input Details:
- Enter the job URL: `https://example.com/job-posting`
- Enter your name: `Jane Doe`
- Enter your university/organization: `University of Example`
- LinkedIn Profile: `https://www.linkedin.com/in/janedoe`
- Portfolio Website (Optional): `https://janedoeportfolio.com`

### Generated Email:
A professionally crafted email with:
1. **Introduction**
2. **Experience and skills**
3. **Why you're the best fit**
4. **Call to action**

### Output:
- View the email in the app.
- Download the email as a `.txt` file.

---

## Customization

- **Email Structure**: Modify the email template in the `PromptTemplate` and `ChatPromptTemplate` sections  of `main.py`.
- **Styling**: Update the CSS in the `st.markdown` section of `main.py` to further customize the UI.

---

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests for improvements or new features.

---

> **Note:** This application serves as a **template** to help students get started with crafting professional cold emails for job applications. The generated email is a starting point, which students can further customize and tailor to fit their specific needs and preferences.

