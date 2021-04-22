# Safety for Intelligent Agents

This project is my introduction to RL and safe RL. I develop two grid-world simulation and RL algorithms from scratch, no ML or RL libraries, to experiment and test safety methods. After developing, training and deploying the agents I was able to achieve my goal. For every environment the agent was able to learn an optimal policy (shortest route) without falling into any crater.

<p align="center">
	<img width="250" src="https://jonaac.github.io/img/grid-1.jpg" />
	<img width="250" src="https://jonaac.github.io/img/mineral-2.jpg" />
</p>

## Getting Started

A list of all the prerequisites you'll need to run the experiments and the files the code will generate with the parameters to load the CNN and CNN+XGBoost models for each iteration.

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
