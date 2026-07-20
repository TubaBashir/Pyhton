import turtle

# Set up the screen and turtle speed
screen = turtle.Screen()
star = turtle.Turtle()
star.speed(3)

# Draw a 5-point star
for _ in range(5):
    star.forward(150)  # Length of the star line
    star.right(144)    # The precise angle required for a 5-point star

# Keep the window open until clicked
screen.exitonclick()
