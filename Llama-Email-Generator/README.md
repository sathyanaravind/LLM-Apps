# Cold Email Generator

This project is a **Cold Email Generator** that helps users create personalized cold emails for job applications based on job listings. By analyzing job descriptions, it generates tailored emails highlighting relevant experience and skills, streamlining the process of reaching out to potential employers.

## Features
- **Job Data Extraction**: Input a job listing URL to fetch and analyze job details.
- **Personalized Email Generation**: Automatically generates a customized email based on job requirements and user skills.
- **Powered by Llama-3.2 Large Language Model**:
  
## Technologies Used
- **Streamlit**: Used to build the interactive web application.
- **LangChain Community Document Loaders**: For loading and extracting text from job URLs.
- **Langchain**: LLM Orchestrator
- **Chromadb**: Open source vector database
## Installation
To set up this project, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd cold-email-generator
    ```

2. **Install required packages**:
    Make sure you have Python 3.7 or later installed. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit App**:
    ```bash
    streamlit run app.py
    ```

## Usage
1. **Enter the Job URL**: Paste a URL to the job listing in the sidebar input field.
2. **Generate Email**: Click on the **Generate Email** button.
3. **View Job Information**: The app will display job details (position, company, skills required, etc.).
4. **Copy Generated Email**: Use the **Copy Email to Clipboard** button to copy the email for easy use.

## Project Structure
- **app.py**: Main file to run the Streamlit application.
- **chains.py**: Contains the `Chain` class to process job data.
- **portfolio.py**: Manages user-specific project and skill links.
- **utils.py**: Includes utility functions, like `clean_text`, for data processing.

## Error Handling
If any issues arise during URL processing or email generation, error messages will appear in the application interface to guide users.

## Future Enhancements
- **Support for Multiple Job Boards**: Improve compatibility with various job boards.
- **Customization Options**: Allow users to adjust the email tone or structure.
- **Automatic Portfolio Import**: Integrate user-specific data more seamlessly.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.

