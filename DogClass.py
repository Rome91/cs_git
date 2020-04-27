class Dog:
    def __init__(self, name, breed, age, aggressive):
        self.name = name
        self.breed = breed
        self.age = age
        self.aggressive = aggressive

    def dog_info(self):
        return f"Name: {self.name}\nBreed: {self.breed}\nAge: {self.age}\nAgressive: {self.aggressive}"


dog1 = Dog("Rocko", "German Shepherd", 7, False)
dog2 = Dog("Ella", "Dachshund", 14, True)
