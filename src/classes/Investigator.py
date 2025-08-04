class Investigator:

    
    def __init__(self , df):
        self.results = {}
        self.df = df
       


    def total_tweets(self):
        self.results["total_tweets"] = "finish"
        return self

    def average_length(self):
        self.results["average_length"] = "finish"
        return self

    def common_words(self):
        self.results["common_words"] = "finish"
        return self

    def longest_3_tweets(self):
        self.results["longest_3_tweets"] = "finish"
        return self

    def uppercase_words(self):
        self.results["uppercase_words"] = "finish"
        return self
    
    def get_results(self):
        return self.results

    
    







