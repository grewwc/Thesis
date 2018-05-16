import matplotlib.pyplot as plt

plt.xscale('log')
plt.yscale('log')
# ax = plt.axes()
plt.arrow(1, 1, 5, 5, head_width=0.5, head_length=0.1, fc='k', ec='k')
plt.show()