import pandas as pd
from typing import Tuple

def read_sport_dfs(teams_filepath: str, managers_filepath: str) -> Tuple[pd.DataFrame]:
    # Load both CSV files into DataFrames
    teams = pd.read_csv(teams_filepath)
    managers = pd.read_csv(managers_filepath)

    # Return them as a tuple
    return teams, managers
