import os
import json
from app.infra import logger


class Person:
    def __init__(self, name, login, gender, height, weight, age, activity_level, diet, meals_per_day,
                 other_notes):
        self.name = name
        self.login = login
        self.gender = gender
        self.height = height
        self.weight = weight
        self.age = age
        self.activity_level = activity_level
        self.diet = diet
        self.meals_per_day = meals_per_day
        self.other_notes = other_notes
        self.profile_path = "content/" + self.login
        logger.logger.debug('person initialization complete')

    def create(self):
        print(self.login)
        if not os.path.exists(self.profile_path):
            os.makedirs(self.profile_path)
        with open(f"{self.profile_path}/profile.json", "w") as file:
            json.dump(
                {"name": self.name,
                 "login": self.login,
                 "height": self.height,
                 "weight": self.weight,
                 "age": self.age,
                 "gender": self.gender,
                 "diet": self.diet,
                 "activity_level": self.activity_level,
                 "meals_per_day": self.meals_per_day,
                 "other_notes": self.other_notes,
                 "profile_path": self.profile_path
                 }, file)
        logger.logger.debug('person adding to json complete')
        return self.profile_path

    def read(self, login):
        folder_path = "content/" + login
        if not os.path.exists(folder_path):
            logger.logger.debug('person folder not found')
            return None
        with open(f"{folder_path}/profile.json", "r") as file:
            data = json.load(file)
            logger.logger.debug('person reading complete')
            return Person(name=data["name"],
                          login=data["login"],
                          gender=data["gender"],
                          height=data["height"],
                          weight=data["weight"],
                          age=data["age"],
                          activity_level=data["activity_level"],
                          diet=data["diet"],
                          meals_per_day=data["meals_per_day"],
                          other_notes=data["other_notes"])

    def update(self, name=None, login=None, gender=None, height=None, weight=None, activity_level=None,
               diet=None, meals_per_day=None, other_notes=None):
        # Add logic to write to JSON
        if name:
            self.name = name
        if login:
            self.login = login
        if gender:
            self.gender = gender
        if height:
            self.height = height
        if weight:
            self.weight = weight
        if activity_level:
            self.activity_level = activity_level
        if diet:
            self.diet = diet
        if meals_per_day:
            self.meals_per_day = meals_per_day
        if other_notes:
            self.other_notes = other_notes
        logger.logger.debug('person updating complete')
        return "Person updated."

    def delete(self):
        # Add logic to write to JSON
        logger.logger.debug('person deleting complete')
        return "Person deleted."

    def calculate_calories(self):
        bmr = 0
        if self.gender == "male":
            bmr = 66 + (6.23 * self.weight) + (12.7 * self.height) - (6.8 * self.age)
        elif self.gender == "female":
            bmr = 655 + (4.35 * self.weight) + (4.7 * self.height) - (4.7 * self.age)

        # Calculate total daily energy expenditure based on activity level
        if self.activity_level == "sedentary":
            tdee = bmr * 1.2
        elif self.activity_level == "lightly active":
            tdee = bmr * 1.375
        elif self.activity_level == "moderately active":
            tdee = bmr * 1.55
        elif self.activity_level == "very active":
            tdee = bmr * 1.725
        logger.logger.debug(f'TDEE calculated to {tdee}')
        return tdee

    def __str__(self):
        return self.read(self.login)
