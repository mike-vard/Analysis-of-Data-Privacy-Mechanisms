import numpy as np
import matplotlib.pyplot as plt

loc, scale = 0., 1.
s = np.random.laplace(loc, scale, 1000)

count, bins, ignored = plt.hist(s, 30, normed=True)
x = np.arange(-8., 8., .01)
pdf = np.exp(-abs(x-loc)/scale)/(2.*scale)
plt.plot(x, pdf)
plt.show()
