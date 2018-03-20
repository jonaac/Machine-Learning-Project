# Environment Class
import numpy as np

class Environment:

	states = 0
	actions = 0
	transitions = None
	rewards = None
	prob_distribution = [1]

	def __init__(self,states,actions,transitions,rewards):
		self.states = states
		self.actions = actions
		self.transitions = transitions
		self.rewards = rewards
		for i in range(self.actions-1):
			self.prob_distribution.append((1.0-self.prob_distribution[0])/(actions-1))

	def reward(self,state,action):
		reward = self.rewards[state][action]
		return reward

	def transition(self,state_0,action):
		possible_states = []
		for i in range(self.actions):
			possible_states.append(int(self.transitions[state_0][(action+i)%(self.actions)]))
		state_1 = np.random.choice(possible_states,p=self.prob_distribution)
		for j in range(self.actions):
			if self.transitions[state_0][j] == state_1: 
				new_action = j
				break
		return state_1, new_action

	def deterministic_transition(self,state_0,action):
		stete_1 = self.transitions[state_0][action]
		return state_1, action

	def exchange_start_goal(self,state_0,state_goal,unsafe_dictionary):
		for i in range(self.states):
		    for j in range(self.actions):
		        if str(self.transitions[i][j]) == str(state_0):
		            self.rewards[i][j] = 2
		        elif str(self.transitions[i][j]) == str(state_goal):
		        	self.rewards[i][j] = 0
