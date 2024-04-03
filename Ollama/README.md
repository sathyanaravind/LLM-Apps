# Langchain Demo with Ollama Llama2

![streamlit app](https://github.com/sathyanaravind/LLM-Apps/blob/main/Ollama/image.png)

This project creates a simple web application that leverages Langchain and Ollama's local LLM Llama 2 to provide informative responses to user queries.

### Tech Stack:
Langchain   
Ollama   
Streamlit  

### Features:  
Users can enter a query in a text box.
The application prompts Ollama's Llama model to generate a response.
The generated response is presented to the user.
Setup:

Install dependencies:
```
pip install langchain streamlit
download ollama
```

Create a .env file in the project directory with the following variables:
LANGCHAIN_API_KEY=YOUR_API_KEY


### Usage:
Run the application: streamlit run app.py (assuming the code is in a file named app.py)
Access the application in your web browser.
Enter a query in the text box and press Enter.
