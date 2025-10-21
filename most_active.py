import pandas as pd
from typing import List

def most_active(customers) -> List[str]:
    customers = customers.copy()

    # Find the maximum value of YearsActive
    max_years = customers["YearsActive"].max()

    # Select all customers with that maximum value
    most_active_customers = customers[customers["YearsActive"] == max_years]

    # Return their emails as a list of strings
    return list(most_active_customers["Email"])
