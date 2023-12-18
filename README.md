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


### Few Shot Template
Few shot is a way to teach computer to make predication using only small amount of information. Instead of needing lots of example Computer can learn from few example 
They can find the pattern in the example and those pattern to understand and recognize new things. Its Help computer to learn quickly and accurate with only little bit information.
