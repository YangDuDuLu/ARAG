import os
import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
PPLX_API_KEY = os.getenv("PP_API_KEY")
client = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")


def generate_text_pplx_online(prompt):
    messages = [
        {
            "role": "system",
            "content": (
                "You are an artificial intelligence assistant and you need to "
                "engage in a helpful, detailed, polite conversation with a user."
            ),
        },
        {
            "role": "user",
            "content": (
                prompt
            ),
        },
    ]

    response = client.chat.completions.create(
        model="pplx-70b-online",
        messages=messages,
    )

    return response.choices[0].message.content


iface = gr.Interface(
    fn=generate_text_pplx_online,
    inputs="textbox",  # Input is a textbox
    outputs="textbox",  # Output is a textbox
    title="Perplexity Demo"
)


if __name__ == '__main__':
    iface.launch()
    # print(generate_text_pplx_online("what is the weather like in SF today?"))

