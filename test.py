class Animal:

    def __init__(self, age, color, race, name): 
        self.age = age 
        self.color = color
        self.race = race
        self.name = name

dog = Animal(25, 'white', 'black', 'Rocko' )
print(dog.name)
userinput = input('Press any key')    


while True:
    dog.name = 'killa'
    print(dog.name)
    if userinput == 't':
        dog.name = 'tpain'
        print(dog.name)
        break
    break
print(dog.name)