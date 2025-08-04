from fastapi import FastAPI
import pandas as pd
from classes.Manager import Manager
import os

app = FastAPI()


PATH = "..//data//tweets_dataset.csv"
CSV_PATH = os.getenv("CSV_PATH" ,"..//results//cleaned_dataset_tweets.csv")
JSON_PATH = os.getenv("JSON_PATH" ,"..//results//results.json")

@app.get("/")
def home():
    return " עובד"

@app.get("/start")
def start():

    df = Manager.load(PATH)
    results = Manager.DataInvestigation(df)
    cleaned_dataset_tweets = Manager.DataCleaning(df) 

    Manager.SaveJson(results ,JSON_PATH)
    Manager.SaveToCsv(cleaned_dataset_tweets , CSV_PATH)

    return {"status": "Data saved successfully"}


    
    



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)