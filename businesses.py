from animals import Dog
class Rescue:
    def __init__(self, capacity = 0):
        self.inventory = [Dog]
    def add_dog(self, dog):
        if len(self.inventory) < self.capacity:
            self.inventory.append(dog)
        else:
            print("Over capacity. Cannot add.")

