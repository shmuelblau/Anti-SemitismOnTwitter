import pandas as pd

class Cleaner:
    
    def __init__(self , df:pd.DataFrame) :
        self.df = df
    

    # ----------------------------------------------------------------------
    def RelevantColumns(self):

        self.df = self.df[["Text","Biased"]]
        return self
    # ----------------------------------------------------------------------
    
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