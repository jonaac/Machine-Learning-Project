# Requirements and Design for Reinforcement Learning and Safety test bed.

## 1. Introduction
We are looking to test and implement a strategy for safety in machine learning agents. In this project we will build a test bed in which an agent has to achieve some goal G. The implementation of the project will support a machine learning agent in the form of reinforcement learning that will evaluate its environment, and produce optimal strategies to achieve its goal state from any possible initial state in it’s environment. In order to test safety strategies for this agent we will introduce
danger situations into a non-deterministic environment and our algorithms/agent will have to work around these circumstances to obtain not only an optimal strategy but also a safe strategy. The project will be developed in Python.

## 2. Domain
The domain of this test bed will involve a planetary robot in a starting point (initial state sstart) that moves around in a grid world and who’s task is to reach a target destination (a goal state sgoal). Thegrid world will have craters in which the robot can fall (safety concern) and borders that limit theirmovement to a finite number of locations. The robot, or agent, will have the ability to observe thestate of its environment (s∈S), and a set of actions (a∈A) it can perform to alter this state. Also our environment will be non-deterministic, where an agent has 95% chance of performing the intended action and 5% chance of performing any other possible action. Here is a visual example of a grid world with a goal state (green square), crates (red squares) and and initial state (blue circle which is the robot):

The learning algorithm will not be limited to this domain. But for test purposes I will implement a reinforcement learning algorithm in the context of a grid world. The algorithm will be able to work on any circumstances as long as a set of states (including initial and goal state), actions, rewards and punishments are defined. I will be able to adapt the algorithm to any domain.

## 3. Architecture & Components of Test bed
The test bed will be divided in 3 main components, the environment, the intelligent agent and the q-learner. The environment will be a class that contains all the data necessary to describe and act on an environment, it includes a tuple of states, actions, a reward function and a transition function. The agent will be a class that contains all data necessary for an agent, it includes the specific environment the agent is acting upon, the current state of agent, a transition function, it’s agent function and a safety Boolean function.

### 3.1. Environment Specification

The environment will be specified as a class (i.e. environment.py) with the following components:
• States, 𝑆: set of states s.t every s ∈ 𝑆 is a possible state of the environment.
• Actions, 𝐴: set of actions s.t every a ∈ 𝐴 is an action that an agent can perform in this environment.
• Reward Function, 𝑟: 𝑆, 𝐴 → 𝑅 s.t for each pair of state/action inputs (𝑠, 𝑎) it will output the reward r ∈ ℝ an agent would obtain by taking an action 𝑎 from state 𝑠 in this environment.
• Transition Function, 𝑡𝑓: 𝑆, 𝐴 → 𝑆 s.t for each pair of state-action inputs (𝑠3, 𝑎) it will output a state 𝑠4 an agent would transition into if the agent would take action 𝑎 from state 𝑠3 (i.e. if agent is in 𝑠3 = [0,1], and I take action 𝑎 = 𝑈𝑃, then 𝑡𝑓(𝑠3, 𝑎) = 𝑠4 = [0,2]).

### 3.2. Intelligent Agent Specification
The intelligent agent will be specified as a class (i.e. i-agent.py) with the following components,
to build a complete agent one needs at least a specific environment it will run on and a matrix that
will represent the agent’s knowledge of the maximum potential reward for each possible stateaction
pair (in this case based on Q-learning):
• State, s: the current state the agent finds himself in. t
• Environment, environment class 𝑒, such that 𝑒 will be the specific environment the agent is acting on.
• Knowledge Base: matrix Q s.t. for each pair of state-actions, 𝑄[𝑠][𝑎] is equivalent to the 𝑄(𝑠, 𝑎) obtained from a Q-learning algorithm.
• Transition Function, 𝑡𝑓: 𝑆, 𝐴 → 𝑆 s.t for each pair of state-action inputs (𝑠3, 𝑎) it will output a new state 𝑠4 an agent would transition to if the agent would take action 𝑎 from state 𝑠3. (i.e. if agent is in 𝑠3 = [0,1], and I take action 𝑎 = 𝑈𝑃, then 𝑡𝑓(𝑠3, 𝑎) = 𝑠4 = [0,2])
• Agent Function, 𝑡𝑓: 𝑆 → 𝐴 s.t for each input state 𝑠, it will output the action 𝑎 that provides the maximum reward.
• Safety Boolean Function, 𝑠𝑏: 𝑆, 𝐴 → {𝑇𝑟𝑢𝑒, 𝐹𝑎𝑙𝑠𝑒} s.t. for each pair of state/action inputs (𝑠, 𝑎) it will output 𝑇𝑟𝑢𝑒 if the state obtained by applying 𝑎 to 𝑠 is safe and it will return 𝐹𝑎𝑙𝑠𝑒 if it is not safe.

### 3.3 PEAS
These are the specific settings our agent will be working in:
• Performance measure: Safety of agent and ability to reach a goal from an initial state sstart
• Environment: Grid world with an initial state, a goal state and craters.
• Actuators: move forwards, backwards, to the right and to the left.
• Sensors: Ability of agent to inspect its current state.
