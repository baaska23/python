points = {'A': 4.0, 'B':3.0, 'C':2.0, 'D':1.0, 'F':0.5 }
num_courses = 0
total_points = 0
done = False
while not done:
  grade = input()
  if grade == '':
    done = True
  elif grade not in points:
    print("Unknown grade")
  else:
    num_courses+=1
    total_points += points[grade]
if num_courses > 0:
  print("Your GPA is {0:.3}".format(total_points/num_courses))