## Jayton fee
## lab4.py

from valentineGreeting import *


def sequence():
    numTerms = eval(input(
        "How many terms do you want to display in the sequence: "))
    for i in range(numTerms):
        term = i + 1 + i % 2
        print(term, end=" ")
    print()
def pi():
    numTerms = eval(input(
        "How many terms do you want to display in the sequence: "))
    ans = 1
    for i in range(numTerms):
        denom = i + 1 + i % 2
        numerator =  i + 1 + (1 + i)  % 2
        fraction = numerator/denom
        ans = ans * fraction
    ans = ans * 2
    print(ans)
def pi2():
    numTerms = int(input("How many terms do you want to display in "
                         "the sequence? "))
    ans = 0
    denom = -1
    numerator = 4
    for i in range(numTerms):
        denom = denom + 2
        ans = ans + numerator/denom
        numerator = numerator * -1
    print(ans)


def circles():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 200
    height = 500
    win = GraphWin("Lab 4 - Squares", width, height)

    # number of times user can move circle
    numClicks = 5

    # create a space to instruct user
    instPt = Point(width / 2, height - 10)
    instructions = Text(instPt, "Click to move circle")
    instructions.draw(win)

    # builds a circle
    shape = Circle(Point(50, 50), 20)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the
    # circle
    for i in range(numClicks):
        p = win.getMouse()
        c = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx, dy)

    instructions.setText("Click again to close")
    win.getMouse()
    win.close()


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 200
    height = 500
    win = GraphWin("Lab 4 - Squares", width, height)

    # number of times user can move circle
    numClicks = 5

    # create a space to instruct user
    instPt = Point(width / 2, height - 10)
    instructions = Text(instPt, "Click to place a new square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(100,100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the
    # circle
    for i in range(numClicks):
        p = win.getMouse()
        c = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        copySquare = shape.clone()
        copySquare.draw(win)
        copySquare.move(dx,dy)

    instructions.setText("Click again to close")
    win.getMouse()
    win.close()



def displayHouse():
    win = GraphWin("My House", 600, 600)
    frame = Rectangle(Point(10,300),Point(300,500))
    frame.draw(win)
    door = Rectangle(Point(145,500),Point(165,450))
    door.draw(win)
    window1 = Circle(Point(230,440),10)
    window1.draw(win)
    window2 = Circle(Point(80,440),10)
    window2.draw(win)
    roof = Polygon(Point(10,300),Point(155,165),Point(300,300))
    roof.draw(win)
    # Example: aCircle.setFill(color rgb(130, 0, 130))
    frame.setFill("Brown")
    door.setFill("Red")
    window1.setFill("Blue")
    window2.setFill("Blue")
    roof.setFill("Beige")

    p = win.getMouse()
    print(p)


    win.getMouse()

def main():
    # sequence()
    squares()
    displayHouse()
    pi2()
    pi()
main()



