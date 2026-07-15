import turtle

# Setup screen and turtle object
screen = turtle.Screen()
t = turtle.Turtle()

# Define polygon properties
sides = int(input("Enter the number of sides: "))
side_length = 70
angle = 360 / sides  # Exterior angle formula

# Draw the polygon
for _ in range(sides):
    t.forward(side_length)
    t.right(angle)

# Keep the window open until clicked
screen.exitonclick()
