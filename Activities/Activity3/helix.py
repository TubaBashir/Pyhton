import matplotlib.pyplot as plt
import numpy as np

# Create an empty 3D plotting canvas
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Generate data points for the helix
theta = np.linspace(-4 * np.pi, 4 * np.pi, 200) # Rotation angles
z = np.linspace(-2, 2, 200)                    # Height progression
r = z**2 + 1                                   # Expanding radius factor

x = r * np.sin(theta)
y = r * np.cos(theta)

# Plot the 3D line with a custom color map
ax.plot(x, y, z, label='3D Spiral Helix', color='crimson', linewidth=2)
ax.set_title("3D Spiral Helix Profile")
ax.legend()

plt.show()
