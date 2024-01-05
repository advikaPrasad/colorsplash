import turtle
import random

window = turtle.Screen()
window.setup(800, 600)
window.title('colorsplash')

t = turtle.Turtle()
t.speed("fastest")
t.pencolor("gold")
t.penup()
t.hideturtle()

def draw_germ(x, y, color):
    
    t = turtle.Turtle()
    t.speed("fastest")
    t.penup()
    t.goto(x, y)
    t.pensize(5)
    t.pencolor("lime")
    t.pendown()
    t.hideturtle()
    
    for i in range(150):
        t.forward(i)
        t.left(170)
        
for count in range(4):
    draw_germ(random.randint(-400, 400), random.randint(-300, 300), "lime")
    
    
    
def draw_germ2(x, y, color):
    
    t = turtle.Turtle()
    t.speed("fastest")
    t.penup()
    t.goto(x, y)
    t.pensize(5)
    t.pencolor("red")
    t.pendown()
    t.hideturtle()
    
    for i in range(150):
        t.forward(i)
        t.left(170)
        
for count in range(4):
    draw_germ2(random.randint(-400, 400), random.randint(-300, 300), "red")
    
def draw_germ3(x, y, color):
    
    t = turtle.Turtle()
    t.speed("fastest")
    t.penup()
    t.goto(x, y)
    t.pensize(5)
    t.pencolor("brown")
    t.pendown()
    t.hideturtle()
    
    for i in range(150):
        t.forward(i)
        t.left(170)
        
for count in range(4):
    draw_germ3(random.randint(-400, 400), random.randint(-300, 300), "brown")
    
def draw_germ3(x, y, color):
    
    t = turtle.Turtle()
    t.speed("fastest")
    t.penup()
    t.goto(x, y)
    t.pensize(5)
    t.pencolor("silver")
    t.pendown()
    t.hideturtle()
    
    for i in range(150):
        t.forward(i)
        t.left(170)
        
for count in range(4):
    draw_germ3(random.randint(-400, 400), random.randint(-300, 300), "silver")
    
def draw_germ3(x, y, color):
    
    t = turtle.Turtle()
    t.speed("fastest")
    t.penup()
    t.goto(x, y)
    t.pensize(5)
    t.pencolor("gold")
    t.pendown()
    t.hideturtle()
    
    for i in range(150):
        t.forward(i)
        t.left(170)
        
for count in range(4):
    draw_germ3(random.randint(-400, 400), random.randint(-300, 300), "gold")