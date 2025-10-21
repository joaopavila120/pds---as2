import pandas as pd

def load_retail_data(filepath: str) -> pd.DataFrame:
    # Your code goes here
    
    # Using 'latin1' encoding to avoide decoding error - the csv have special characters
    df = pd.read_csv(filepath, encoding="latin1")

    return df
