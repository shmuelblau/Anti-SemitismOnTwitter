import sys
import os
from classes.Manager import Manager

CSV_PATH = os.getenv("CSV_PATH" ,"..//results//cleaned_dataset_tweets.csv")
JSON_PATH = os.getenv("JSON_PATH" ,"..//results//results.json")

# Loading a file path or default path
if len(sys.argv) > 1:
    PATH = sys.argv[1]
else:
    PATH = "..//data//tweets_dataset.csv"




def start():

    

    # Checking if the path is valid
    if Manager.tryLoad == -1 :
        print ("problem in path")
        return 
    

    
    # Running the actions through the manager
    df = Manager.load(PATH)
    results = Manager.DataInvestigation(df)
    cleaned_dataset_tweets = Manager.DataCleaning(df) 

    Manager.SaveJson(results ,JSON_PATH)
    Manager.SaveToCsv(cleaned_dataset_tweets , CSV_PATH)

    print("Data saved successfully")


if __name__ == "__main__":
    start()
