import pandas as pd
import os

def load_ufc_data(folder="ufc_stats"):
    # Initialize an empty DataFrame
    all_data = pd.DataFrame()

    # Loop through all CSV files in the folder
    for file in os.listdir(folder):
        if file.endswith("_top15.csv"):
            division = file.split("_")[0].capitalize()
            filepath = os.path.join(folder, file)
            data = pd.read_csv(filepath)
            data["Division"] = division  # Add division as a column
            all_data = pd.concat([all_data, data], ignore_index=True)

    return all_data