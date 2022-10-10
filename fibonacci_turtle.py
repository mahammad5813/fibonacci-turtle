import turtle
import keyboard, time
t = turtle.Turtle()
t.speed(1000)
def top_right(magnitude):   
    t.penup()
    t.left(45)
    t.fd(magnitude)
    t.right(45)
    t.pendown()
def top_left(magnitude):  
    t.penup()
    t.left(135)
    t.fd(magnitude)
    t.right(135)
    t.pendown()
def bottom_right(magnitude):
    t.penup()
    t.right(45)
    t.fd(magnitude)
    t.left(45)
    t.pendown()
def bottom_left(magnitude):   
    t.penup()
    t.right(135)
    t.fd(magnitude)
    t.left(135)
    t.pendown()
def top(magnitude):   
    t.penup()
    t.left(90)
    t.fd(magnitude)
    t.right(90)
    t.pendown()
def bottom(magnitude):  
    t.penup()
    t.right(90)
    t.fd(magnitude)
    t.left(90)
    t.pendown()
def right(magnitude):   
    t.penup()
    t.fd(magnitude)
    t.pendown()
def left(magnitude):  
    t.penup()
    t.right(180)
    t.fd(magnitude)
    t.left(180)
    t.pendown()


mainloop = True
while mainloop:
    list1 = [0,1]
    t.penup()
    t.left(160)
    t.fd(600)
    t.write('''Q to quit
    R to restart''')
    t.right(180)
    t.fd(600)
    t.left(20)
    t.pendown()
    location = input('''Where to start?
    c - center     r - right
    t - top        l - left
    b - bottom     tr - top right
    tl - top left  br - bottom right
    bl - bottom left
    > ''').lower()
    
    if location == "c":
        pass
    else:
        initial = int(input("Enter the initial magnitude>> "))
    if location == "r":
        right(initial)
    if location == "l":
        left(initial)
    if location == "t":
        top(initial)
    if location == "b":
        bottom(initial)
    if location == "tr":
        top_right(initial)
    if location == "br":
        bottom_right(initial)
    if location == "tl":
        top_left(initial)
    if location == "bl":
        bottom_left(initial)
    rotation_coefficient = float(input("Enter the rotation coefficient> "))
    magnitude_fd = int(input("Enter forward magnitude> "))
    d_color = input("Enter the color of the drawing> ").lower()
    bg_color = input("Enter the background color> ").lower()
    if d_color:
        t.color(d_color)
    if bg_color:
        turtle.Screen().bgcolor(bg_color)
    step = 0
    while True:
        step+=1
        if step == 100:
            turtle.update()
            step = 0
        # time.sleep(0.00001)
        turtle.tracer(0,0)
        if keyboard.is_pressed("h"):
            t.hideturtle()
        if keyboard.is_pressed("v"):
            t.showturtle()
        if keyboard.is_pressed("f"):
            turtle.update()
        if keyboard.is_pressed("q"):
            mainloop = False
            break
        if keyboard.is_pressed("r"):
            t.clear()
            t.penup()
            t.home()
            break
        number = list1[-1] + list1[-2]
        list1.append(number)
        t.circle(magnitude_fd, 90)
        t._rotate(number%360-rotation_coefficient)
