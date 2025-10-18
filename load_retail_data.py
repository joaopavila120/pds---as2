import pandas as pd

def load_retail_data(filepath: str) -> pd.DataFrame:
    """ Load retail data from a CSV file and returns it aas a pandas dataframe"""
    
    # Using 'latin1' encoding to avoide decoding error - the csv have special characters
    df = pd.read_csv(filepath, encoding="latin1")

    return df
