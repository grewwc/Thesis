import matplotlib.pyplot as plt


class Plot_Step:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_ylim(self, ylim):
        self.ylim = ylim

    def set_xlim(self, xlim):
        self.xlim = xlim

    def plot(self):
        plt.ylim(self.ylim)
        y_tick_pos = self.y[0]
        print(y_tick_pos)
        plt.yticks([y_tick_pos], ['$\\rho$'])
        plt.plot(self.x, self.y)


p1 = Plot_Step([0, 0.7], [0.2, 0.2])
p1.set_ylim([0, 1.5])
p1.set_xlim([0, 1])


p2 = Plot_Step([0.7, 1], [1.2, 1.2])
p2.set_xlim([0, 1.5])
p2.set_ylim([0, 1])



p1.plot()
p2.plot()
plt.show()