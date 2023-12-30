import streamlit as st
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain import FewShotPromptTemplate

def examples():
    return [
        {
            "input": "fun addTwoNumbers(a: Int, b: Int): Int { return a + b }",
            "output": "A mobile is magical Device that fit in your pocket, Like mini playground, it has games, movies"
        },
        {
            "input": "What are your dreams",
            "output": "My dreams are like a colorful adventure, where I become a superhero and save the day"
        }
    ]

def createPrompt():
    example_template = """
    question:{input}
    answer:{output}
    """
    example_prompt = PromptTemplate(input_variables=["input", "output"], template=example_template)
    return example_prompt

def prefix():
    return """ You are an Android Developer working on MNC. and Heaving 5 years of Experience.:
    Here are some examples:
    """

def suffix():
    return """
    question:{user_input}
    answer:
    """

def fewShotPromtTemplate():
    template = FewShotPromptTemplate(
        examples=examples(),
        example_prompt=createPrompt(),
        prefix=prefix(),
        suffix=suffix(),
        input_variables=['question'],  # Update to match the keys in your examples
        example_separator="\n\n"
    )
    return template

# Function to return the response
def load_answer(question):
    llm = HuggingFaceHub(repo_id="google/flan-t5-large")
    template = fewShotPromtTemplate()
    single_line_question = question.replace('\n', ' ')
    print(examples())
    answer = llm.predict(template.format(user_input=single_line_question))
    return answer

# App UI starts here
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("LangChain Demo")

# Gets the user input
def get_text():
    input_text = st.text_area("You: ", key="input")  # Use text_area for multiline input
    return input_text

user_input = get_text()
response = load_answer(user_input)

submit = st.button('Generate')

# If generate button is clicked
if submit:
    st.subheader("Answer:")
    st.write(response)
