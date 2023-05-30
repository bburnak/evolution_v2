import pandas as pd
import numpy as np
import random

class Life():
    def __init__(self, world_map, config):
        self.world_map = world_map
        self.config = config
        self.number_of_cells = self.config["cells"]["num_points"]
        self.data = pd.DataFrame({'x': np.random.rand(self.number_of_cells),
                                  'y': np.random.rand(self.number_of_cells),
                                  'prob_clone': np.random.uniform(0, 0.005, self.number_of_cells),
                                  'prob_move': np.random.uniform(0, 1, self.number_of_cells),
                                  'energy': 1,
                                  'will_die': False})
        

    def update(self):
        # initialization
        self.number_of_cells = len(self.data)
        self.data['delta_energy'] = 0
        self.data['will_die'] = False
         
        # move mechanics
        self.data['realization_move'] = np.random.uniform(0, 1, self.number_of_cells)
        self.data['is_moving'] = self.data['realization_move'] < self.data['prob_move']
        self.data['delta_x'] = np.random.normal(0, 0.001, self.number_of_cells)*self.data['is_moving'].astype(int)
        self.data['delta_y'] = np.random.normal(0, 0.001, self.number_of_cells)*self.data['is_moving'].astype(int)
        self.data['x'] += self.data['delta_x']
        self.data['y'] += self.data['delta_y']
        
        # clone
        self.data['realization_clone'] = np.random.uniform(0, 1, self.number_of_cells)
        self.data['is_cloning'] = self.data['realization_clone'] < self.data['prob_clone']
        self.data = pd.concat([self.data, self.data[self.data['is_cloning']]])
        
        # # change gene ### TODO: changing gene is problematic
        self.data['prob_clone'] = self.data['prob_clone']*(1 + np.random.normal(0, 0.05, self.number_of_cells)*self.data['is_cloning'])
        self.data['prob_move'] = self.data['prob_move']*(1 + np.random.normal(0, 0.05, self.number_of_cells)*self.data['is_cloning'])
                
        # grazing
        self.data['is_grazing'] = False
        for polygon in self.world_map.source_polygons:
            self.data['is_grazing'] = self.data['is_grazing'] | polygon.contains_points(self.data[['x', 'y']])
        
        # energy
        self.data['delta_energy'] -= np.sqrt(self.data['delta_x']**2+self.data['delta_y']**2) # energy loss due to movement
        self.data['delta_energy'] += 0.001*self.data['is_grazing'].astype(int) # energy gain due to grazing
        self.data['energy'] += self.data['delta_energy']
        self.data.loc[self.data['is_cloning'], 'energy'] = self.data.loc[self.data['is_cloning'], 'energy']/2 # halve the energy if cloning
        self.data['will_die'] = self.data['energy']<0
        
        # kill the weak
        self.data = self.data[~self.data['will_die']]
        