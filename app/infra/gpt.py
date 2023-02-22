import openai
from dotenv import load_dotenv
import os
from app.infra import logger


def ask_gpt(prompt: str):
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    logger.logger.debug("OPENAI_API_KEY key loaded from dotenv")
    logger.logger.debug("sending OpenAI completion request")
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        temperature=0.7,
        max_tokens=3000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=['human:', 'AI:']
    )
    logger.logger.debug("response received from openai")
    return response['choices'][0]['text']