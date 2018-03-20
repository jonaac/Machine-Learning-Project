import numpy as np
from environment import Environment
from intelligent_agent import Agent

action_distribution = []

# Mix Exploitation and Exploration
def select_action(actions,state,q_matrix):
	action = np.random.randint(0,actions)
	return action

def sum_actions(env,action,q_matrix,gamma):
	for i in range(1,(n-1)/2):
		rest_q += q_matrix[state][(action+i)%n] + q_matrix[state][(action-i)%n]
	return (gamma * maxq + (1 - gamma) * rest_q)

def max_q(q_matrix,state):
	for i in range(0,len(q_matrix[state])):
		if i == 0:
			maxim = q_matrix[state][i]
		elif maxim < q_matrix[state][i]:
			maxim = q_matrix[state][i]
	return maxim

def q_learning(env,unsafe_dictionary,state_goal,gamma):
	q_matrix = np.zeros((env.states,env.actions))
	visited = np.zeros((env.states,env.actions))
	alpha = 1
	for i in range (150000):
		state = np.random.randint(0,env.states)
		while True:
			if (str(state) in unsafe_dictionary) or state == state_goal: break
			#if state == state_goal: break
			action = select_action(env.actions,state,q_matrix)
			new_state, n_a = env.transition(state,action)
			reward = env.reward(state,n_a)
			visited[state][action] += 1
			alpha = 1 / (1 + visited[state][action])
			q_matrix[state][action] = q_matrix[state][action] + alpha*(reward+gamma*max_q(q_matrix,new_state)-q_matrix[state][action])
			state = new_state
			if (str(state) in unsafe_dictionary) or state == state_goal: break
			#if state == state_goal: break
	return q_matrix