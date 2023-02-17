# Meal Planner App

The Meal Planner app is a Flask-based application that uses chatgpt to generate meal plans based on user preferences and dietary restrictions. 
The app also allows users to add new personal information, such as their height, weight, and activity level, to create personalized meal plans.

## Technology
The Meal Planner app is built using the following technologies:

- Python 3.11
- Flask
- Celery
- Redis
- JSON

## Getting Started

To get started with the Meal Planner app, first, make sure you have Redis installed on your machine. Then, run the following command to start the Redis container:

      docker run --name some-redis -p 6379:6379 -d redis

Next, start the Flask server by running:

      flask --debug run --port=5001

Finally, start the Celery worker by running:

      celery -A app.infra.app_celery.celery worker --loglevel=info


You can now access the app by going to `http://localhost:5001`.

## Main Functionality

The Meal Planner app has the following main functionality:

- Allows users to add new personal information, such as their height, weight, and activity level, to create personalized meal plans.
- Uses chatgpt to generate meal plans based on user preferences and dietary restrictions.
- Allows users to generate new meal plans and recipes using the `generate_recipes` route.
- Allows users to view their meal plans and recipes.

## Contributing

We welcome contributions to the Meal Planner app! To contribute, please fork this repository and submit a pull request with your changes.

Here are some areas that we are particularly interested in improving:

- Error handling and input validation
- File management and object-oriented programming
- Parallelizing the `generate_recipes` function
- Creating a mobile app to view meals and submit them to health apps
- Implementing Google authentication
- Training the Ada model for use in generating meal plans (instead of relying on the Davinci model)

If you are interested in training the Ada model, please reach out to us for more information on how to get started. Thank you for your interest in the Meal Planner app!

# Todo list

1. Implement error handling
2. Implement input validation 
3. split generate recipe into multiple parallel celery tasks
4. Pull file management to one package
5. pull meal from json to object
6. pull meal plan to object
7. pull recipe to object
8. Make mobile app to
   1. Show meals 
   2. Submit to health app
9. Implement google authentication for

# Deployment

Start redis in docker container

    docker run --name some-redis -p 6379:6379 -d redis
Start Flask

    flask --debug run --port=5001
Start Celery

    celery -A app.infra.app_celery.celery worker --loglevel=info