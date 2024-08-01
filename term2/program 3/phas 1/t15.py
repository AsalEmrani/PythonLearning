from turtle import *

def go_up() :
   if heading()!= 90:
       setheading(90)
   else:   
       forward(100)

def go_down() :
   if heading()!= 270:
       setheading(270)
   else:   
       forward(100)

def go_left() :
   if heading()!= 180:
       setheading(180)
   else:   
       forward(100)

def go_right() :
   if heading()!= 0:
       setheading(0)
   else:   
       forward(100)

def change_color() :
    fc = textinput('change color ',' fill color : ')
    fillcolor(fc)
    color(fc)
    listen()

def drow_circle() :
    a = int(textinput('draw_circle ',' circle width : '))
    pendown()
    circle(a)
    penup()
    listen()

def drow_rectangle() :
    w = int(textinput('drow_rectangle ',' rectangle wight : '))
    h = int(textinput('drow_rectangle ',' rectangle hight : '))

    pendown()
    for i in range(2) :
        forward(h)
        left(90)
        forward(w)
        left(90)
    penup()
    listen()

 
onkeypress (go_up , 'Up')
onkeypress (go_down , 'Down')
onkeypress (go_left , 'Left')
onkeypress (go_right , 'Right')
onkeypress (clear , 'Delete')
onkeypress (exit , 'Escape')
onkeypress (pendown , 'Shift_L')
onkeyrelease (penup , 'Shift_L')
onkeypress (begin_fill , 'Alt_L')
onkeyrelease (end_fill , 'Alt_L')
onkeypress (change_color , 'g')
onkeypress (drow_circle , 'c')
onkeypress (drow_rectangle , 'r')

penup()
shape("turtle")
listen()







