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
        names = ["John", "Jane", "Alex", "Emily", "Chris", "Katie"]
        locations = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
        relationship_types = ["love", "something casual"]

        name = random.choice (names)
        age = random.randint (18, 60)
        location = random.choice (locations)
        kids = random.choice (["yes", "no"])
        want_kids = random.choice (["yes", "no"])
        relationship_type = random.choice (relationship_types)
        max_distance = random.randint (1, 100)

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


if __name__ == "__main__":
    profile = Profile.create_profile ()
    profile.display_profile ()