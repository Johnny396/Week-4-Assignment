"""Person"""
class Person:
    """Person"""
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        """Introduction"""
        print(f"My name is {self.name}. I am {self.age} years old. I am a {self.gender}.")


details = Person("Ikoobong", 31, "Male")
details.introduce()
