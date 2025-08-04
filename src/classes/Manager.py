import json
import pandas as pd
from classes.Investigator import Investigator
from classes.Cleaner import Cleaner
class Manager:

    @staticmethod
    def load(path):

        return pd.read_csv(path)
            
        
    @staticmethod
    def tryLoad(path):
        try:
            df = pd.read_csv(path)
            return 1
        except:
            return -1
        

    @staticmethod 
    def DataInvestigation(df:pd.DataFrame):
        results = Investigator(df).average_length().common_words().longest_3_tweets().total_tweets().uppercase_words().get_results()
       
        return results
    
    @staticmethod
    def DataCleaning(df : pd.DataFrame ):
        clean_df = Cleaner(df).PunctuationCleaning().ToLowercase().DropUncategorized().RelevantColumns().get_df()
        return clean_df
    
    @staticmethod
    def SaveJson(data , path):
        with open(path , "w") as f:
            json.dump(data, f)

        
    
    @ staticmethod
    def SaveToCsv(df:pd.DataFrame , path):
        df.to_csv(path)
    