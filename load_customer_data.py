import pandas as pd

def load_customer_data(filepath: str) -> pd.DataFrame:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(filepath)

    # Return the DataFrame
    return df
