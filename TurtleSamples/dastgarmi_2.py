from turtle import *
import random
import time 

rnd_list = [0] * 25
circles = [0] * 25
level = 1

def draw_circle(n , c):
    goto(number_to_point(n))
    pendown()
    color(c)
    begin_fill()
    circle(25)
    end_fill()
    penup()    

def number_to_point(n):
    x = (n % 5 * 50 + 25 ) - 125
    y = (n // 5 * 50 ) - 125
    return x, y

def point_to_number(x, y):
    row = (y + 125) // 50
    col = (x + 125) // 50
    n = int(row * 5 + col)
    
    if(0 <= row <= 4 and 0 <= col <= 4):
        if(circles[n] == 0):
            circles[n] = 1
            draw_circle(n,'skyblue')
        elif (circles[n] == 1):
            circles[n] = 0
            draw_circle(n,'beige')
        
def init_circles():
    for i in range(25):
        circles[i] = 0
        rnd_list[i] = 0
        draw_circle(i,'beige')
    
    # sample يه تابع 
    random_list = random.sample(range(25), level)
    print(random_list)
    for i in random_list:
        draw_circle(i, "limegreen")
        rnd_list[i] = 1

    time.sleep(1)
    for i in random_list:
        draw_circle(i, "beige")

def compare():
    print(rnd_list)
    print(circles)

    global level
    ok = True

    for i in range(25):
        if circles[i] == 1 and rnd_list[i] == 0:
            draw_circle(i, "red")
            ok = False
            
        if circles[i] == 0 and rnd_list[i] == 1:
            draw_circle(i, "yellow")
            ok = False
            
        if circles[i] == 1 and rnd_list[i] == 1:
            draw_circle(i, "lightgreen")

    if ok == True:
        print("Good Job")
        level = level + 1
    else:
        print("Sorry! you lost")
        level = 1
        
    init_circles()
    
    
ht()
penup()
speed(0)
init_circles()

listen()
onscreenclick( point_to_number )
onkeypress(init_circles, 'Control_L' )
onkeypress(compare, 'Return')

