from message_module import Message  # Add this import statement


class DatingApp:
    def __init__ (self):
        self.profile = None
        self.messages = self.generate_messages ()
        self.correct_response = "I love reading books!"

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
        print ("Sorry, you didn't find the right match.")
        return False

    def second_date (self):
        print ("\nWelcome to the second date!")
        self.messages = self.generate_messages ()  # Generate new messages for the second date
        self.correct_response = "I love hiking!"  # Change the correct response for the second date
        self.respond_to_messages ()

    def run (self):
        self.profile = Profile.create_profile ()
        self.profile.display_profile ()
        if self.respond_to_messages ():
            self.second_date ()


if __name__ == "__main__":
    app = DatingApp ()
    app.run ()