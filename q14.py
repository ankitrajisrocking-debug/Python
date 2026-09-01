import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([6, 17, 34, 57, 86, 121])

def poly(x, a, b, c,d):
    #return a*x**2 + b*x + c
    return a*x**3 + b*x**2 + c*x + d

p, _ = curve_fit(poly, x, y)

print("Coefficients:", p)
#print(f"Polynomial: y = {p[0]:.2f}x² + {p[1]:.2f}x + {p[2]:.2f}")
print(f"Polynomial: y = {p[0]:.2f}x^3 + {p[1]:.2f}x^2 + {p[2]:.2f} + {p[3]:.2f}")

plt.scatter(x, y, label="Data")
plt.plot(x, poly(x, *p), label="Fitted curve")
plt.xlabel("x"); plt.ylabel("y")
plt.legend(); plt.show()
