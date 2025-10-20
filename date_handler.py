import pandas as pd

def date_handler(df) -> pd.DataFrame:
    df = df.copy()

    # Ensure 'InvoiceDate' is datetime
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    df = df[df['InvoiceDate'].dt.year != 2011]

    return df
