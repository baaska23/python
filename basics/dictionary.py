alien_0 = {'color':'blue', 'height': 180}
print(alien_0['color'])
alien_0['gender'] = 'any/all haha'
del alien_0['gender']
#if the key you ask doesnt exist
point_value = alien_0.get('weight', 'No weight is recorded')
print(alien_0)

user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

for key, value in user_0.items():
  print(f"\nKey: {key}")
  print(f"Value: {value}")

for key in user_0.keys():
  print(f"Keys are {key}")

for val in user_0.values():
  print(f"\tValues are {val}")

aliens = []
for alien_number in range (30):
  new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
  aliens.append(new_alien)

for alien in aliens[:3]:
  if alien['color'] == 'green':
    alien['color'] = 'yellow'
    alien['speed'] = 'medium'
    alien['points'] = 10
for alien in aliens[:5]:
  print(alien)

#dictionary inside dictionary
users = {
'aeinstein': {
  'first': 'albert',
  'last': 'einstein',
  'location': 'princeton',
  },
'mcurie': {
  'first': 'marie',
  'last': 'curie',
  'location': 'paris',
  },
}
for username, user_info in users.items():
  print(f"\nUsername: {username}")
  full_name = f"{user_info['first']} {user_info['last']}"
  location = user_info['location']

  print(f"\tFull name: {full_name.title()}")
  print(f"\tLocation: {location.title()}")