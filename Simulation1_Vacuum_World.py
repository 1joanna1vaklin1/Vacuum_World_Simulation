#Joanna Vaklin

from Environment import Environment
from Room import Room
from Simple_Agent import agent

#Simulation that creates an enviorment of 2 rooms with specific dirt placement and an agent that cleans. 

def simulation(num_info, info, room_characteristics):
    environment = Environment(num_info[0], num_info[1], info, room_characteristics)
    count = 0 
    #loop that allows the agent to complete the SENSE, DECIDE, ACT, on a room. 
    #4 times 
    for x in range(0,4):
        status = environment.percept() 
        action = environment.agent.program(status)
        environment.update_env(action)
        count += environment.agent.steps_made
        print("+" + str(environment.agent.steps_made) + " steps made")
    print(" ")

    return(environment.agent.steps_made)
   

#this method simulates all possible combos of the 1 agent, 2 rooms configuration 
#Uses binary counting to create a pattern for each combo, (i.e: 001 = Agent is in Room A, A is Clean, B is Dirty)
def all_possible_combos_1a2R(num_info, room_characteristics):
    info = []
    binary_list = []
    num = 0 
    room = {'0': 'A',
            '1': 'B'}
    state = {'0': 'Clean', 
            '1': 'Dirty'}
    queue = []
    queue.append("1")
    s1 = queue[0]

    for x in range(0,8):
        if x == 0: 
            binary_list.append("000")
        else: 
            info = []
            s1 = queue[0]
            queue.pop(0) 
            s2 = s1
            if len(s1) < 3: 
                s = '0' * (3-len(s1))
                temp = s + s1 
                binary_list.append(temp)
            else: 
                binary_list.append(s1)

            queue.append(s1 + "0")
            queue.append(s2 + "1")
        info.append(room.get(binary_list[x][0]))
        info.append(state.get(binary_list[x][1]))
        info.append(state.get(binary_list[x][2]))
        print("Configuration: ", end=" ")
        print(info)
        
        num += simulation(num_info, info, room_characteristics)
    
    print("Average Score: " + str(num/8))
    

    

if __name__ == "__main__":
    num_info = [2, 1]
    room_characteristics = ['middle', 'small', 'square']
    all_possible_combos_1a2R(num_info, room_characteristics)
    




