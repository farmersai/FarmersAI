import pickle
import os
import openai
openai.api_type = "azure"
openai.api_version = "2023-05-15" 
openai.api_base = "https://americasopenai.azure-api.net"  # Your Azure OpenAI resource's endpoint value.
openai.api_key = ""

def recommend_marketPlace(data):
    crop_name, location = data[0]
    question = (f"I am a farmer who has harvested {crop_name} crop, at city {location}. I want to sell this crop."
                f"Could you provide a list of markets I can sell this at?")
    print(question)
    response = openai.ChatCompletion.create(
        engine="gpt-35-turbo-16k", # The deployment name you chose when you deployed the GPT-35-Turbo or GPT-4 model.
        messages=[
            {"role": "system", "content": "I want you to act like a helpful agriculture chatbot and help farmers with their query."},
            {"role": "user", "content": question}
        ]
    )

    print(response['choices'][0]['message']['content'])
    return response['choices'][0]['message']['content']
