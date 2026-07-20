import turtle

# 1. Initialize canvas and settings
screen = turtle.Screen()
screen.bgcolor("black")  # Black background makes colors pop
screen.title("Rainbow Web Spiral")

spi = turtle.Turtle()
spi.speed(0)             # Set drawing speed to maximum

# 2. Define a rich color palette
colors = ["#FF1493", "#00FFFF", "#00FF00", "#FFD700", "#FF4500", "#9400D3"]

# 3. Draw the expanding spiral
for x in range(360):
    spi.pencolor(colors[x % 6])  # Cycle cleanly through the 6 colors
    spi.width(x // 100 + 1)      # Gradually thicken lines as it grows
    spi.forward(x)               # Move further out each turn
    spi.left(59)                 # Dynamic angle for a twisted web effect

# Close canvas cleanly on user click
screen.exitonclick()
