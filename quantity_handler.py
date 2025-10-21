import pandas as pd

def quantity_handler(df) -> pd.DataFrame:
    
    df = df.copy()

    return df[df["Quantity"] > 0]
