#Joanna Vaklin

class agent:
    
    def __init__ (self, steps_made, location): 
        self.steps_made = steps_made
        self.location = location
    
    #rules for the 2 room, 1 agent environment
    def rules(self, percept):
        action_rules = {'A Clean': 'Right',
            'A Dirty' : 'Suck', 
            'B Clean' : 'Left',
            'B Dirty' : 'Suck'}
        rule = action_rules.get(percept)
        return rule
    
    #Called by the program method. It does an action and records steps.
    #If the agent moves it only gets 1 point. If the agents sucks it gets 10 points. 
    def action(self, rule): 
        if rule == 'Right':
            self.steps_made += 1 
        elif rule == 'Left':
            self.steps_made += 1
        else: 
            self.steps_made += 10 

    #Method to find the decision of a perception. Returns what rule was completed in the action 
    def program(self, percept):
        rule = ''
        rule = self.rules(percept)
        self.action(rule)
        return rule


    
    



