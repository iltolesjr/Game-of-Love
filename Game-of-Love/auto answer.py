import random


class DateSimulation:
    def run (self):
        self.stages [self.current_stage]

    def stage_one (self):
        dates = ["Ice cream", "Movies", "Dinner", "Concert", "Planning holidays"]
        for date in dates:
            print (f"Date: {date}")
            time.sleep (1)
        self.current_stage += 1

    def stage_two (self):
        events = [
            "She doesn't show up for a date.",
            "She forgets to call or respond to a text.",
            "You send another text.",
            "You make another phone call.",
            "You ask to go out on another date.",
            "You ask, 'Are we OK?'",
            "You ask, 'How come we don't talk anymore?'"
        ]
        for event in events:
            print (event)
            time.sleep (1)
        self.current_stage += 1

    def stage_three (self):
        attempts = 0
        while attempts < 3:
            print ("You try to call or text, but she doesn't answer.")
            attempts += 1
            time.sleep (1)
        print ("Her loss. Let's find you the one.")
        self.current_stage = 0  # Restart the loop

    def run (self):
        while True:
            pass


import time


class DateSimulation:
    def __init__ (self):
        self.stages = [self.stage_one, self.stage_two, self.stage_three]
        self.current_stage = 0

    def stage_one (self):
        dates = ["Ice cream", "Movies", "Dinner", "Concert", "Planning holidays"]
        for date in dates:
            print (f"Date: {date}")
            time.sleep (1)
        self.current_stage += 1

    def stage_two (self):
        events = [
            "She doesn't show up for a date.",
            "She forgets to call or respond to a text.",
            "You send another text.",
            "You make another phone call.",
            "You ask to go out on another date.",
            "You ask, 'Are we OK?'",
            "You ask, 'How come we don't talk anymore?'"
        ]
        for event in events:
            print (event)
            time.sleep (1)
        self.current_stage += 1

    def stage_three (self):
        attempts = 0
        while attempts < 3:
            print ("You try to call or text, but she doesn't answer.")
            attempts += 1
            time.sleep (1)
        print ("Her loss. Let's find you the one.")
        self.current_stage = 0  # Restart the loop

    def run (self):
        while True:
            self.stages [self.current_stage] ()


def simulate_user_input ():
    simulation = DateSimulation ()
    while True:
        simulation.run ()
        time.sleep (random.randint (1, 3))  # Random delay between 1 to 3 seconds


# Run the simulation with random user inputs
simulate_user_input ()


def simulate_user_input ():
    simulation = DateSimulation ()
    while True:
        simulation.run ()
        time.sleep (random.randint (1, 3))  # Random delay between 1 to 3 seconds


# Run the simulation with random user inputs
simulate_user_input ()