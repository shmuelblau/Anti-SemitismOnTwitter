import sys
from Manager import Manager


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
    results = Manager.DataExploration(df)
    cleaned_dataset_tweets = Manager.DataCleaning(df)

    Manager.SaveJson(results)
    Manager.SaveToCsv(cleaned_dataset_tweets)

    print("Data saved successfully")


if __name__ == "__main__":
    start()
