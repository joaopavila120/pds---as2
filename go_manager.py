import pandas as pd
from go_sports import go_sports

def go_manager(teams, managers) -> str:
    
    sports = go_sports(teams, managers)
    
    # Sum wins per manager over all seasons
    wins_per_manager = sports.groupby("managerID")["W"].sum()
    
    # Get the managerID with the highest total wins
    top_manager = wins_per_manager.idxmax()
    
    # Return as string (contract asks for correct string)
    return str(top_manager)
