# Intelligent Agent Class
from environment import Environment

class Agent:

	current_state = None
	env = None
	knowledge_b = None

	def __init__(self,state,env,k_base):
		self.current_state = state
		self.env = env
		self.knowledge_b = k_base

	def transition_function(self,action):
		next_state = self.env.transitions[self.current_state][action]
		return next_state

	def agent_function(self,ID):
		action = 0
		for i in range(0,self.env.actions):
			if i == 0: 
				maxim = self.knowledge_b[ID][self.current_state][i]
			elif maxim < self.knowledge_b[ID][self.current_state][i]:
				maxim = self.knowledge_b[ID][self.current_state][i]
				action = i
		return action

	def update_current_state(self,state):
		self.current_state = state

	def safety_boolean(self,action):
		if self.env.reward(self.current_state,action) < 0: return True
		else: return False

	def maximum_reward(self,state,q_i):
		max_reward = -100
		for i in range(self.env.actions): 
			reward = self.knowledge_b[q_i][state][i]
			if max_reward < reward: 
				max_reward = reward
		return max_reward

	def select_next_best_action(self,state,q_i):
		max_reward = -100
		for i in range(self.env.actions):
			if self.env.rewards[state][i] == 0: 
				reward = self.maximum_reward(self.env.transitions[state][i],q_i)
				if max_reward < reward: 
					max_action = i
					max_reward = reward
			if self.env.rewards[state][i] > 0: max_action = i
		return max_action



