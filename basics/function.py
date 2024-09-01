#argument-kai parameter-username
def greeting(username):
  print(f"Hello, {username}")

greeting('Kai')

def describe_pet(animal_type, pet_name):
  print(f"\nI have a {animal_type}")
  print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('dog', 'Trump') 
describe_pet(animal_type='jaguar', pet_name='hudson')

def get_formatted_name(first, last):
  full_name = f"{first} {last}"
  return full_name.title()

musician = get_formatted_name('Jamie', 'Foxx')
print(musician)

def build_person(firstname, lastname):
  person = {'first': firstname, 'last':lastname}
  return person
actor = build_person('Leo', 'Dicap')
print(actor)

#arbitrary number of arguments
def make_pizza(size, *toppings):
  print(size, toppings)

make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')