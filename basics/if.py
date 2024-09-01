#if statements
cars = ['audi', 'bmw', 'honda', 'toyota']
for car in cars:
  if car != 'honda':
    print(car.upper())
  else:
    print(car.lower())
  if 'nissan' in cars:
    print("true")