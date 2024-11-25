import os
import pandas as pd

def load_division_data(folder):
    """
    Load all division data from the specified folder.
    """
    division_files = [f for f in os.listdir(folder) if f.endswith('_top15.csv')]
    divisions = {}
    for file in division_files:
        division_name = file.split('_top15.csv')[0].capitalize()
        divisions[division_name] = pd.read_csv(os.path.join(folder, file))
    return divisions

def compare_fighters(division_data, fighter1, fighter2):
    """
    Compare two fighters based on their statistics and count advantages.
    """
    # Extract fighters' data
    f1_stats = division_data[division_data['Fighter Name'].str.lower() == fighter1.lower()]
    f2_stats = division_data[division_data['Fighter Name'].str.lower() == fighter2.lower()]

    if f1_stats.empty or f2_stats.empty:
        return None, f"One or both fighters not found in the division."

    f1_stats = f1_stats.iloc[0]
    f2_stats = f2_stats.iloc[0]

    # List of numerical columns to compare
    numeric_columns = [
        'Rank', 'Age', 'Reach (in)', 'SLpM', 'Str. Acc.', 'SApM',
        'Str. Def.', 'TD Avg.', 'TD Acc.', 'TD Def.', 'Sub. Avg.'
    ]

    advantages = {fighter1: 0, fighter2: 0}
    advantage_categories = {fighter1: [], fighter2: []}

    # Compare each metric
    for column in numeric_columns:
        if column in division_data.columns:
            f1_value = f1_stats[column]
            f2_value = f2_stats[column]

            # Ensure values are numerical
            try:
                f1_value = float(f1_value)
                f2_value = float(f2_value)
            except ValueError:
                continue

            # Handle specific cases: Rank (lower is better) and Age (younger is better)
            if column == 'Rank' or column == 'Age':
                if f1_value < f2_value:
                    advantages[fighter1] += 1
                    advantage_categories[fighter1].append(column)
                elif f2_value < f1_value:
                    advantages[fighter2] += 1
                    advantage_categories[fighter2].append(column)
            # For all other metrics, higher is better
            else:
                if f1_value > f2_value:
                    advantages[fighter1] += 1
                    advantage_categories[fighter1].append(column)
                elif f2_value > f1_value:
                    advantages[fighter2] += 1
                    advantage_categories[fighter2].append(column)

    # Predict the winner
    if advantages[fighter1] > advantages[fighter2]:
        winner = fighter1
    elif advantages[fighter2] > advantages[fighter1]:
        winner = fighter2
    else:
        winner = "Draw"

    # Create a detailed comparison for console output
    comparison = {
        column: (f1_stats[column], f2_stats[column])
        for column in numeric_columns if column in division_data.columns
    }

    return advantages, winner, comparison, advantage_categories

def main():
    folder = input("Enter the folder path containing division CSV files (e.g., ufc_stats): ").strip()

    if not os.path.exists(folder):
        print("Folder not found. Exiting.")
        return

    divisions = load_division_data(folder)
    division_name = input(f"Enter the division (available: {', '.join(divisions.keys())}): ").capitalize()

    if division_name not in divisions:
        print("Division not found. Exiting.")
        return

    division_data = divisions[division_name]

    fighter1 = input("Enter the first fighter's name: ").strip()
    fighter2 = input("Enter the second fighter's name: ").strip()

    result = compare_fighters(division_data, fighter1, fighter2)

    if result[0] is None:
        print(result[1])  # Error message
        return

    advantages, winner, comparison, advantage_categories = result

    # Print detailed comparison
    print("\nStatistical Comparison:")
    print(f"{'Metric':<15}{fighter1:<20}{fighter2:<20}{'Advantage':<10}")
    print("-" * 60)
    for metric, (f1_value, f2_value) in comparison.items():
        advantage = ""
        if metric in advantage_categories[fighter1]:
            advantage = fighter1
        elif metric in advantage_categories[fighter2]:
            advantage = fighter2
        print(f"{metric:<15}{str(f1_value):<20}{str(f2_value):<20}{advantage:<10}")

    # Print results
    print("\nComparison Results:")
    print(f"{fighter1} Advantages: {advantages[fighter1]}")
    print(f"{fighter2} Advantages: {advantages[fighter2]}")
    print(f"Advantage Categories for {fighter1}: {', '.join(advantage_categories[fighter1])}")
    print(f"Advantage Categories for {fighter2}: {', '.join(advantage_categories[fighter2])}")
    print(f"Predicted Winner: {winner}")

if __name__ == "__main__":
    main()
