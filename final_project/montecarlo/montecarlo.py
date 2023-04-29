import pandas as pd
import numpy as np
import re
import requests
from lxml import etree
import random

#-------------------------------------------------------------------------------------------------------------------------

class Die:
    '''
    A die class with N sides/faces and W weights that users can roll to select a side/face.
    
    
    Attributes:
    -----------
    None
    
    
    Methods:
    -----------
    - initializer
    - change_weight
    - rolls
    - show_die
    '''
    
    def __init__(self, faces):
        '''
        Initializer that takes an array or list of faces of any length, then initializes weights to 1 and saves to a private dataframe.
        
        
        Parameters:
        -----------
        - faces: numpy array or a list
        '''
        self.faces = np.array(faces)
        self._faces_weights = pd.DataFrame(data = faces, columns = ['Faces'], index = range(len(faces)))
        self._faces_weights['Weights'] = np.array([1.0 for i in range(len(faces))])
        
    def change_weight(self, face, new_weight):
        '''
        A method that changes a side/face weight and checks whether side/face and weight are valid.
        
        
        Parameters:
        -----------
        - face: str or int
        - new_weight: float
        
        Raises:
        -----------
        ValueError if new_weight is not a float or convertible to a float. 
        This error will also appear if face is not included in the die.
        '''
        if not (face in list(self._faces_weights['Faces'])):
            return ValueError ("That face does not exist.")
        else:
            self._faces_weights.loc[self._faces_weights['Faces'] == face, 'Weights'] = float(new_weight)
            
    def rolls(self, rolls=1):
        '''
        A method that rolls the die one or more times but defaults to 1.
        
        
        Parameters:
        -----------
        - rolls
        
        Returns:
        -----------
        rolled_outcome: a list of the rolled outcomes.
        '''
        rolled_outcome = self._faces_weights.sample(n = rolls, weights = 'Weights', replace = True)
        return list(rolled_outcome['Faces'])
    
    def show_die(self):
        '''
        A method that shows the dataframe of faces and weights.
        
        Parameters:
        -----------
        - None
        
        Returns:
        -----------
        A pandas df of faces and weights of the die.
        '''
        return self._faces_weights
    
#-------------------------------------------------------------------------------------------------------------------------

class Game:
    '''
    A game class that rolls one or more dice of the same kind one or more times.
    
    
    Attributes:
    -----------
    None
    
    
    Methods:
    -----------
    - initializer
    - play
    - show_play
    '''
    
    def __init__(self, die_list):
        '''
        Initializer that takes a single parameter — a list of already instantiated similar Die objects.
        
        Parameters:
        -----------
        - die_list: list
        '''
        self.die_list = die_list
        
    def play(self, rolls):
        '''
        A method that takes a parameter to specify how many times the dice should be rolled.
 
 
        Parameters:
        -----------
        - rolls: int
        '''
        self._played = pd.DataFrame()
        self.rolls = rolls
        Rando_Dice = 0
        
        for die in self.die_list:
            dice_results = die.rolls(rolls=rolls)
            Rando_Dice += 1
            series = pd.Series(dice_results, name = f'Die{Rando_Dice}')
            self._played = pd.concat([self._played, series], axis = 1)
        
        self._played['Roll'] = self._played.index + 1
        self._played = self._played.set_index('Roll')
    
    def show_play(self, form = 'wide'):
        '''
        A method that shows the user the results of the most recent play.
        Takes a parameter to return the dataframe in narrow or wide form.
        This parameter defaults to wide form.
        This parameter raises an exception if the user passes an invalid option.
        
        The narrow form of the dataframe will have a two-column index with:
            * the roll number
            * the die number
            * a column for the face rolled
        
        The wide form of the dataframe will be a single-column index with:
            * the roll number
            * each die number as a column
        
        
        Parameters:
        -----------
        - form: string
        
        Raises:
        -----------
        ValueError if form is not narrow or wide.
        
        Returns:
        -----------
        A pandas df with the most recent result from the play method, including:
            * the roll number
            * the die number
            * the face rolled for each respective roll
        '''
        self.form = form
        if not (form == 'wide' or form == 'narrow'):
            raise ValueError("Input must be wide or narrow") 
        elif form == 'wide':
            return self._played
        elif form == 'narrow':
            return self._played.stack().to_frame('Face')

#-------------------------------------------------------------------------------------------------------------------------

class Analyzer:
    '''
    An analyzer class that takes the results of a single game and computes various descriptive statistical properties about it. 
    These properties and results are available as attributes of an Analyzer object.
    
    
    Attributes:
    -----------
    None
    
    
    Methods:
    -----------
    - initializer
    - face_count
    - jackpot
    - combo
    '''
    
    def __init__(self, game):
        '''
        Initializer that takes a game object as its input parameter.
        At initialization time, it also infers the data type of the die faces.
        
        Parameters:
        -----------
        - game: Game object.
        '''
        self._game_ = game
        self.die_dtype = type(game.die_list[0])
        self.JPs = 0
        self.counts_df = pd.DataFrame()
    
    def face_count(self):
        '''
        A method that computes how many times a given face is rolled in each event.
        Stores the results as a dataframe in a public attribute.
        The dataframe has an index of the roll number and face values as columns (i.e., in wide form).
        
        Parameters:
        -----------
        - None
        
        Returns:
        -----------
        A pandas df with the counts of each face value per roll, including:
            * Indexes for the roll number
            * Columns showing die face values 
        '''
        self.face_count = self._game_.show_play().apply(lambda x: x.value_counts(), axis = 1).fillna(int(0))
        self.counts_df = self.face_count
        self.counts_df.index.name = 'Roll'
        self.counts_df.columns.name = "Die Face"
        return self.counts_df
    
    def jackpot(self):
        '''
        A method that computes how many times the game resulted in all faces being identical 
            and returns an integer for the number of times to the user.
        Stores the results as a dataframe of jackpot results in a public attribute.

        Parameters:
        -----------
        - None
        
        Returns:
        -----------
        A pandas df with the rows for when a jackpot occurred, including:
            * the roll number
            * the die number
            * the respective face rolled
        '''
        self.JPs_df = pd.DataFrame()
        for i in range(1, self._game_.show_play().T.shape[1]+1):
            if ((len(set(self._game_.show_play().loc[[i]].values[0].flatten())))==1):
                temp = self._game_.show_play().loc[[i]]
                self.JPs_df = pd.concat([self.JPs_df, temp], axis=0)
        self.JPs = self.JPs_df.shape[0]
        return self.JPs
    
    def combo(self):
        '''
        A method that computes the distinct combinations of faces rolled and their counts.
        Combinations are sorted and saved as a multicolumned index.
        Stores the results as a dataframe in a public attribute.
        
        
        Parameters:
        -----------
        - None
        
        Returns:
        -----------
        A pandas df where the face values are multi-indexes and columns show the combination count.
        '''
        self.combo_df = pd.DataFrame()
        self.combo = self._game_._played.apply(lambda x: pd.Series(sorted(x)), 1).value_counts().to_frame('Count')
        self.combo_df = self.combo.sort_values(by='Count',ascending=False)
        self.combo_df.index.names = ["Face"+str(i) for i in range(1, len(self._game_.die_list)+1)]
        return(self.combo_df)