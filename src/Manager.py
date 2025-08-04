import pandas as pd


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
    def DataExploration(df:pd.DataFrame):
        return
    
    @staticmethod
    def DataCleaning(df : pd.DataFrame ):
        return
    
    @staticmethod
    def SaveJson(data):
        return
    
    @ staticmethod
    def SaveToCsv(df):
        return
    