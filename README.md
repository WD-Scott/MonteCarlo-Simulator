# Monte Carlo Package:

## Metadata:
Wyatt Scott's Final Project (Monte Carlo Simulator)


## Synopsis:
...

### Installing:
``!pip install .``
### Importing: 
``from montecarlo import Die, Game, Analyzer``

### Creating dice:
- Object:
- Change Weight:
- Roll:

### Playing games:
- Begin Game:
- Play:
- Show Results:

### Analyzing games:
- Start Analyzer:
- Face Counts per Roll:
- Jackpot:
- Combo:

### Classes and attributes:

### Die Class:
A die class with N sides/faces and W weights that can be rolled to select a side/face.
#### Attributes:
None
#### Methods:
##### ``__init__``:
Initializer that takes an array or list of faces of any length, initializes weights to 1, then saves to a private dataframe.
###### Parameters:
- faces
##### ``weight_change``:
A method that changes a side/face weight and checks whether side/face and weight are valid.
###### Parameters:
- face
- weight_changed
##### ``rolls``:
A method that rolls the die one or more times but defaults to 1. Returns a list of outcomes.
###### Parameters:
- rolls
##### ``show_faces_weights``:
A method that shows the dataframe of faces and weights.
###### Parameters:
- None

### Game Class:

#### Attributes:

#### Methods:

### Analyzer Class:

#### Attributes:

#### Methods:

## Manifest:

### Files in repo:
- montecarlo_demo.ipynb
- montecarlo_test.py
- montecarlo.py
- setup.py
- 
