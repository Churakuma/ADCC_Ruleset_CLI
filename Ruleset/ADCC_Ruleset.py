""" This module provides Ruleset main module. """

import sqlite3

genders = ["male", "female"]
levels =["beginnner", "intermediate", "advanced", "professional"]
weight = 0
age = 0
gender = ""
level = ""

class Ruleset:
    def __init__(self):
        self._competitor = _Competitor(gender, weight, level, age)

    def display_rules(self):
        #TODO: generate rules based on given data
        age = _Competitor.get_age
        gender = _Competitor.get_gender
        weight = _Competitor.get_weight
        level = _Competitor.get_level

        competitor = _Competitor(gender, weight, age, level)

    def determine_ruleset(competitor):
            try:
                conn = sqlite3.connect("C:\Users\zubai\OneDrive\Documents\Databases\ADCC_RULESET.db")
                cursor = conn.cursor()
            except(FileNotFoundError):
                print("ERROR: Cannot connect to the database.")
            
            if (gender == "male"):
                # Query the male weight categories
                cursor.execute("""
                        SELECT category
                        FROM adults_male_weight_categories
                        WHERE lower_limit <= ? AND (upper_limit IS NULL OR ? <= upper_limit)
                    """, (weight, weight))
            else:
                # Query the female weight categories
                cursor.execute("""
                        SELECT category
                        FROM adults_female_weight_categories
                        WHERE lower_limit <= ? AND (upper_limit IS NULL OR ? <= upper_limit)
                    """, (weight, weight))

            if (competitor.age < 7):
                print("Sorry you are unable to compete yet, come back when you are over 7 years old.")
                exit()

            

class _Competitor:
    def __init__(self, gender, weight, level, age):
        self._gender = gender
        self._weight = weight
        self._level = level
        self.age = age

    def get_gender():
        while gender not in genders:
            gender = input("Please enter your gender: ").lower()
            if (gender != "male" or "female"):
                print("Please answer as Male or Female.")
        return gender
    
    def get_weight():
        try:
            weight = float(input("Please enter your weight in Kilograms: "))
            if (weight >= 0):
                print("Please only enter positive numbers.")
                _Competitor.get_weight()

        except ValueError:
            print("ERROR: That is not a number. Please only enter positive numbers.")
        return weight

    def get_level():
        try:
            while level not in levels:
                level = input("Please enter your competitor level: ").lower()
                if (level != "beginnner" or "intermediate" or "advanced" or "professional"):
                    print("Please only enter a valid competitor level ,this includes Beginner, Intermediate, Advanced and Professional.")
            return level
        except (ValueError):
            print("ERROR: Please only enter a valid competitor level ,this includes Beginner, Intermediate, Advanced and Professional.")

    def get_age():
        try:
            age = int(input("Please enter your age: "))
            if (age >= 0):
                print("Please only enter positive numbers.")
                _Competitor.get_age()

        except ValueError:
            print("ERROR: That is not a valid input. Please only enter positive whole numbers.")
        return age