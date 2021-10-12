#Joanna Vaklin

from Room import Room
from Simple_Agent import agent



class Environment: 

    def __init__(self, num_of_rooms, num_of_agents, info, room_characteristics): 
        self.num_of_rooms = num_of_rooms
        self.num_of_agents = num_of_agents 
        self.rooms = self.create_rooms(info, room_characteristics)
        self.agent = self.create_agent(info)
        
    
    #the info is a String list that indicates the attributes of each room 
    def create_rooms(self,info,room_characteristics):
        num = self.num_of_rooms 
        rooms = [] 
        for x in range (1,num+1): 
            room1 = Room(info[x], room_characteristics[0], room_characteristics[1], room_characteristics[2])
            rooms.append(room1)
        return rooms

    def create_agent(self, info):
        location = info[0]
        agent1 = agent(0, location)
        return agent1

    #Returns a String that has a location of the agent and the whether the room is dirty or clean 
    def percept(self): 
        status = ''
        l = self.agent.location
        if(l == 'A'):
            status = self.rooms[0].room_status() 
        else:
            status = self.rooms[1].room_status()
        return l + " " + status

    #method that updates the enviornment when agent cleans or moves. 
    def update_env(self, action):
        if(action == "Right"):
            self.agent.location = 'B'
        elif(action == 'Left'):
            self.agent.location = 'A'
        elif(action == 'Suck' and self.agent.location == 'A'):
            self.rooms[0].state = 'Clean'
        elif(action == 'Suck' and self.agent.location == 'B'):
            self.rooms[1].state = 'Clean'

        print(self.rooms[0].state, self.rooms[1].state)



        


        
