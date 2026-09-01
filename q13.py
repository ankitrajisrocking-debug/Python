from scipy.optimize import approx_fprime
from scipy.integrate import quad

f = lambda x: x*3 + 2*x*2 + x
x, h = 2, 1e-6

d = (f(x+h) - f(x-h))/(2*h)
I, _ = quad(f, 0, 2)

print("Derivative:", d)
print("Integral:", I)
