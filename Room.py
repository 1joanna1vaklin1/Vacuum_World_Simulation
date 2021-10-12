#Joanna Vaklin

class Room: 


    def __init__(self, state, dp, size, shape): # State = clean/dirty, dp = dirtplacement, size = size of room, shape = shape of room 
        self.state = state 
        self.dp = dp
        self.size = size
        self.shape = shape 
    
    def room_status(self):
        return self.state
    


    '''def room_directions(self, size, shape):
        if self.size == 'small':
            if(self.shape == 'square'):
                rules = ['left', 'right']
        elif self.size == 'large':
            if(self.shape == 'square'):
                rules = ['left', 'right', 'right', 'down'] 
        return rules '''

        




