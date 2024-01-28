## ChatGPT Clone Streamlit

<div align="center">
    <img src="https://github.com/sathyanaravind/LLM-Apps/blob/main/ChatGPT-Clone-Chainlit/chatgptclone.gif" alt="Webapp Demo GIF" width="500" height="300" />
</div>


ChatGPT Clone using the ChainLit and the OpenAI GPT-3.5 Turbo model. The chatbot assists users in generating responses to their input messages.

## Setup

1. Clone this repository to your local machine or download the script file.

2. Install the required Python packages using pip:
   ```bash
   pip install chainlit openai python-dotenv
Set up your OpenAI API key as an environment variable. You can do this by creating a .env file in the same directory as the script and adding the following line:

makefile
`
OPENAI_API_KEY=your-api-key-here
`
Replace your-api-key-here with your actual OpenAI API key.

Usage

Open a terminal or command prompt and navigate to the directory where the script is located.

Run the script using Python:

`
chainlit run app.py -w 
`
