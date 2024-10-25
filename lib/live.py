class Dog: 
    all = []

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Dog.all.append(self)

# add a class variable all
# add each instance to the list