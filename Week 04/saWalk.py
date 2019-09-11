#

class SAWalker(object):
    def __init__(self, initial_x = 0, initial_y = 0, initial_z = 0, kind='2d'):
        """ Initialize self-avoiding random walker """
        
        # set initial / current position of walker (DEFAULT: origin)
        if kind == '2d': 
            self.current_position = [initial_x, initial_y]
        elif kind == '3d':
            self.current_position = [initial_x, initial_y, initial_z]  
        else:
            raise ValueError("Invalid Walker Kind")
        
        # initialize walker chain
        self.chain = [self.current_position]  # list of [x,y] coordinates
        self.monomer_type = ["blue"]
        
        # whether the walker can step in some direction
        self.is_stuck = False
        
        # initialize the chain energy
        self.energy = 0.0 
        
    def step(self):
        """ Take a random step on a fixed lattice """
        import numpy.random as nprand
        
        # seed our random number generator
        nprand.seed()
        
        # check whether the chain can move
        if self.stuck():
            return
        else:
            pass
        
        # make an X or Y step
        proposed_position = self.current_position
        while proposed_position in self.chain:
            # select x or y direction and step
            if nprand.random() < 0.5:
                dx = nprand.randint(-1, 2)
                dy = 0
            else:
                dx = 0
                dy = nprand.randint(-1, 2)
            proposed_position = [self.current_position[0] + dx, 
                                 self.current_position[1] + dy]
        # choose polar (r) vs nonpolar (b)
        if nprand.random() < 0.7:
            c = "blue"
        else:
            c = "red"
        self.chain.append(proposed_position)
        self.monomer_type.append(c)
        self.current_position = proposed_position
            
    def stuck(self):
        from numpy import array
        dx_p1 = [self.current_position[0] + 1, self.current_position[1]]
        dx_m1 = [self.current_position[0] - 1, self.current_position[1]]
        dy_p1 = [self.current_position[0],     self.current_position[1] + 1]
        dy_m1 = [self.current_position[0],     self.current_position[1] - 1]
        
        if (dx_p1 in self.chain) and (dx_m1 in self.chain) and (dy_p1 in self.chain) \
           and (dy_m1 in self.chain):
            self.is_stuck = True
            self.chain = array(self.chain)
        else:
            self.is_stuck = False
            
        return self.is_stuck
        
    def change_energy(self):
        """ """
