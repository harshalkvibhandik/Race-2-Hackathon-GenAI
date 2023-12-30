from models import LanguageMessages
from models import LanguageType
from models import ModelType


def get_default_language_messages():
    return LanguageMessages(LanguageType.KOTLIN.value[0], LanguageType.KOTLIN.value[1])


def get_default_messages():
    return LanguageType.KOTLIN.value[1]


def get_messages_for_language(language):
    if language == LanguageType.KOTLIN.value[0]:
        return LanguageType.KOTLIN.value[1]
    elif language == LanguageType.JAVA.value[0]:
        return LanguageType.JAVA.value[1]
    elif language == LanguageType.PYTHON.value[0]:
        return LanguageType.PYTHON.value[1]
    elif language == LanguageType.SWIFT.value[0]:
        return LanguageType.SWIFT.value[1]
    else:
        return LanguageType.KOTLIN.value[1]


def generate_language_system_context_dict():
    return {
        LanguageType.KOTLIN.value[0]: LanguageType.KOTLIN.value[1],
        LanguageType.JAVA.value[0]: LanguageType.JAVA.value[1],
        LanguageType.PYTHON.value[0]: LanguageType.PYTHON.value[1],
        LanguageType.SWIFT.value[0]: LanguageType.SWIFT.value[1]
    }


def generate_deployed_models_dict():
    return {
        ModelType.GPT_4_32K.value[0]: ModelType.GPT_4_32K.value[1],
        ModelType.GPT_35_TURBO_16K.value[0]: ModelType.GPT_35_TURBO_16K.value[1],
        ModelType.GPT_35_TURBO.value[0]: ModelType.GPT_35_TURBO.value[1]
    }


def calculate_cost_for_model(model_name, total_tokens, prompt_tokens, completion_tokens):
    # from https://openai.com/pricing#language-models
    if model_name == ModelType.GPT_4_32K.value[0]:
        return total_tokens * 0.0600 / 1000
    elif model_name == ModelType.GPT_35_TURBO_16K.value[0]:
        return total_tokens * 0.0160 / 1000
    elif model_name == ModelType.GPT_35_TURBO.value[0]:
        return total_tokens * 0.0080 / 1000
    else:
        return (prompt_tokens * 0.03 + completion_tokens * 0.06) / 1000


def generate_page_header_html_content():
    return """
            <h1 style='text-align: center;'>
            Race 2 Innovate Hackathon
            </h1>
            <h3 style='text-align: center;'>
            Chatbot to generate unit test cases - by LLMNinjas Team</h3>
            <br>
            <h5 style='text-align: center;'>
            This Chatbot is well matured to genearate unit test cases - simply paste your code
            </h5>
            <br>
        """


def get_formatted_cost_message(model_name, total_tokens, cost):
    return f"\t\tModel used: {model_name}; Number of tokens: {total_tokens}; Cost: ${cost:.5f}"


def get_formatted_total_cost_message(total_cost):
    return f"Total cost of this conversation: ${total_cost:.5f}"
