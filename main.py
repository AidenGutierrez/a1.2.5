import turtle as trtl
import time
wn = trtl.Screen()

wn.screensize(canvwidth=500,canvheight=300,bg="black")
#starts by asking user for their name
Inputname = trtl.textinput("name", "Please insert your name.")
#initializes turtles
phoneDrawer = trtl.Turtle()
phoneDrawer.speed(0)
friendTextDrawer = trtl.Turtle()
friendTextDrawer.speed(0)
friendTextDrawer.hideturtle()
def textMessage(UserName):
    #globals the friendTextDrawer for later
    global friendTextDrawer

    #sets up the drawer
    global phoneDrawer
    phoneDrawer.penup()
    phoneDrawer.fillcolor("white")
    phoneDrawer.goto(-320,250)
    phoneDrawer.begin_fill()
    phoneDrawer.pendown()
    #draws the rectangle for the phone
    for i in range(2):
        phoneDrawer.forward(640)
        phoneDrawer.right(90)
        for x in range(1):
            phoneDrawer.forward(700)
            phoneDrawer.right(90)
    phoneDrawer.end_fill()
    phoneDrawer.hideturtle()
    #draws the friendTexts on screen
    friendTextDrawer.penup()
    friendTextDrawer.color("blue")
    friendTextDrawer.goto(-300,50)
    friendTextDrawer.write("Alex: \nHey " + UserName + ", \nwanna hang out today?", font=('Arial',20,'bold'))
    #draws the new text
    friendTextDrawer.goto(50,-100)
    friendTextDrawer.color("green")
    friendTextDrawer.write("Me: \nSure! Let me ask \nmy mom!",font=('Ariel',20, 'bold'))
#calls on the name function
textMessage(Inputname)
time.sleep(1)
friendTextDrawer.clear()
phoneDrawer.clear()
#makes the user input family names
familyNamesList = []
for i in range(2):
    familynames = trtl.textinput("familyNames", "Please input a sibling names.")
    familyNamesList.append(familynames)
print(familyNamesList)
#puts the mom picture in a variable
angryMomPic = "AngryMom.gif"
#creates the scene with angry mom
def momScene(familylist):
    #globals the family name
    index = 0
    #draws the mom pic on the screen as a background
    wn.bgpic(angryMomPic)
    familymember1 = familylist.pop(index)
    #sets up the text drawer
    selfTextDrawer = trtl.Turtle()
    selfTextDrawer.penup()
    selfTextDrawer.color('white')
    selfTextDrawer.goto(0,0)
    selfTextDrawer.write("No Mijo!\n you have to make your siblings Happy!", font=('Arial',20,'bold'))

#have noth siblings on screen that require both of them to be at 100% happy at the same time
#increase happiness by clicking on them a certain amount of times
#happiness level of the babies can go over 100%
#creates the sibling screen
def siblingScreen():
    wn.bgcolor("white")





momScene(familyNamesList)
siblingScreen()
wn.mainloop()