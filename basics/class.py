from random import randint, choice
class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def sit(self):
    print(f"{self.name} is asleep")

my_dog = Dog('Klay', 2)
print(f"My dog's name is {my_dog.name} and he's {my_dog.age} years old")

class Car:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer = 0
  def get_descriptive_name(self):
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()
  def read_odometer(self):
    print(f"this car has {self.odometer} miles on it")
  
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#python library
rand = randint(1,10)
print(rand)

players = ['sara', 'kevin', 'heily', 'dona']
chosen = choice(players)
print(chosen)

#class name should be written in CamelCase