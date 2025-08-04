# Anti-SemitismOnTwitter

A Python script designed to provide information for a file of tweets that includes a classification of whether the tweet is antisemitic or not.

## Project Structure

```
Data-cleaning-project-04-08-2025/

├── README.md                        
├── data/
│   └── tweets_dataset.csv          
├── results/
│   ├── results.json                
│   └── tweets_dataset_cleaned.csv  
└── src/
    ├── main.py                          
    └── classes/
        ├── manager.py              
        ├── cleaner.py           
        └── investigator.py           
       
### 🔹Results

Results are saved in a results folder in a CSV file that contains the relevant data, and in a JSON file that contains general data about the received file.

### 🔹Receiving the file

The data can be received as a path to a CSV file via a command line argument or as a default file that exists in the system if no path was entered when running the script.


##  Models 
- `Manager`
- `Claener`
- `Investigator`
`
