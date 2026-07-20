import turtle

# Set up canvas background and drawing speed
screen = turtle.Screen()
screen.bgcolor("black")
spi = turtle.Turtle()
spi.speed(0)  # 0 is the fastest speed

# List of colors for a rainbow effect
colors = ["red", "purple", "blue", "green", "orange", "yellow"]

# Loop to draw the expanding spiral
for x in range(360):
    spi.pencolor(colors[x % 6])  # Cycles through the 6 colors
    spi.width(x // 100 + 1)      # Gradually thickens the line
    spi.forward(x)               # Moves forward a tiny bit more each turn
    spi.left(59)                 # Change angle slightly under 60 for the twist

# Keep window open until clicked
screen.exitonclick()
