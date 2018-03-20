from tkinter import *
from environment import Environment
from intelligent_agent import Agent
import Qlearning
import threading
import time
import numpy as np

master = Tk()

def render_grid():
    global specials, Width, x, y, player
    for i in range(x):
        for j in range(y):
            board.create_rectangle(i*Width, j*Width, (i+1)*Width, (j+1)*Width, fill="white", width=1)
    for (i, j, c, w) in specials:
        board.create_rectangle(i*Width, j*Width, (i+1)*Width, (j+1)*Width, fill=c, width=1)

def try_move(dx, dy, direction):
    global player, x, y, me, restart
    if restart == True:
        restart_game()
    else:
        new_x = player[0] + dx
        new_y = player[1] + dy
        print("from: (" + str(player[0]) + "," +str(player[1]) + ") -> move " + direction + " to: (" + str(new_x) + "," +str(new_y) + ")")
        if (new_x >= 0) and (new_x < x) and (new_y >= 0) and (new_y < y):
            board.coords(me, new_x*Width+Width*2/10, new_y*Width+Width*2/10, new_x*Width+Width*8/10, new_y*Width+Width*8/10)
            player = (new_x, new_y)
        for (i, j, c, w) in specials:
            if new_x == i and new_y == j and c == "green":
                print("\nYou have arrived to your destination, CONGRATULATIONS!\n")
                restart = True
                return
            elif new_x == i and new_y == j and c == "red":
                print("ATTN: Your Rover has FALLEN, CAREFUL!!")
                return

def call_up(event): try_move(0, -1,"Up")
def call_down(event): try_move(0, 1, "Down")
def call_left(event): try_move(-1, 0, "Left")
def call_right(event): try_move(1, 0, "Right")

def restart_game():
    global player, me, restart
    player = ((state_0%5), int(state_0/5))
    restart = False
    board.coords(me, player[0]*Width+Width*2/10, player[1]*Width+Width*2/10, player[0]*Width+Width*8/10, player[1]*Width+Width*8/10)

def has_restarted():
    return restart

def start_game():
    master.mainloop()

def do_action(action):
    if action == 0: try_move(0, -1,"Up")
    elif action == 2: try_move(0, 1, "Down")
    elif action == 3: try_move(-1, 0, "Left")
    elif action == 1: try_move(1, 0, "Right")
    else: return

def run():
    global discount
    time.sleep(1)
    t = 1
    safety_counter = 0
    for i in steps:
        new_action, next_action = i.split(",")
        if (next_action != new_action): 
            print("Something happened, your Rover wasn't able to go (" + str(actions[int(next_action)]) + "), instead your Rover went (" + str(actions[int(new_action)]) + ")")
        if (i_agent.safety_boolean(int(new_action))): safety_counter += 1
        i_agent.update_current_state(i_agent.transition_function(int(new_action)))
        do_action(int(new_action))
        # Check if the game has restarted
        t += 1.0
        if has_restarted():
            print("SAFETY DATA: Your Rover has fallen " + str(safety_counter) + " times.\n")
            time.sleep(1.5)
            restart_game()
            t = 1.0
        # MODIFY THIS SLEEP IF THE GAME IS GOING TOO FAST.
        time.sleep(0.5)

'''
This following section is the main() method:
1. The program will ask for all the input data.
2. Contruct Grid-World from data provided.
3. Construct the environment with the data provided.
4. Call the Q-learning class to build Q-matrix.
5. Construct agent with data provided and Q-matrix (Knowledge Base).
6. Build path (non-deterministic).
7. Showcase path on grid.
'''
''' ========================== 1. Input data requested ========================== '''
''' ---------------- 1.1. Initial State, Goal State, Reward State ---------------- '''
n = int(input("Enter # of states in your environment N: \n"))
m = int(input("Enter # of possible actions per state in your environment M: \n"))
state_0 = int(input("Enter Initial state: \n"))
state_goal = int(input("Enter Goal state: \n"))
unsafe_states = input("Enter states and their rewards (State,Reward): \n").split(" ")
unsafe_dictionary = dict(u.split(',') for u in unsafe_states)
for key in unsafe_dictionary: unsafe_dictionary[key] = int(unsafe_dictionary[key])
specials = []
for key in unsafe_dictionary: 
    i = int(key)%5
    j = int(int(key)/5)
    if unsafe_dictionary[key] < 0:
        c = "red"
        w = -1
    elif unsafe_dictionary[key] > 0:
        c = "green"
        w = 1
    specials.append((i,j,c,w))

''' ------------- 1.2. Transition Matrix and Contruct Reward Matrix  ------------- '''
transitions = np.zeros((n,m),int)   
rewards = np.zeros((n,m),int)
print("Enter transition matrix of size NxM:")
for i in range(n):
    aux = input().split(" ")
    for j in range (m):
        transitions[i][j] = int(aux[j])
print("Reward Matrix NxM built.")
for i in range(n):
    for j in range (m):
        if str(transitions[i][j]) in unsafe_dictionary:
            rewards[i][j] = unsafe_dictionary[str(transitions[i][j])]
        else: rewards[i][j] = 0


''' ================ 2. Contructing Grid World with data provided ================ '''
Width = 150
(x, y) = (5, 4)
actions = ["Up", "Right", "Down", "Left"]
board = Canvas(master, width=x*Width, height=y*Width)
player = ((state_0%5), int(state_0/5))
restart = False
render_grid()
master.bind("<Up>", call_up)
master.bind("<Down>", call_down)
master.bind("<Right>", call_right)
master.bind("<Left>", call_left)
me = board.create_rectangle(player[0]*Width+Width*2/10, player[1]*Width+Width*2/10,
                            player[0]*Width+Width*8/10, player[1]*Width+Width*8/10, fill="blue", width=1, tag="me")
board.grid(row=0, column=0)


''' ============== 3. Construct Environment with the data provided. ============== '''
env = Environment(n,m,transitions,rewards)


''' ============== 4. Call the Q-learning class to build Q-matrix.  ============== '''
print("Building Q-Matrix...")
q_matrix = []
q_1 = Qlearning.q_learning(env,unsafe_dictionary,state_goal,0.95)
q_matrix.append(q_1)


''' ==== 5. Construct agent with data provided and Q-matrix (Knowledge Base). ==== '''
i_agent = Agent(state_0,env,q_matrix)


''' ===================== 6. Build path (non-deterministic). ===================== '''
discount = 0.3
steps = []
actual_steps = []
while True:
    next_action = i_agent.agent_function(0)
    next_state, new_action = i_agent.env.transition(i_agent.current_state,next_action)
    steps.append(str(new_action)+","+str(next_action))
    if (i_agent.safety_boolean(int(new_action))):
        safety_action = i_agent.select_next_best_action(next_state,0)
        steps.append(str(safety_action)+","+str(safety_action))
        next_state = i_agent.env.transitions[next_state][safety_action]
    i_agent.update_current_state(next_state)
    if i_agent.current_state == state_goal: 
        i_agent.update_current_state(state_0)
        break
''' ========================= 7. Showcase path on grid.  ========================= '''
t = threading.Thread(target=run)
t.daemon = True
t.start()
start_game()

'''
END OF SIMULATION
'''
