import os
from openai import AzureOpenAI


# Create an AzureOpenAI client instance
client = AzureOpenAI(
    azure_endpoint='https://hsbc-aiml-team-resource.openai.azure.com/',
    api_version='2023-07-01-preview',
    api_key=os.environ['OPENAI_API_KEY']
)


def get_response_from_client(model, messages):
    return client.chat.completions.create(
        # Replace with the actual genai name if it exists
        model=model,
        # Send all messages from current session
        messages=messages,
        # Controls randomness of response
        temperature=0.8,
        # Set a limit on the number of tokens per genai response
        max_tokens=2000,
        # Similar to temperature, this controls randomness but uses a different method
        top_p=0.95,
        # Reduce the chance of repeating a token proportionally based on how often it has appeared in the text so far
        frequency_penalty=0,
        # Reduce the chance of repeating any token that has appeared in the text at all so far
        presence_penalty=0,
        # Number of completions
        n=1,
        # Make the genai end its response at a desired point
        stop=None,
    )
