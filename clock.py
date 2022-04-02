# clock module
import turtle as t
# time data
hours = 8
minutes = 55
seconds = 12

#print the time
def printTime():
    print( f"{hours:02}:{minutes:02}:{seconds:02}" )

# draw clock with turtle
def drawClock():
    t.pensize(5)
    t.color("blue")
    t.circle(100)
    t.left(90)
    t.penup()
    t.forward(100)
    
    # clock center dot
    t.color("red")
    t.forward(4)
    t.left(90)
    t.pendown()
    t.circle(2)
    
    # reset the pen
    t.penup()
    t.right(90)
    
    # hours indicator
    t.color("black")
    t.pendown()
    t.right(hours * 30)
    t.forward(65)
    
    # reset the pen
    t.penup()
    t.left(180)
    t.forward(65)
    t.right(180-hours * 30)
    
    # minutes indicator
    t.color("green")
    t.pensize(2)
    t.pendown()
    t.right(minutes * 6)
    t.forward(80)

    # reset the pen
    t.pensize(1)
    t.penup()
    t.left(180)
    t.forward(80)
    t.right(180-minutes * 6)
  
    # seconds indicator
    t.color("red")
    t.pendown()
    t.right(seconds * 6)
    t.forward(90)
    
    t.mainloop()