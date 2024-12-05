import random


class Profile:
    def __init__ (self, name, age, location, kids, want_kids, relationship_type, max_distance):
        self.name = name
        self.age = age
        self.location = location
        self.kids = kids
        self.want_kids = want_kids
        self.relationship_type = relationship_type
        self.max_distance = max_distance

    @classmethod
    def create_profile (cls):
        name = input ("Enter your name: ")
        age = input ("Enter your age: ")
        location = input ("Enter your location: ")
        kids = input ("Do you have kids? (yes/no): ")
        want_kids = input ("Do you want kids? (yes/no): ")
        relationship_type = input ("Are you looking for love or something casual? ")
        max_distance = input ("What's the maximum distance you're willing to date (in miles)? ")
        return cls (name, age, location, kids, want_kids, relationship_type, max_distance)

    def display_profile (self):
        print ("\nYour Profile:")
        print (f"Name: {self.name}")
        print (f"Age: {self.age}")
        print (f"Location: {self.location}")
        print (f"Kids: {self.kids}")
        print (f"Want Kids: {self.want_kids}")
        print (f"Relationship Type: {self.relationship_type}")
        print (f"Max Distance: {self.max_distance} miles")


class Message:
    def __init__ (self, content):
        self.content = content

    def display_message (self, index):
        print (f"\nMessage {index + 1}: {self.content}")


class DatingApp:
    def __init__ (self):
        self.profile = None
        self.messages = self.generate_messages ()
        self.correct_response = "I love reading books!"
        self.girlfriends = [Girlfriend (name) for name in ["Alice", "Bella", "Catherine", "Diana", "Eva", "Fiona", "Grace", "Hannah", "Isla", "Julia"]]
        self.current_girlfriend = None


class Girlfriend:
    def __init__ (self, name, attributes, likes, dislikes):
        self.name = name
        self.attributes = attributes
        self.likes = likes
        self.dislikes = dislikes
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
        self.girlfriends = self.generate_girlfriends ()
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

    def generate_girlfriends (self):
        names = ["Alice", "Bella", "Catherine", "Diana", "Eva", "Fiona", "Grace", "Hannah", "Isla", "Julia"]
        attributes = ["kind", "funny", "intelligent", "adventurous", "creative"]
        likes = ["reading", "traveling", "cooking", "sports", "music"]
        dislikes = ["laziness", "rudeness", "dishonesty", "boredom", "negativity"]
        return [Girlfriend (name, random.choice (attributes), random.choice (likes), random.choice (dislikes)) for name in names]

    def display_welcome_message (self):
        print ("Welcome to Ira's Game of Love!")
        print ("Let's build your profile to find the best matches for you.")

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
        self.display_welcome_message ()
        self.profile = Profile.create_profile ()
        self.profile.display_profile ()

        while self.girlfriends:
            self.current_girlfriend = random.choice (self.girlfriends)
            print (f"\nYou are now dating {self.current_girlfriend.name}.")
            print (f"Attributes: {self.current_girlfriend.attributes}")
            print (f"Likes: {self.current_girlfriend.likes}")
            print (f"Dislikes: {self.current_girlfriend.dislikes}")
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

    # Example of using repr() correctly
    example_object = "This is an example"
    print (repr (example_object))  # This will print the string representation of 'example_object'