from user import User
import random  # Ensure the random module is imported

class Teacher(User):
    def __init__(self, first_name, last_name) -> None:
        super().__init__(first_name, last_name)
        self.knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]

    def teach(self):
        '''Returns a random knowledge string from the knowledge list.'''
        random_index = random.randint(0, len(self.knowledge) - 1)  # Get a random index
        return self.knowledge[random_index]  # Return the element at that index
