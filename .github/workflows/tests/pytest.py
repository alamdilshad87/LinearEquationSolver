import numpy as np
from linear_solver import solve_equations  # Import your function

def test_solver():
    A = np.array([[2, 3, 4], [1, -2, 3], [3, 1, -1]])
    B = np.array([10, 5, 2])
    solution = solve_equations(A, B)  # This should be your solver function
    assert len(solution) == 3  # Ensure it returns three values
