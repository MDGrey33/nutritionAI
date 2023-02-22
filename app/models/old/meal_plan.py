from app.infra.gpt import ask_gpt
from app.infra.file_system import write_file
from app.models.meal_plan_message import get_conversation
from app.models.person import Person
from app.infra import logger


def create_meal_plan(login):
    person = Person.read("", login)
    tdee = person.calculate_calories()
    conversation = get_conversation(person, tdee)
    logger.logger.debug(f'request sent to OpenAI')
    response = ask_gpt(conversation)
    logger.logger.debug(f'response received from OpenAI')
    write_file(response, f'{person.profile_path}/weekly_plan.json')
    logger.logger.debug(f'{person.profile_path}/weekly_plan.json written')
