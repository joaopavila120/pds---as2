import pandas as pd
from go_sports import go_sports

def go_manager(teams, managers) -> str:
    
    sports = go_sports(teams, managers)

    # Keep only valid manager IDs
    sports = sports.dropna(subset=["managerID"])

    # Make sure wins is numeric (invalid becomes NaN, then 0)
    sports["W"] = pd.to_numeric(sports["W"], errors="coerce").fillna(0)

    # Sum wins over the manager's career
    wins_by_manager = sports.groupby("managerID")["W"].sum()

    # Get the manager with the highest total wins
    best_manager_id = wins_by_manager.idxmax()

    # Return as a string
    return str(best_manager_id)
