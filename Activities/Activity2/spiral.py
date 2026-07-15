import turtle

# Set up the screen and turtle cursor
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed

# Control variables
line_length = 5
angle = 90  # 90 for a square spiral, 89 or 91 for a twisted web spiral

# Draw 100 steps of the spiral
for _ in range(100):
    t.forward(line_length)
    t.right(angle)
    line_length += 4  # Grow the line slightly on each step

# Keep window open until you click on it
screen.exitonclick()
