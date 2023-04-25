# Monte Carlo Package:

## Metadata:
Final Project (Monte Carlo Simulator)

## Synopsis:
.is-live-preview hr {
  border-color: #FFFFFF !important;
}
The **``Monte Carlo Package``** is a python package with three classes: ``Die``, ``Game``, and ``Analyzer``. Class descriptions and demonstration code are included below to demo how to install and import the package and how to use the three classes.

## Classes and attributes:
- - - -
### Die Class:
A die class with N sides/faces and W weights that can be rolled to select a side/face.
#### Attributes:
- None
#### Methods:
##### ``__init__(self, faces)``:
Initializer that takes an array or list of ``faces`` of any length, initializes weights to 1, then saves to a private dataframe.
###### Parameters:
- ``faces``: numpy array or a list
##### ``change_weight(self, face, new_weight)``:
A method that changes a side/face weight and checks whether side/face and weight are valid.
###### Parameters:
- ``face``: str or int
- ``new_weight``: float
###### Raises:
- ``ValueError`` if ``new_weigh`` is not a float or convertible to a float. This error will also appear if ``face`` is not included in the die.
##### ``rolls(self, rolls=1)``:
A method that rolls the die one or more times but defaults to 1.
###### Parameters:
- ``rolls``: int
###### Returns:
- ``rolled_outcome``: a list of the rolled outcomes.
##### ``show_die(self)``:
A method that shows the dataframe of faces and weights.
###### Parameters:
- None
###### Returns:
- a pandas df of faces and weights of the die.

- - - -

### Game Class:
A game class that consists of rolling of one or more dice of the same kind one or more times.
#### Attributes:
- None
#### Methods:
##### ``__init__(self, die_list)``:
Initializer that takes a single parameter — a list of already instantiated similar Die objects.
###### Parameters:
- ``die_list``: list
##### ``play(self, rolls)``:
A method that takes a parameter to specify how many times the dice should be rolled. Saves the result of the play to a private dataframe of shape N rolls by M dice. Results in a table of data with columns for: 
- roll number
- the die number (its list index)
- the face rolled in that instance
###### Parameters:
- ``rolls``: int
##### ``show_play(self, form = 'wide')``:
A method that shows the user the results of the most recent play. Takes a parameter to return the dataframe in narrow or wide form. This parameter defaults to wide form. This parameter raises an exception if the user passes an invalid option. The narrow form of the dataframe will have a two column index with:
- the roll number
- the die number
- a column for the face rolled

The wide form of the dataframe will be a single column index with:
- the roll number
- each die number as a column
###### Parameters:
- ``form``: string
###### Raises:
- ``ValueError`` if ``form`` is not narrow or wide.
###### Returns:
A pandas df with the most recent result from ``play``, including:
- the die number 
- the rolle number
- the face rolled for each respective roll

- - - -

### Analyzer Class:
An analyzer class that takes the results of a single game and computes various descriptive statistical properties about it. These properties results are available as attributes of an Analyzer object.
#### Attributes:
- None
#### Methods:
##### ``__init__(self, game)``:
Initializer that takes a game object as its input parameter. At initialization time, it also infers the data type of the die faces used.
###### Parameters:
- ``game``: Game object.
##### ``face_count(self)``:
A method that computes how many times a given face is rolled in each event. Stores the results as a dataframe in a public attribute. The dataframe has an index of the roll number and face values as columns (i.e., in wide form).
###### Parameters:
- None
###### Returns:
A pandas df with the counts of each face value per roll. Includes indexes for the roll number and columns showing die face values.
##### ``jackpot(self)``:
A method that computes how many times the game resulted in all faces being identical. Returns an integer for the number times to the user. Stores the results as a dataframe of jackpot results in a public attribute.
###### Parameters:
- None
###### Returns:
A pandas df with the rows for when a jackpot occurred, including:
- the roll number
- the die number
- the respective face rolled
##### ``combo(self)``:
A method that computes the distinct combinations of faces rolled and their counts. Combinations are sorted and saved as a multicolumned index. Stores the results as a dataframe in a public attribute.
###### Parameters:
- None
###### Returns:
A pandas df with combinations where the face values are multi-indexes and columns show the combination count.

- - - -

## Installing:
```python
!pip install .
```
## Importing: 
```python
from montecarlo import Die, Game, Analyzer
```

## Creating dice:
- Create the die object called ``myDie``:

```python
myDie = Die(['face1', 'face2', 'face3'])
```

- Change the weight of ``'face1'``:

```python
myDie.change_weight('face1', 3)
```

- Show the faces and weights of ``myDie``:

```python
myDie.show_die()
```

- Roll ``myDie`` five times:

```python
myDie.rolls(5)
```

## Playing games:
- Create the game object ``myGame``:

```python
myGame = Game([Die([1,2,3]), Die([1,2,3]), Die([1,2,3])])
```

- Play the game using ``myGame``, input value in the ``rolls`` pararmeter to specify number of times each die is to be rolled:

```python
myGame.play(3)
```

- Show the results of ``play``, input either 'wide' or 'narrow' for the ``form`` parameter to specify the format of the df of results to be shown (defaults to wide).

```python
myGame.show_play()
```

## Analyzing games:
- Create the analyzer object ``myAnalyzer`` using ``myGame``:

```python
myAnalyzer = Analyzer(myGame)
```

- Return a df with counts for the occurrence of each face value per roll:

```python
myAnalyzer.face_count()
```

- Find out how many times a jackpot occurred:

 ```python
 myAnalyzer.jackpot()
 ```

- Find out the combintations of faces rolled and their counts:

```python
myAnalyzer.combo()
```

- - - -

## Manifest:

### Files in repo:
* final_project
    * montecarlo
        * init.py
        * montecarlo.py
        * pycache
          *  init.cpython-39.pyc
          *  montecarlo.cpython-39.pyc
   * montecarlo_demo.ipynb
   * montecarlo_tests.py
   * setup.py
   * test_results.txt
