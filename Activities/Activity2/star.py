import turtle

# Set up the screen and turtle cursor
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(3)  # Adjust drawing speed

# Dimensions of the star
line_length = 150

# A 5-pointed star requires 5 repeating lines
for _ in range(5):
    t.forward(line_length)
    t.right(144)  # The exact angle needed for a 5-point star

# Keep window open until you click on it
screen.exitonclick()
