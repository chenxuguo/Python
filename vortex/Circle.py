import numpy as np
import matplotlib.pyplot as plt

r = np.arange(0, 2*np.pi + np.pi/1000, np.pi/1000)

x = [5 * np.cos(i) for i in r]
y = [5 * np.sin(i) for i in r]

plt.plot(x, y)

# n = 240
n = 50   # modulus

# m = 7417
m = 4     # multiplier
nx, ny = [], []

dn = 2*np.pi/n

for i in range(n):
    nx.append(5 * np.cos(i*dn))
    ny.append(5 * np.sin(i*dn))

# plt.plot(nx, ny, 'ro')

for i in range(n):
    n1 = i
    n2 = (i*m) % n

    plt.plot([nx[n1], nx[n2]], [ny[n1], ny[n2]], c='r', lw=.1)

plt.show()
