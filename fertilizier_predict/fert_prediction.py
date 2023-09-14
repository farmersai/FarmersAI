import os
import openai
openai.api_type = "azure"
openai.api_version = "2023-05-15" 
openai.api_base = "https://americasopenai.azure-api.net"  # Your Azure OpenAI resource's endpoint value.
openai.api_key = ""

def recommend_crop(data):
    N_val, P_val, K_val, temp_val, humidity_val, soil_type_val, crop_type_val = data[0]
    question = (f"I'm a farmer, the soil in my farmland has nitrogen value as {N_val}, the phosphorus value as {P_val}, "
            f"the potassium value as {K_val}, the temperature as {temp_val}°C, "
            f"the humidity as {humidity_val}%, the soil type as {soil_type_val}, "
            f"and the crop type as {crop_type_val}. could you recommend fertilizer that works best with the crop?")
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