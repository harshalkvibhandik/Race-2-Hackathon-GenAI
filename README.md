# Race-2-Hackathon-GenAI
Race-2 Hackathon participation by GenAI Team to build the Chatbot to generate Unit Tests by using LangChain services

## Chat Model
Chat Model are advance language model that generate human like response in conversation enhancing interation with with AI system.

## PromptTemplate
Use PromptTemplate to create a template for a string prompt.
By default, PromptTemplate uses Python’s str.format syntax for templating.

from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "Tell me a {adjective} joke about {content}."
)
prompt_template.format(adjective="funny", content="chickens")
