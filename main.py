# Alyssa Miller alyssa.dannielle@gmail.com
# I'm still just learning
# I use "pies" to keep track of my projects and To Do's - this program wants to replicate that

import turtle

print("Pie Tracker!")
project = input("Enter your project name: ")

slice = []
for i in range(8):
    slice.append(input("Enter a task for that project: ")) # each task is a slice of pie
print(slice)

turtle.hideturtle()
turtle.speed(0)
turtle.circle(100)
turtle.left(90)
turtle.forward(100)

for i in range(7):
    turtle.left(90+45)
    turtle.forward(100)
    turtle.left(180)
    turtle.forward(100)

turtle.done()
