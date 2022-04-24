# Alyssa Miller alyssa.dannielle@gmail.com
# I'm still just learning
# I use "pies" to keep track of my projects and To Do's - this program wants to replicate that

import turtle

def header(title, char):
    length = len(title) + 4
    print(char * length)
    print(char, title, char)
    print(char * length)

header("Pie Tracker", "%")
print()

project = input("Give this project a name: ")
pies = eval(input("How many pies do you need for " + project.title() + "? ")) * 8

slice = []
for i in range(pies):
    slice.append(input("Write one simple step for " + project + ": ")) # each task is a slice of pie
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

#>fill slice upon task completion
#>congratulations you completed x pies! and/or x slices!
#>congratulations you survived! if none completed
