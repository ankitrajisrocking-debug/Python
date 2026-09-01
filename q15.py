from scipy.optimize import minimize

def f(v):
    x, y = v
    return (x - 2)**2 + (y - 2)**2

result = minimize(f, [0, 0])

print("Minimum point:", result.x)
print("Minimum value:", result.fun)


