# Name: Jayton Fee
# mean.py
# Problem: Make a Valentines Day Card. Needs to have a heart and a
# shooting arrow.
# Certification of Authenticity:
# I certify that this lab is entirely my own work.
# Inputs: If inputs are used they will be mouse clicks from the user
# on the window or text entries in the created window. These inputs
# need to be piped into the code.
# Outputs: All outputs need to go to the created window.


from graphics import *
import time


def valentinesCard(text):

    # build window
    winWidth = 500
    winHeight = 700
    win = GraphWin("Valentines Day Card", winWidth, winHeight)
    win.setBackground("blue")

    # clouds
    cloudCluster(10,10, win)
    cloudCluster(400,25, win)
    cloudCluster(450, 20, win)
    cloudCluster(200,35,win)
    cloudCluster(225, 15, win)

    # build heart
    heart = Polygon(Point(201.0, 602.0), Point(150.0, 551.0),
                    Point(148.0, 546.0), Point(146.0, 540.0),
                    Point(144.0, 534.0), Point(145.0, 527.0),
                    Point(146.0, 523.0), Point(147.5, 519.0),
                    Point(149.0, 516.0), Point(152.0, 511.0),
                    Point(156.0, 508.0), Point(160.0, 506.0),
                    Point(163.0, 504.0), Point(170.0, 501.0),
                    Point(177.0, 501.0), Point(181.0, 501.0),
                    Point(186.0, 504.0), Point(192.0, 508.0),
                    Point(196.0, 511.0), Point(199.0, 515.0),
                    Point(200.0, 517.0), Point(204.0, 513.0),
                    Point(208.0, 509.0), Point(214.0, 504.0),
                    Point(220.0, 502.0), Point(228.0, 501.0),
                    Point(232.0, 501.0), Point(236.0, 502.0),
                    Point(240.0, 502.0), Point(244.0, 505.0),
                    Point(247.0, 507.0), Point(250.0, 510.0),
                    Point(253.0, 514.0), Point(254.0, 518.0),
                    Point(255.0, 520.0), Point(257.0, 526.0),
                    Point(257.0, 534.0), Point(257.0, 542.0),
                    Point(254.0, 547.0), Point(250.0, 551.0),
                    Point(201.0, 602.0))

    # move heart and change the color
    colorChange(heart, "pink")
    heart.draw(win)
    moveShape(heart, 2, 2, 48, .01)
    colorChange(heart, "red")
    moveShape(heart, 2, -2, 74, .01)
    colorChange(heart, "pink")
    moveShape(heart, -2, -2, 194, .01)
    colorChange(heart, "red")
    moveShape(heart, 2, -2, 32, .01)
    colorChange(heart, "pink")
    moveShape(heart, 2, 2, 163, .01)
    colorChange(heart, "red")
    moveShape(heart, -2, 2, 136, .01)
    colorChange(heart, "pink")
    moveShape(heart, -2, -2, 61, .01)
    colorChange(heart, "red")
    moveShape(heart, 2, -2, 99, .01)

    # Build message set to "Be Mine?"
    message = Text(Point(250, 200), "Be Mine?")
    message.setTextColor("Red")
    message.setSize(30)

    # Build Instructions for text Input
    instructions = Text(Point(150, 500), text)
    instructions.setTextColor("Pink")
    instructions.setSize(15)

    # Build text box to take "Be Mine" input
    beMineInput = Entry(Point(250, 500), 5)
    beMineInput.setFill("red")
    beMineInput.setTextColor("white")

    # Draw message, instructions, and input box
    message.draw(win)
    instructions.draw(win)
    beMineInput.draw(win)

    # Grab input from user
    win.getMouse()
    beMineAns = beMineInput.getText()
    beMineAns = beMineAns.lower()

    # Un-draw after input
    beMineInput.undraw()
    instructions.undraw()

    # Use Be Mine Input for conditional statement
    if beMineAns == "yes":
        # Fires the Arrows
        positiveSlopeArrows(11, 765, win)
        negativeSlopeArrows(491, 765, win)
        straightArrow(251, 701, win)
        # Changes message text and swap color of heart
        message.setText("Not Today Cupid!!!")
        colorChange(heart, "pink")
        #Move heart and message. Change message size
        moveShape(heart, 0, -4, 100, .01)
        moveShape(message, 0, 2, 75, .01)
        message.setSize(31)
        time.sleep(.01)
        message.setSize(32)
        time.sleep(.01)
        message.setSize(33)
        time.sleep(.01)
        message.setSize(34)
        time.sleep(.01)
        message.setSize(35)
        time.sleep(.01)
        message.setSize(36)
        message.setText("Happy Valentines Day!")
        time.sleep(5)
        win.close()

    else:
        message.setText("Try Again...")
        time.sleep(1)
        win.close()
        valentinesCard("I would choose yes...\nDon't forget to click")
        

def colorChange(shape, color):
    shape.setFill(color)
    shape.setOutline(color)


def moveShape(shape, dx, dy, times, delay):
    for i in range(times):
        time.sleep(delay)
        shape.move(dx, dy)


def cloudCluster(x, y, win):
    cloud1 = Circle(Point(x, y), 30)
    cloud2 = Circle(Point(x+10,y+15),40)
    cloud3 = Circle(Point(x+50,y),35)
    cloud4 = Circle(Point(x+45,y+25),25)
    colorChange(cloud1,"white")
    colorChange(cloud2,"white")
    colorChange(cloud3, "white")
    colorChange(cloud4, "white")
    cloud1.draw(win)
    cloud2.draw(win)
    cloud3.draw(win)
    cloud4.draw(win)


def positiveSlopeArrows(x, y, win):
    pSArrow = Line(Point(x, y), Point(x+50, y-65))
    pSArrow.setWidth(3)
    pSArrow.draw(win)
    pSArrow.setArrow("last")
    moveShape(pSArrow,1.5, -2.75, 300, .001)


def negativeSlopeArrows(x, y, win):
    nSArrow = Line(Point(x, y), Point(x-50, y-65))
    nSArrow.setWidth(3)
    nSArrow.draw(win)
    nSArrow.setArrow("last")
    moveShape(nSArrow, -1.5, -2.75, 300, .001)


def straightArrow(x, y, win):
    straightArrow = Line(Point(x, y), Point(x, y+70))
    straightArrow.setWidth(3)
    straightArrow.draw(win)
    straightArrow.setArrow("first")
    moveShape(straightArrow, 0, -2.75, 300, .001)


valentinesCard("Enter yes or no: \nClick to "
                                    "continue")
