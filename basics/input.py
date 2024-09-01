message=input("whats your height: ")
message = int(message)

if message >= 60:
  print("Nice!")
else:
  print("Sheiße")

curr = 1
while curr <= 5:
  print(curr)
  curr += 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
  message = input(prompt)
  print(message)

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
  pets.remove('cat')
  break #finished after first loop

print(pets)

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
  current_user= unconfirmed_users.pop()
  print(f"Verifying user: {current_user.title()}")
  confirmed_users.append(current_user)

print("\nThe following users have been confirmed: ")
for confirmed in confirmed_users:
  print(confirmed.title())
