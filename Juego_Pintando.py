from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    if start.x==end.x or (end.x - start.x) <= 1:
        left(90)
        diameter = (end.y - start.y)  # Calculate the diameter of the circle
        circumference = 2 * 3.14159 * diameter  # Calculate the circumference
        side_length = circumference / 360  # Calculate the side length for each degree
        begin_fill()

        for count in range(360):
            forward(side_length)
            left(1)
        end_fill()
        right(90)


    else:
        diameter = (end.x - start.x)  # Calculate the diameter of the circle
        # Calculate the radius of the circle
        circumference = 3.1416 * diameter*2  # Calculate the circumference
        side_length = circumference / 360  # Calculate the side length for each degree
        begin_fill()

        for count in range(360):
            forward(side_length)
            left(1)
        end_fill()

def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    if start.x==end.x or (end.x - start.x) <= 1: # if the rectangle is in the "y" axis 
        for count in range(2):  # 2 times because its only 2 high and 2 lenght
            forward(2*(end.y - start.y)) # its .y because is in the "Y" axis, and its 2 times because its the length
            left(90)
            forward(end.y - start.y) # its .y because is in the "Y" axis, and its only one time because its the high
            left(90)
            
        end_fill()
    
    else: 
        for count in range(2): # 2 times because its only 2 high and 2 lenght
            forward(end.x - start.x) # its .x because is in the "x" axis. its only one time because its the high
            left(90)
            forward(2*(end.x - start.x)) # its .x because is in the "x" axis. its 2 times because its the length
            left(90)  

        end_fill()

def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    if start.x==end.x or (end.x - start.x) <= 1:
        left(90) # turn left to look to the 2nd click
        for count in range (3): #sides of the triangle
            forward(end.y - start.y)
            left(120) # angle of equilateral triangle (60º) + 90 degrees
        end_fill()
        right(90) #turn right. restart original position
    
    else:
        
        for count in range (3): #sides of the triangle
            forward(end.x - start.x) 
            left(120) # angle of equilateral triangle (60º) + 90 degrees
        
        end_fill()

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'y') # color yellow 
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()