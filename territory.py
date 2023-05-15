from matplotlib import pyplot as plt

class Territory:
    def __init__(self):
        self.food_island = None
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(0, 1), 
                           ylim=(0, 1))