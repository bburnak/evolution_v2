import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from territory import Territory
import json
import os

# with open(os.path.join(os.getcwd(),"input","config.json")) as config_file:
#     config = json.load(config_file)
w_map = Territory()
line, = w_map.ax.step([], [])

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(0, 2, 10)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

anim = animation.FuncAnimation(w_map.fig, animate, init_func=init,
                               frames=100, interval=20, blit=True)

plt.show()