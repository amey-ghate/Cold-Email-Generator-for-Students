# 📧 Cold Email Generator for Students

This project is a **Cold Email Generator for Students**, designed to help students create professional and tailored cold emails for job applications. Powered by Groq's advanced LLMs, this tool extracts job descriptions from URLs and crafts customized emails based on the extracted details and user inputs.

---

## Features

- **Job Description Extraction**: Automatically scrapes job descriptions from the provided URL.
- **Customizable Inputs**: Allows users to input their name, university/organization, and other key details.
- **Cold Email Generation**: Creates a professional cold email in four structured paragraphs:
  1. **Introduction**
  2. **Experience and Skills**
  3. **Why Choose Me**
  4. **Call to Action**
- **Vibrant User Interface**: Clean and vibrant design for a better user experience.
- **Download Option**: Users can download the generated email as a text file.

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

2. When prompted in the application:

    - **Enter the Job URL**: Provide the URL for the job posting you’re applying to.
    - **Your Name**: Enter your full name (used for personalization in the email).
    - **Your University/Organization**: Provide your current university or organization name (e.g., "University of Example").
    - **Groq API Key**: Enter your Groq API key when prompted.

3. Click the **Extract Job Details and Generate Email** button to start the process.
4. Once the job description is extracted:
    - A **Cold Email** is generated, which can be previewed in the app.
    - Download the email as a `.txt` file for further use.

---
## File Structure

- `main.py`: The main script to run the Streamlit application.
- `requirements.txt`: Lists the required Python dependencies for the project.
- `README.md`: This documentation file.
- 
---

## Example Workflow

### Input Details:
- Enter the job URL: `https://example.com/job-posting`
- Enter your name: `Jane Doe`
- Enter your university/organization: `University of Example`

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

- **Email Structure**: The email template can be modified in the `PromptTemplate` sections of `main.py`.
- **Styling**: Update the CSS in the `st.markdown` section of `main.py` to further customize the UI.

---

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests for improvements or new features.

---

> **Note:** This application serves as a **template** to help students get started with crafting professional cold emails for job applications. The generated email is a starting point, which students can further customize and tailor to fit their specific needs and preferences.

