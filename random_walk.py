import numpy as np
import matplotlib.pyplot as plt

delta_X = np.random.normal(0, 1, (2, 10000))

# X_0 is an array that contains position 0,0
X_0 = np.array([[0], [0]])

# X is the position of the random walker at any given time (with start at 0,0)
X = np.concatenate((X_0, np.cumsum(delta_X, axis=1)), axis=1)

# to plot the random walk:
plt.plot(X[0], X[1], "ro-")
plt.show()