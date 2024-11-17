import random


class Profile:
    def __init__ (self, name, age, gender, interests):
        self.name = name
        self.age = age
        self.gender = gender
        self.interests = interests

    @classmethod
    def create_profile (cls):
        name = input ("Enter your name: ")
        age = input ("Enter your age: ")
        gender = input ("Enter your gender: ")
        interests = input ("Enter your interests (comma separated): ").split (',')
        return cls (name, age, gender, interests)

    def display_profile (self):
        print ("\nYour Profile:")
        print (f"Name: {self.name}")
        print (f"Age: {self.age}")
        print (f"Gender: {self.gender}")
        print (f"Interests: {', '.join (self.interests)}")


class Message:
    def __init__ (self, content):
        self.content = content

    def display_message (self, index):
        print (f"\nMessage {index + 1}: {self.content}")


class Girlfriend:
    def __init__ (self, name):
        self.name = name
        self.distancing_level = 0

    def distance (self):
        self.distancing_level += 1

    def is_ghosting (self):
        return self.distancing_level >= 3


class DatingApp:
    def __init__ (self):
        self.profile = None
        self.messages = self.generate_messages ()
        self.correct_response = "I love reading books!"
        self.girlfriends = [Girlfriend (name) for name in ["Alice", "Bella", "Catherine", "Diana", "Eva", "Fiona", "Grace", "Hannah", "Isla", "Julia"]]
        self.current_girlfriend = None

    def generate_messages (self):
        messages_content = [
            "Hi! How are you?",
            "What's your favorite hobby?",
            "Do you like traveling?",
            "What's your favorite movie?",
            "Do you have any pets?",
            "What's your dream job?",
            "Do you like cooking?",
            "What's your favorite book?",
            "Do you play any sports?",
            "What's your favorite music genre?"
        ]
        return [Message (content) for content in messages_content]

    def respond_to_messages (self):
        for i, message in enumerate (self.messages):
            message.display_message (i)
            response = input ("Your response: ")
            if response == self.correct_response:
                print ("Congratulations! You found the right match!")
                return True
            else:
                self.current_girlfriend.distance ()
                if self.current_girlfriend.is_ghosting ():
                    print (f"Sorry, {self.current_girlfriend.name} is ghosting you. Starting over...")
                    return False
        return False

    def run (self):
        self.profile = Profile.create_profile ()
        self.profile.display_profile ()

        while self.girlfriends:
            self.current_girlfriend = random.choice (self.girlfriends)
            print (f"\nYou are now dating {self.current_girlfriend.name}.")
            success = self.respond_to_messages ()
            if success:
                break
            else:
                self.girlfriends.remove (self.current_girlfriend)
                if not self.girlfriends:
                    print ("No more women to date. Game over.")
                    break


if __name__ == "__main__":
    app = DatingApp ()
    app.run ()