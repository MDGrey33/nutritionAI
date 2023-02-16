from app.infra import logger

json_string = """{
    "recipe": {
        "name": "Banana Pancakes",
        "serving": "2",
        "cookingTime": "15 minutes",
        "ingredients": [
            {
                "name": "all-purpose flour",
                "quantity": "1",
                "unit": "cup"
            },
            {...},
            {...}
        ],
        "instructions": [
            "In a large mixing bowl, combine the flour, baking powder, and salt.",
            "Mash the banana in a separate bowl.",
            "Cook until bubbles form on the surface and the edges start to dry, then flip and cook until browned."
        ],
        "nutrition": {
            "calories": "240",
            "fat": "9g",
            "carbohydrates": "34g",
            "protein": "6g"
        }
    }
}
"""


def get_conversation(meal):
    conversation = f"""Give me the recipe for {meal['name']} with the following constraints:
serving size {meal['servings']},{meal['nutrition_facts']}
The units should be following the European standard.
The instructions should be a list
Respond inside the following JSON
{json_string}"""
    logger.logger.debug('Conversation generated')
    return conversation
