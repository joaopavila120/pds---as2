import pandas as pd

def go_sports(teams, managers) -> pd.DataFrame:
    teams = teams.copy()
    managers = managers.copy()
    
    #(one is yyyy and the other is yyyy-mm-dd)
    teams["yearID"] = pd.to_datetime(teams["yearID"]).dt.year.astype("Int64")
    managers["yearID"] = managers["yearID"].astype("Int64")

    # Merge teams with main managers on teamID and yearID
    merged = pd.merge(
        teams[["teamID", "name", "yearID", "W", "L"]], #make sure W and L come from teams
        managers[["teamID", "yearID", "managerID"]],
        on=["teamID", "yearID"],
        how="inner"
    )

    # Keep only required columns
    return merged[["name", "managerID", "yearID", "W", "L"]]
