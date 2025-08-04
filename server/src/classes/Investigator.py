import pandas as pd
class Investigator:

    # All functions modify the gson and add information to it and return the instance itself to allow threading.
    
    def __init__(self , df:pd.DataFrame):
        self.results = {}
        self.df = df
       
    # ----------------------------------------------------------------------
    def total_tweets(self):

        result = self.df["Biased"].value_counts()

        self.results["total_tweets"] = {}
        self.results["total_tweets"]["antisemitic"] = int(result[0])
        self.results["total_tweets"]["non_antisemitic"] = int(result[1])
        self.results["total_tweets"]["total"] = self.df.shape[0]
        self.results["total_tweets"]["unspecified"] = self.df.shape[0] - int(result[0]) - int(result[1])


        return self
    # ----------------------------------------------------------------------
    # Using a helper function to find the average for each table by adding a column named LEN
    def average_length(self):
        
        def get_average(df:pd.DataFrame):
            df["len"] = df["Text"].apply(lambda x : len(str(x).split()))
            return float(df["len"].mean())
        
        
        non_antisemitic = self.df[self.df["Biased"] == 0]
       
        antisemitic = self.df[self.df["Biased"] == 1]


        self.results["average_length"] = {}
        self.results["average_length"]["non_antisemitic"] = get_average(non_antisemitic)
        self.results["average_length"]["antisemitic"] = get_average(antisemitic)
        self.results["average_length"]["total"] = get_average(self.df)

        return self
    # ----------------------------------------------------------------------
    # Finding the words by concatenating them into one large array and turning it into a series of pandas
    def common_words(self):
        words = []
        for i in self.df["Text"].values:
            words += str(i).split()
        words = pd.Series(words).value_counts().head(10)
        
        self.results["common_words"] ={}
        self.results["common_words"]["total"] = [i for i in words.keys()]
        return self
    # ----------------------------------------------------------------------
    # Using a helper function to find the longest by a new column
    def longest_3_tweets(self):
 
        def get_3_longest(df:pd.DataFrame):
            df["len"] = df["Text"].apply(lambda x : len(str(x)))
            
            df = df.sort_values(by="len",ascending=False).head(3)
            
            return df["Text"].to_list()


        non_antisemitic = self.df[self.df["Biased"] == 0]
       
        antisemitic = self.df[self.df["Biased"] == 1]
       


        self.results["longest_3_tweets"] = {}
        self.results["longest_3_tweets"]["non_antisemitic"] = get_3_longest(non_antisemitic)
        self.results["longest_3_tweets"]["antisemitic"] = get_3_longest(antisemitic)

        return self
    # ----------------------------------------------------------------------
    # Using a helper function to find words with all capital letters, and a helper function that adds a column that counts those words
    def uppercase_words(self):
        def is_uppercase(word:str):
            for i in word:
                if not i.isupper():
                    return False
                
            return True

        def get_uppercase(df:pd.DataFrame):
            df["sum"] = df["Text"].apply(lambda x : len([word for word in str(x).split() if is_uppercase(word)]))
            return int(df["sum"].sum())
        
        non_antisemitic = self.df[self.df["Biased"] == 0]
       
        antisemitic = self.df[self.df["Biased"] == 1]

        self.results["uppercase_words"] = {}
        self.results["uppercase_words"]["non_antisemitic"] = get_uppercase(non_antisemitic)
        self.results["uppercase_words"]["antisemitic"] = get_uppercase(antisemitic)
        self.results["uppercase_words"]["total"] = get_uppercase(self.df)

        return self
    # ----------------------------------------------------------------------
    
    def get_results(self):
        return self.results

    
    







