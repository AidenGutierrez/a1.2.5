import turtle as trtl
import time
#initializes the background screen
wn = trtl.Screen()
wn.bgcolor("black")
wn.bgpic("PakistanFlag.gif")
#creates the list of family members 
familyNamesList = []
for i in range (2):
    familyNames = trtl.textinput("family names", "Please input a family name:")
    familyNamesList.append(familyNames)
#makes the writer
writer = trtl.Turtle()
writer.color("red")
writer.hideturtle()
writer.penup()
writer.goto(-450,100)
#writes the users objective
writer.write('''Your goal is to reach 
Pakistan with your family:
\n'''+ familyNamesList[0] + " and " + familyNamesList[1], font=("Arial",30,'bold'))
time.sleep(3)

writer.clear()
#gives the user the objective for the minigame
writer.write('''Protect you and your family \nfrom the turtles for 10 seconds, 
\nyou must eliminate at least 15 \nturtles to keep your family alive!''',font=("Arial",30,'bold'))
time.sleep(4)
writer.clear()
#draws the screen for the player to play on
wn.bgpic("nopic")
wn.bgcolor("brown")
legLength = 40
armLength = 20
bodyLength = 60
HeadSize = 40
xcor = -100
color = "black"
#draws each stick figure in different locations
painter = trtl.Turtle()
painter.hideturtle()
painter.speed(0)
painter.fillcolor(color)
for people in range(3):
    #prepares the painter to go to the right spot
    painter.penup()
    painter.goto(xcor,0)
    painter.setheading(0)
    painter.pendown()
    #draws head
    painter.begin_fill()
    painter.circle(HeadSize)
    painter.end_fill()
    #draws body
    painter.right(90)
    painter.forward(bodyLength)
    #draws left leg
    painter.right(45)
    painter.forward(legLength)
    painter.back(legLength)
    #draws right leg
    painter.left(90)
    painter.forward(legLength)
    painter.back(legLength)
    painter.right(45)
    #draws arms in the middle of the body
    painter.back(bodyLength/2)
    painter.right(90)
    painter.forward(armLength)
    painter.back(armLength*2)
    xcor += 100





wn.mainloop()
