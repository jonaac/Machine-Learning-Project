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

A list of all the prerequisites you'll need to run the experiments

### Prerequisites

```
Python
Keras
tensorflow
xgboost
sklearn
numpy
scipy
pickle
```

### Files Needed

## Running Experiments

For each iteration, I train the original CNN model, I used the train model to generate the CNN+XGBoost model and I compare the accoracy of each model. Download this repository and run the following code for each CNN+XGboost model:

### Baseline
```
cd code/baseline/
python3 cnn.py
python3 cnn_xgboost.py
python3 accuracy_baseline.py
```
### VGG16
```
cd code/vgg16/
python3 cnn_vgg16.py
python3 cnn_vgg16_xgboost.py
python3 acuoracy_vgg16.py
```


## Results


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
