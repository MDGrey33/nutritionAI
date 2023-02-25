# NutritionAI App(FastAPI)

The Meal Planner app is a FastAPI based application that uses chatgpt to generate meal plans based on user preferences and dietary restrictions. 
The app also allows users to add new personal information, such as their height, weight, and activity level, to create personalized meal plans.

## Technology
The Meal Planner app is built using the following technologies:

- Python 3.11
- fastapi 0.92.0
- pydantic 1.10.5
- uvicorn 0.20.0

## Getting Started
To get started with the Meal Planner app, follow these steps:

Clone the repository to your local machine using the command:

      git clone https://github.com/MDGrey33/nutritionAI.git --branch FastAPI 

Create a virtual environment using Python 3.11:

      python3.11 -m venv envp11

Activate the virtual environment:

      source envp11/bin/activate

Install the required packages by running:

      pip install -r requirements.txt

Start the Uvicorn server by running:

      uvicorn app.main:app --reload

You can now access the app by going to `http://localhost:8000`.

You can now access the api documentation and run swagger tests by going to `http://localhost:8000/docs`.

If you make changes, make sure you run `pytest` with 5 passed tests before you make a pull request. 

If you install new libraries use `pip freeze > requirements.txt `

If you need help, feel free to ask.

## Main Functionality

The Meal Planner app will have the following main functionality:

- Allows users to add new personal information, such as their height, weight, and activity level, to create personalized meal plans.
### Coming soon
- Uses chatgpt to generate meal plans based on user preferences and dietary restrictions.
- Allows users to generate new meal plans.
- Allows users to generate recipes for the meals in the plans.

## Contributing

We welcome contributions to the Meal Planner app! To contribute, please fork this repository and submit a pull request with your changes.

Here are some areas that we are particularly interested in improving:

- Parallelizing the `generate_recipes` function
- Creating a mobile app to view meals and submit them to health apps
- Implementing Google authentication
- Training the Ada model for use in generating meal plans (instead of relying on the Davinci model)

If you are interested in training the Ada model, please reach out to us for more information on how to get started. Thank you for your interest in the Meal Planner app!

# Todo list

1. address updating name
2. split generate recipe into multiple parallel celery tasks
3. Pull file management to one package
4. pull meal from json to object
5. pull meal plan to object
6. pull recipe to object
7. Make mobile app to
   1. Show meals 
   2. Submit to health app
8. Implement google authentication for
