import os
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://neyahopenai.openai.azure.com/",
    api_version="2023-06-01-preview",
    api_key=os.environ["OPENAI_API_KEY"]
)

response = client.chat.completions.create(
    model="text_demo",
    messages=[{"role": "system", "content": "You are a AI Tutor"},
              {"role": "user", "content": "What is AI"}],
    temperature=0.7,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
)

print(response)
print(response.choices[0].message.content)

