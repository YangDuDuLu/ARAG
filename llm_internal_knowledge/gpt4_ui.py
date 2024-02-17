import gradio as gr
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("GPT4_API_KEY"),
)


def generate_text_gpt4(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4-turbo-preview",
    )
    return chat_completion.choices[0].message.content


iface = gr.Interface(
    fn=generate_text_gpt4,
    inputs="textbox",  # Input is a textbox
    outputs="textbox",  # Output is a textbox
    title="GPT-4 Turbo Demo"
)

if __name__ == '__main__':
    iface.launch()
