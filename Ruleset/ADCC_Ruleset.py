""" This module provides Ruleset main module. """

import sqlite3

genders = ["male", "female"]
levels =["beginner", "intermediate", "advanced", "professional"]

class Ruleset:
    def __init__(self):
        self._competitor = _Competitor()

    def display_rules(self):
        #TODO: generate rules based on given data
        pass

    def determine_ruleset(self):
            age = self._competitor.get_age()
            gender = self._competitor.get_gender()
            weight = self._competitor.get_weight()
            level = self._competitor.get_level()
            
            try:
                conn = sqlite3.connect("C:\\Users\\zubai\\OneDrive\\Documents\\Programs\\Python\\ADCC_RULESET\\ADCC_Ruleset_CLI\\ADCC_RULESET.db")
                cursor = conn.cursor()
            except(FileNotFoundError):
                print("ERROR: Cannot connect to the database.")

            if (age < 11):
                # Query the juniors weight categories
                cursor.execute("""
                        SELECT category
                        FROM junior_weight_categories
                        WHERE lower_limit <= ? AND (upper_limit IS NULL OR ? <= upper_limit)
                    """, (weight, weight))
            elif (gender == "male" and age > 18):
                # Query the adult male weight categories
                cursor.execute("""
                        SELECT category
                        FROM adults_male_weight_categories
                        WHERE lower_limit <= ? AND (upper_limit IS NULL OR ? <= upper_limit)
                    """, (weight, weight))
            elif(gender == "female" and age > 18):
                # Query the adult female weight categories
                cursor.execute("""
                        SELECT category
                        FROM adults_female_weight_categories
                        WHERE lower_limit <= ? AND (upper_limit IS NULL OR ? <= upper_limit)
                    """, (weight, weight))
            elif(gender == "male" and 15 <= age <= 18 ):
                # Query the males 15 to 18 year old weight categories
                cursor.execute("""
                        SELECT category
                        FROM boys_15_18_weight_categories
                        WHERE lower_limit <= ? AND (upper_limit IS NULL OR ? <= upper_limit)
                    """, (weight, weight))
            elif(gender == "male" and 13 <= age <= 14 ):
                # Query the males 13 to 14 year old weight categories
                cursor.execute("""
                        SELECT category
                        FROM boys_13_14_weight_categories
                        WHERE lower_limit <= ? AND (upper_limit IS NULL OR ? <= upper_limit)
                    """, (weight, weight))
            elif(gender == "male" and 11 <= age <= 12 ):
                # Query the males 11 to 12 year old weight categories
                cursor.execute("""
                        SELECT category
                        FROM boys_11_12_weight_categories
                        WHERE lower_limit <= ? AND (upper_limit IS NULL OR ? <= upper_limit)
                    """, (weight, weight))
            elif(gender == "female" and 15 <= age <= 18 ):
                # Query the females 15 to 18 year old weight categories
                cursor.execute("""
                        SELECT category
                        FROM girls_15_18_weight_categories
                        WHERE lower_limit <= ? AND (upper_limit IS NULL OR ? <= upper_limit)
                    """, (weight, weight))
            elif(gender == "female" and 13 <= age <= 14 ):
                # Query the females 13 to 14 year old weight categories
                cursor.execute("""
                        SELECT category
                        FROM girls_13_14_weight_categories
                        WHERE lower_limit <= ? AND (upper_limit IS NULL OR ? <= upper_limit)
                    """, (weight, weight))
            elif(gender == "female" and 11 <= age <= 12 ):
                # Query the females 11 to 12 year old weight categories
                cursor.execute("""
                        SELECT category
                        FROM girls_11_12_weight_categories
                        WHERE lower_limit <= ? AND (upper_limit IS NULL OR ? <= upper_limit)
                    """, (weight, weight))
            else:
                print("No appropriate weight class currently exists.")
                
            result = cursor.fetchone()
            
            if result:
                weight_category = result[0]
                print(f'The user falls under the category: {weight_category}')
            else:
                print('No matching weight category')

class _Competitor:
    def __init__(self):
        self.gender = ""
        self.weight = 0
        self.level = ""
        self.age = 0

    def get_gender(self):
        self.gender = input("Please enter your gender: ").lower()
        if self.gender not in genders:
            print("Please answer as Male or Female.")
            self.get_gender()
        return self.gender
    
    def get_weight(self):
        try:
            self.weight = float(input("Please enter your weight in Kilograms: "))
            if (self.weight <= 0):
                print("Please only enter positive numbers.")
                self.get_weight()

        except ValueError:
            print("ERROR: That is not a number. Please only enter positive numbers.")
        return self.weight

    def get_level(self):
        try:
            self.level = input("Please enter your competitor level: ").lower()                
            if (self.level not in levels):
                print("Please only enter a valid competitor level ,this includes Beginner, Intermediate, Advanced and Professional.")
                self.get_level()
            return self.level
        except (ValueError):
            print("ERROR: Please only enter a valid competitor level ,this includes Beginner, Intermediate, Advanced and Professional.")

    def get_age(self):
        try:
            self.age = int(input("Please enter your age: "))
            if (self.age <= 0):
                print("Please only enter positive numbers.")
                self.get_age()

            if (self.age < 7):
                print("Sorry you are unable to compete yet, come back when you are over 7 years old.")
                exit()

        except ValueError:
            print("ERROR: That is not a valid input. Please only enter positive whole numbers.")
        return self.age