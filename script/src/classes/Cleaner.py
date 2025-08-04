import pandas as pd

class Cleaner:
    # The functions modify self.df and return the instance itself to allow function chaining.

    def __init__(self , df:pd.DataFrame) :
        self.df = df
    
    # ----------------------------------------------------------------------
    
    def RelevantColumns(self):

        self.df = self.df[["Text","Biased"]]
        return self
    
    # ----------------------------------------------------------------------
    # Using a helper function to delete characters that are not letters, numbers, or spaces
    def PunctuationCleaning(self):
        def removePunctuation(str):
            return "".join(filter(lambda x: x.isalnum() or x == " ",str))

        self.df["Text"] = self.df["Text"].apply(lambda x :removePunctuation(x))
        return self
    
    # ----------------------------------------------------------------------
    def ToLowercase(self):
        
        self.df["Text"] = self.df["Text"].apply(lambda x : x.lower())
        return self
    # ----------------------------------------------------------------------
    
    def DropUncategorized(self):
        mask = self.df["Biased"].isin([0,1])
        self.df = self.df[mask]
        return self

    # ----------------------------------------------------------------------

    def get_df(self):
        return self.df