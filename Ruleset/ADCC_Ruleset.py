""" This module provides Ruleset main module. """

genders = ["male", "female"]
weight = 0
levels =["beginnner", "intermediate", "advanced", "professional"]

class Ruleset:
    def __init__(self, gender, weight, level):
        self._competitor = _Competitor(gender, weight, level)

    

class _Competitor:
    def __init__(self, gender, weight, level):
        self._gender = gender
        self._weight = weight
        self._level = level

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
            print("That is not a number. Please only enter positive numbers.")
        return weight

    def get_level():
        try:
            while level not in levels:
                level = input("Please enter your competitor level: ").lower()
                if (level != "beginnner" or "intermediate" or "advanced" or "professional"):
                    print("Please only enter a valid competitor level ,this includes Beginner, Intermediate, Advanced and Professional.")
        except (ValueError):
            print("Please only enter a valid competitor level ,this includes Beginner, Intermediate, Advanced and Professional.")