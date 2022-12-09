import turtle as trtl
import time
import random as rand
#initializes the background screen
wn = trtl.Screen()
wn.screensize(canvwidth=600,canvheight=600)
wn.bgpic("PakistanFlag.gif")
#objective number 
objectiveNumber = 8
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
writer.goto(-300,100)
#writes the users objective
writer.write('''Your goal is to reach 
Pakistan with your family:
\n'''+ familyNamesList[0] + " and " + familyNamesList[1], font=("Arial",30,'bold'))
time.sleep(3)

writer.clear()
#gives the user the objective for the minigame
writer.write('''Protect you and your family \nfrom the turtles for 10 seconds, 
\nyou must eliminate at least ''' + str(objectiveNumber) + ''' 
\nturtles to keep your family alive!''',font=("Arial",30,'bold'))
time.sleep(4)
writer.clear()
#draws the screen for the player to play on
wn.bgpic("nopic")
wn.bgcolor("brown")
#creates the variables for the stick figures
legLength = 40
armLength = 20
bodyLength = 60
HeadSize = 40
xcor = -100
color = "black"
#prepares the drawer turtle and it's attributes
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
#sets up a timer and score countrer from the a1.2.1
score = 0
timer = 10
counter_interval = 1000   #1000 represents 1 second
timer_up = False
font_setup = ("Arial", 20, "normal")

#countdown turtle and function
counter =  trtl.Turtle()
counter.penup()
counter.hideturtle()
counter.goto(-250,250)
def countdown():
    global timer, timer_up,spot
    counter.clear() # clears what was previously written
    if timer <= 0: #makes timer up true so the counter stops counting
        counter.write("Time's Up", font=font_setup)
        timer_up = True
        #CHECKS IF THE USER HAS LOST
        if timer_up and score<objectiveNumber:
            wn.bgcolor("white")
            painter.clear()
            writer.goto(0,0)
            writer.write("you lose!",font=font_setup)
    else: #decreases and writes the timer
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval) 
        spot.forward(40)

#makes the score
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(250,250)
#updates the score function
def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)
#creates the variables for the turtles
spot = trtl.Turtle()
spot.penup()
spot.goto(100,100)
spot_color = "blue"
spot_size = 2
spot_shape = "turtle" 
spot.fillcolor(spot_color)
spot.shapesize(spot_size)
spot.shape(spot_shape)
#creates the spots new positions
def change_position():
        #creates the variables for the turtle to go to a random 
        #spot but away from the stickfigure
    new_xpos= rand.randint(-200,200)
    new_ypos = rand.randint(-200,200)
    spot.hideturtle()
    spot.goto(new_xpos, new_ypos)
    if spot.ycor() < 0:
        spot.setheading(90)
    else: 
        spot.setheading(270)
    spot.showturtle()
#creates the fuction to call all other functions when spot is clicked
#return how far away the turtle was before clicked
def spot_clicked(x, y):
    if timer_up != True:
        update_score()
        change_position()
    else:
        spot.hideturtle()
#creates the kill function

def kill(familylist):
    index = rand.randint(0,len(familylist))
    

    killed = familylist[index] 
    return killed
#action for when spot is clicked
spot.onclick(spot_clicked)
#countdown call
wn.ontimer(countdown, counter_interval)
#checks if the user has lost


wn.mainloop()
