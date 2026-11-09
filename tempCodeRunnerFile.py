import numpy as np
import matplotlib.pyplot as plt

Tb = 0.1
fs = 2000
f1, f2 = 30, 10

bits = np.random.randint(0, 2, 8)
N = int(Tb * fs)
t = np.arange(0, len(bits) * Tb, 1/fs)

data = np.repeat(bits, N)

plt.figure(figsize=(10, 3))
plt.plot(t, data, drawstyle='steps-pre')
plt.title("Binary Data")
plt.ylim(-0.2, 1.2)
plt.grid()
plt.show()

fsk = np.zeros(len(t))

for i, bit in enumerate(bits):
    f = f1 if bit == 1 else f2
    tb = np.arange(0, Tb, 1/fs)
    fsk[i*N:(i+1)*N] = np.sin(2*np.pi*f*tb)

plt.figure(figsize=(10, 3))
plt.plot(t, fsk)
plt.title("FSK Signal")
plt.grid()
plt.show()

recovered = []

for i in range(8):
    x = fsk[i*N:(i+1)*N]
    zc = np.sum(x[:-1] * x[1:] < 0)
    recovered.append(1 if zc > 4 else 0)

print("Transmitted:", bits)
print("Recovered:  ", recovered)
print("Match:", np.array_equal(bits, recovered))