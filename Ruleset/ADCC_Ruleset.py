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
            gender = input("Are you male or female?").lower()
            if (gender != "male" or "female"):
                print("Please answer as Male or Female.")
        return gender