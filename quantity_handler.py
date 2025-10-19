import pandas as pd

def quantity_handler(df) -> pd.DataFrame:

    df = df.copy()

    df[df["Quantity"] > 0]

    return df
