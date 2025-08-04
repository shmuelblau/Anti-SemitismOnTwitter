import pandas as pd

class Cleaner:
    
    def __init__(self , df:pd.DataFrame) :
        self.df = df
    
    def RelevantColumns(self):
        return self
    
    def PunctuationCleaning(self):
        return self
    
    def ToLowercase(self):
        return self
    
    def DropUncategorized(self):
        return self


    def get_df(self):
        return self.df