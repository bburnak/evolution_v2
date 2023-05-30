import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.animation as animation
from territory import Territory
from cells import Life
import json
import os


# get config options
with open(os.path.join(os.getcwd(),"input","config.json")) as config_file:
    config = json.load(config_file)


# Create scatter plot
world_map = Territory(config)
    
# Create Life
life = Life(world_map, config)

def update(frame):
    # with pd.option_context('display.max_rows', None,
    #                         'display.max_columns', None,
    #                         'display.precision', 3):
    #     print(life.data)

    
    # Perturb the data points
    life.update()
    observed_columns = ['x', 'y', 'is_moving', 'delta_x', 'prob_move']
    print(life.data[observed_columns])

    # Update scatter plot data
    world_map.scatter.set_offsets(life.data[['x', 'y']])

    return world_map.scatter,

# Create animation
ani = animation.FuncAnimation(world_map.fig, update, frames=range(100), interval=10, blit=True)

# Display the plot
plt.show()