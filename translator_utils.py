# translator_utils.py

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from languages import output_language_codes  # Import the language code dictionary
import os
import json


# Configure model - API
working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))
OPENAI_API_KEY = config_data["OPENAI_API_KEY"]
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

llm = ChatOpenAI(model="gpt-4o", temperature=0)

def translate(input_language, output_language, input_text):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant that translates {input_language} to {output_language}."),
            ("human", "{input}")
        ]
    )
    
    chain = prompt | llm

    response = chain.invoke(
        {
            "input_language": input_language,
            "output_language": output_language,
            "input": input_text
        }
    )

    return response.content

def get_gTTS_language_code(language_name):
    """
    Retrieves the correct gTTS language code from the language name.
    """
    return output_language_codes.get(language_name, "en")  # Default to English if not found
