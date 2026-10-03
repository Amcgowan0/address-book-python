class Dog:
    def __init__(self, breed, color, age):
        self.breed = breed
        self.color = color
        self.age = age

    def __eq__(self, other):
        if self.breed == other.breed and \
        self.color == other.color and \
        self.age == other.age:
            return True
        else:
            return False

        

