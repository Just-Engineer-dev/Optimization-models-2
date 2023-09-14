import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import linprog

x1 = np.linspace(0, 5, 100)

x2_1 = (8 - 4 * x1) / 2
x2_2 = (6 - x1) / 3
x2_3 = (4 - 4 * x1) / 3

c = [4, 3]

A = [
    [-4, -2],
    [-1, -3],
    [4, 3]
]

b = [-8, -6, 4]

x0_bounds = (0, None)
x1_bounds = (0, None)

plt.plot(x1, x2_1, label='4x1 + 2x2 ≤ 8')
plt.plot(x1, x2_2, label='x1 + 3x2 ≤ 6')
plt.plot(x1, x2_3, label='4x1 + 3x2 ≥ 4')

plt.fill_between(x1, 0, x2_1, where=(x2_1 >= 0), color='gray', alpha=0.5)
plt.fill_between(x1, 0, x2_2, where=(x2_2 >= 0), color='gray', alpha=0.5)
plt.fill_between(x1, 0, x2_3, where=(x2_3 >= 0), color='gray', alpha=0.5)

x2_level = (0 - 4 * x1) / 3


plt.xlim(0, 5)
plt.ylim(0, 5)
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()
plt.grid(True)

plt.show()

res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='simplex')

min_x1 = res.x[0]
min_x2 = res.x[1]
min_z = res.fun

print(f"Минимальное значение целевой функции: {min_z:.2f} при x1 = {min_x1:.2f}, x2 = {min_x2:.2f}")
