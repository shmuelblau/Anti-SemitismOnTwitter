import sys
import os
from classes.Manager import Manager

CSV_PATH = os.getenv("CSV_PATH" ,"C://Users//user//Desktop//DATA//Projects//Anti-SemitismOnTwitter//results//cleaned_dataset_tweets.csv")
JSON_PATH = os.getenv("JSON_PATH" ,"C://Users//user//Desktop//DATA//Projects//Anti-SemitismOnTwitter//results//results.json")

def start():

    # Loading a file path or default path
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "..//data//tweets_dataset.csv"


    if Manager.tryLoad == -1 :
        print ("problem in path")
        return 
    

    df = Manager.load(path)
    results = Manager.DataInvestigation(df)
    cleaned_dataset_tweets = Manager.DataCleaning(df) 

    Manager.SaveJson(results ,JSON_PATH)
    Manager.SaveToCsv(cleaned_dataset_tweets , CSV_PATH)

    print("Data saved successfully")


if __name__ == "__main__":
    start()
