import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_text_gpt4(prompt):
    response = openai.Completion.create(
        engine="gpt-4-turbo",  # Specify the GPT-4 Turbo model
        prompt=prompt,
        max_tokens=100,  # Adjust the maximum response length as needed
        n=1,
        stop=None,
        temperature=0.7,  # Adjust for creativity level
    )
    return response.choices[0].text

# Example Usage
prompt = "Write a poem about the beauty of nature."
response = generate_text_gpt4(prompt)
print(response)
