import random


class Person:
    def __init__ (self, name, age, gender, traits, appearance, health, occupation, hobbies, values, goals):
        self.name = name
        self.age = age
        self.gender = gender
        self.traits = traits
        self.appearance = appearance
        self.health = health
        self.occupation = occupation
        self.hobbies = hobbies
        self.values = values
        self.goals = goals
        self.emotions = {
            "happiness": 0,
            "sadness": 0,
            "anger": 0,
            "fear": 0,
            "love": 0
        }

    def update_emotion (self, emotion, change):
        if emotion in self.emotions:
            self.emotions [emotion] += change
            self.emotions [emotion] = max (min (self.emotions [emotion], 100), 0)

    def display_emotions (self):
        print (f"{self.name}'s emotions: {self.emotions}")

    def display_info (self):
        print (f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")
        print (f"Traits: {self.traits}, Appearance: {self.appearance}, Health: {self.health}")
        print (f"Occupation: {self.occupation}, Hobbies: {self.hobbies}")
        print (f"Values: {self.values}, Goals: {self.goals}")


def create_person ():
    names = ["Alice", "Bob", "Charlie", "Diana"]
    traits = ["kind", "intelligent", "funny", "thoughtful"]
    appearances = [{"height": "5'6\"", "hair_color": "brown", "eye_color": "blue"},
                   {"height": "5'10\"", "hair_color": "black", "eye_color": "green"}]
    occupations = ["Software Developer", "Artist", "Teacher", "Doctor"]
    hobbies = ["reading", "hiking", "gaming", "cooking"]
    values = ["honesty", "compassion", "creativity", "determination"]
    goals = ["career advancement", "personal growth", "traveling", "learning new skills"]

    name = random.choice (names)
    age = random.randint (20, 40)
    gender = random.choice (["Male", "Female", "Non-binary"])
    selected_traits = random.sample (traits, 2)
    appearance = random.choice (appearances)
    health = random.choice (["Good", "Fair", "Poor"])
    occupation = random.choice (occupations)
    selected_hobbies = random.sample (hobbies, 2)
    selected_values = random.sample (values, 2)
    selected_goals = random.sample (goals, 2)

    return Person (name, age, gender, selected_traits, appearance, health, occupation, selected_hobbies, selected_values, selected_goals)


class Relationship:
    def __init__ (self, person1, person2):
        self.person1 = person1
        self.person2 = person2
        self.status = "starting"

    def interact (self):
        print (f"{self.person1.name} and {self.person2.name} are interacting.")
        # Define more complex interactions here


class Event:
    def __init__ (self, description, emotional_impact):
        self.description = description
        self.emotional_impact = emotional_impact

    def trigger (self, relationship):
        print (f"Event: {self.description}")
        for person in [relationship.person1, relationship.person2]:
            for emotion, change in self.emotional_impact.items ():
                person.update_emotion (emotion, change)


class LoveSimulation:
    def __init__ (self):
        self.people = []
        self.relationships = []

    def add_person (self, person):
        self.people.append (person)

    def create_relationship (self, person1, person2):
        relationship = Relationship (person1, person2)
        self.relationships.append (relationship)

    def run (self):
        while True:
            options = ["Add Person", "Create Relationship", "Run Simulation", "Exit"]
            choice = get_user_choice (options)
            if choice == "Add Person":
                person = create_person ()
                self.add_person (person)
                print (f"Added: {person.name}")
            elif choice == "Create Relationship":
                if len (self.people) < 2:
                    print ("Not enough people to create a relationship.")
                else:
                    person1 = random.choice (self.people)
                    person2 = random.choice ([p for p in self.people if p != person1])
                    self.create_relationship (person1, person2)
                    print (f"Created relationship between {person1.name} and {person2.name}.")
            elif choice == "Run Simulation":
                for relationship in self.relationships:
                    relationship.interact ()
            elif choice == "Exit":
                break


def get_user_choice (options):
    for i, option in enumerate (options, 1):
        print (f"{i}. {option}")
    choice = input ("Enter the number or first letter of your choice: ").strip ().lower ()
    if choice.isdigit ():
        return options [int (choice) - 1]
    else:
        for option in options:
            if option.lower ().startswith (choice):
                return option
    return None


# Create the simulation
simulation = LoveSimulation ()

# Run the simulation with user interaction
simulation.run ()