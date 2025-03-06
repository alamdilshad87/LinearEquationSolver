import numpy as np
import matplotlib.pyplot as plt

# Input coefficients for three equations
print("Enter the coefficients for the three equations (ax + by + cz = d):")
a1, b1, c1, d1 = map(float, input("Equation 1: ").split())
a2, b2, c2, d2 = map(float, input("Equation 2: ").split())
a3, b3, c3, d3 = map(float, input("Equation 3: ").split())

# Solving the linear equations
A = np.array([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])
B = np.array([d1, d2, d3])

try:
    solution = np.linalg.solve(A, B)
    print(f"Solution: x = {solution[0]}, y = {solution[1]}, z = {solution[2]}")
except np.linalg.LinAlgError:
    print("The system of equations has no unique solution.")

# 3D Graph plotting
x_vals = np.linspace(-10, 10, 10)
y_vals = np.linspace(-10, 10, 10)
X, Y = np.meshgrid(x_vals, y_vals)

Z1 = (d1 - a1 * X - b1 * Y) / c1
Z2 = (d2 - a2 * X - b2 * Y) / c2
Z3 = (d3 - a3 * X - b3 * Y) / c3

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z1, alpha=0.5, color='r')
ax.plot_surface(X, Y, Z2, alpha=0.5, color='g')
ax.plot_surface(X, Y, Z3, alpha=0.5, color='b')

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Graph of the Equations')

plt.show()
