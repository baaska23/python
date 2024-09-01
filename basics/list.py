#list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles[3] = "giant"
bicycles.append("hondashu")
bicycles.insert(-1, "tokui")
bicycles.pop()
bicycles.remove("cannondale")
del bicycles[0]
for x in bicycles:
  print(x)
message = f"My first bicycle was {bicycles[1].title()}"
print(bicycles[0].title())
print(message)
bicycles.sort()
bicycles.reverse()
print(bicycles)
print(len(bicycles))

magicians = ['alisa', 'tom', 'kai']
for magician in magicians:
  print(f"{magician.title()}, that was great!")

pizzas = ['hawai', 'pepporoni', 'tuna']
for pizza in pizzas:
  print(f"I love {pizza.title()} pizza")

for value in range(1, 10):
  print(value)

numbers = list(range(1, 10))
odd = list(range(1, 12, 2))
print(odd)

squares = []
for value in range(1, 11):
  square = value ** 2
  squares.append(square)
print(squares)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[2:])

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

tuples = (200, 50, 12)
for n in tuples:
  print(n)