from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.path import Path
import numpy as np
import random
from scipy.spatial import ConvexHull

class Territory:
    def __init__(self, config):
        self.config = config
        self.food_island = None
        self.fig = plt.figure(figsize=(config["mapping"]["size"]["height"],
                                       config["mapping"]["size"]["width"]))
        self.ax = plt.axes(xlim=(0, 1), 
                           ylim=(0, 1))
        self.scatter = self.ax.scatter(random.random(), 
                                       random.random(), alpha=0.8)
        self.source_polygons = []
        for i in range(self.config["mapping"]["number_of_pastures"]):
            source_coordinates = generate_valley()
            source_polygon = Path(source_coordinates)
            self.source_polygons.append(source_polygon)
            energy_source_mapped = Polygon(source_coordinates, 
                                           color='g', alpha = 0.1)
            self.ax.add_patch(energy_source_mapped)

def generate_valley():
    scale = np.random.random()
    points = np.random.rand(60,2)*scale
    hull = ConvexHull(points)
    x,y = points[hull.vertices,0], points[hull.vertices,1]
    x += np.random.random()
    y += np.random.random()
    xy = np.vstack([x,y]).T
    return xy