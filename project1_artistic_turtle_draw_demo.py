import turtle
import random
import panda
import math

# Set up the Turtle screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create a Turtle for drawing
pen_turtle = turtle.Turtle()
pen_turtle.speed(0)  # Set the maximum drawing speed
pen_turtle.shape("blank")

def draw_circle(t, x, y, radius, color):
    """
    Function to draw a filled circle with the given radius and color at location(x, y)
    """
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_sun_beams(t, x, y, color, outer_radius, beam_length):
    """
    Function to draw a beam with the given color, outer_radius, beam_length at location(x, y)
    """
    t.seth(0)
    t.goto(x, y)
    t.up()
    t.color(color)
    for _ in range(12): # 12 beams
        t.forward(outer_radius - beam_length)
        t.down()
        t.forward(beam_length)
        t.up()
        t.backward(outer_radius)
        t.left(360/12)

def draw_dandelion_seed(t, x, y, size, stem_angle):
    """Function to draw a dandelion seed shape"""
    draw_sun_beams(t, x, y, "white", size, size)
    # Add a stem
    t.right(stem_angle)
    t.down()
    t.width(size / 10) # Make the stem line thicker than the seed line
    t.forward(2 * size)
    t.width(1) # Set back to the default thickness 1
    t.up()



# Draw the sun with beams
draw_circle(pen_turtle, -200, 210, 40, "yellow")
draw_sun_beams(pen_turtle, -200, 210, "yellow", 75, 15)

# Draw 8 floating dandelion seeds
random.seed(0)
for _ in range(8): 
    x = random.randint(-200, 200)
    y = random.randint(-200, 50)
    stem_angle = random.randint(90, 180)
    draw_dandelion_seed(pen_turtle, x, y, 20, stem_angle)

screen.exitonclick()
