# Safety for Intelligent Agents

This project is my introduction to RL and safe RL. I develop two grid-world simulation and RL algorithms from scratch, no ML or RL libraries, to experiment and test safety methods. After developing, training and deploying the agents I was able to achieve my goal. For every environment the agent was able to learn an optimal policy (shortest route) without falling into any crater.

## Grid-World Environments

Both environments involve 5x4 grids limited by four borders. The agent will be able to move from one grid to another by performing 1 out of 4 possible actions (Up, Down, Left and Right). The first set of grid-world environments are Navigation simulations. It consists of a 'planetary robot' (blue) looking travel from a starting point (purple) to a specified target destination (green) while avoiding to fall into (red).

The second set of grid-world environments are Mineral Collection simulations. It consists of a planetary robot (blue) looking to collect mineral ore (yellow) and bringing it back to its starting position (purple) while avoiding to fall into craters (red). In the case of the Mineral Colection environment the agent will automatically pick up the ore when it reaches it's position.

<p align="center">
	<img width="250" src="https://jonaac.github.io/img/grid-1.jpg" />
	<img width="250" src="https://jonaac.github.io/img/mineral-2.jpg" />
</p>

## Getting Started

### Prerequisites
A list of all the prerequisites you'll need to run the experiments
```
Python
numpy
```

### Files Needed
Files that will be used to generate each environment.
```
/env/input.txt
/env/input-2.txt
/env/input-3.txt
```

## Running Experiments

For each environment run the following code to reproduce the experiment. It will load the .txt file used to generate the environment, run a Q-learning algorithm and deploy the trained agent in the environment.

### Navigation
```
python3 grid-world.py < input.txt
python3 grid-world.py < input-2.txt
python3 grid-world.py < input-3.txt
```
### Mineral Collection
```
python3 mineral-world.py < input.txt
python3 mineral-world.py < input-2.txt
python3 mineral-world.py < input-3.txt
```

## Results

### Navigation
```
NAVIGATION DOMAIN:
from (0,0) -> move DOWN to: (0,1)
from (0,1) -> move RIGHT to: (1,1)
from (1,1) -> move RIGHT to: (2,1)
from (2,1) -> move RIGHT to: (3,1)
from (3,1) -> move RIGHT to: (4,1)
from (4,1) -> move DOWN to: (4,2)
from (4,2) -> move DOWN to: (4,3)
from (4,3) -> move LEFT to: (3,3)
You have found the minerals!
CONGRATULATIONS!
SAFETY DATA: Your Rover has fallen 0
time/s.
```
<p align="center">
	<img width="250" src="https://jonaac.github.io/img/navigation.gif" />
</p>
### Mineral Collection
```
MINERAL COLLECTION DOMAIN
from (0,0) -> move DOWN to: (0,1)
from (0,1) -> move RIGHT to: (1,1)
from (1,1) -> move RIGHT to: (2,1)
from (2,1) -> move RIGHT to: (3,1)
from (3,1) -> move RIGHT to: (4,1)
from (4,1) -> move DOWN to: (4,2)
from (4,2) -> move DOWN to: (4,3)
from (4,3) -> move LEFT to: (3,3)
You have found the minerals!
CONGRATULATIONS!
from (3,3) -> move RIGHT to: (4,3)
from (4,3) -> move UP to: (4,2)
from (4,2) -> move UP to: (4,1)
from (4,1) -> move LEFT to: (3,1)
from (3,1) -> move LEFT to: (2,1)
from (2,1) -> move LEFT to: (1,1)
from (1,1) -> move LEFT to: (0,1)
from (0,1) -> move UP to: (0,0)
You are back in BASE with the MINERALS,
CONGRATULATIONS!
SAFETY DATA: Your Rover has fallen 0 time/s.
```
<p align="center">
	<img width="250" src="https://jonaac.github.io/img/mineral.gif" />
</p>

## Files
```
code ---|- baseline --|-- cnn.py
	|    	      |-- cnn_xgboost.py
	|    	      |-- accuracy_baseline.py
	|
	|- resnet ----|-- cnn_resnet.py
	|    	      |-- cnn_resnet_xgboost.py
	|    	      |-- accuracy_resnet.py
	|
	|- vgg16 -----|-- cnn_vgg.py
	     	      |-- cnn_vgg_xgboots.py
	     	      |-- accuracy_vgg16.py
```
