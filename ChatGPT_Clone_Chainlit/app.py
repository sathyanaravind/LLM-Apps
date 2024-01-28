import chainlit as cl
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os

openai_api_key = os.getenv('OPENAI_API_KEY')


client = OpenAI()

messages = [
    {"role": "system", "content": "You are a helpful AI assistant"}
]


def ask_order(messages):
    response = client.chat.completions.create(
        model= "gpt-3.5-turbo",
        messages=  messages,
        temperature= 0,
    )

    return response.choices[0].message.content


@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    messages.append({"role": "user", "content": message.content})
    response = ask_order(messages)
    messages.append({"role": "assistant", "content": response})

    # Send a response back to the user
    await cl.Message(
        content=response,
    ).send()