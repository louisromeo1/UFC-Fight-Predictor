import pandas as pd
import os


def calculate_winning_chance(file_path):
    # Define weights for the metrics
    weights = {
        "Age": -0.1,  # Negative weight for age (younger fighters preferred)
        "Reach (in)": 0.2,
        "SLpM": 0.3,  # Strikes landed per minute
        "Str. Acc.": 0.2,  # Strike accuracy
        "SApM": -0.2,  # Strikes absorbed per minute (lower is better)
        "Str. Def.": 0.2,  # Strike defense
        "TD Avg.": 0.2,  # Takedown average
        "TD Acc.": 0.15,  # Takedown accuracy
        "TD Def.": 0.2,  # Takedown defense
        "Sub. Avg.": 0.1  # Submission average
    }

    # Load CSV file
    df = pd.read_csv(file_path)

    # Process percentage columns (convert to numeric)
    for col in ["Str. Acc.", "Str. Def.", "TD Acc.", "TD Def."]:
        df[col] = df[col].str.rstrip('%').astype(float) / 100.0

    # Initialize performance score
    df['Performance Score'] = (
            weights["Age"] * df["Age"] +
            weights["Reach (in)"] * df["Reach (in)"] +
            weights["SLpM"] * df["SLpM"] +
            weights["Str. Acc."] * df["Str. Acc."] +
            weights["SApM"] * df["SApM"] +
            weights["Str. Def."] * df["Str. Def."] +
            weights["TD Avg."] * df["TD Avg."] +
            weights["TD Acc."] * df["TD Acc."] +
            weights["TD Def."] * df["TD Def."] +
            weights["Sub. Avg."] * df["Sub. Avg."]
    )

    # Normalize scores to calculate winning chances
    max_score = df['Performance Score'].max()
    min_score = df['Performance Score'].min()
    df['Winning Chance (%)'] = ((df['Performance Score'] - min_score) / (
                max_score - min_score)) * 99 + 1  # Ensures no 0%

    # Sort by winning chance for display
    df = df.sort_values(by="Winning Chance (%)", ascending=False)

    print("\nDivision Analysis (Sorted by Winning Chance):")
    print(df[["Rank", "Fighter Name", "Winning Chance (%)"]])
    return df


def predict_matchup(df, fighter1, fighter2):
    # Get the performance scores for the two fighters
    fighter1_data = df[df['Fighter Name'].str.lower() == fighter1.lower()]
    fighter2_data = df[df['Fighter Name'].str.lower() == fighter2.lower()]

    if fighter1_data.empty or fighter2_data.empty:
        print(f"Error: One or both fighters not found in the division.")
        return

    fighter1_score = fighter1_data['Performance Score'].values[0]
    fighter2_score = fighter2_data['Performance Score'].values[0]

    # Calculate winning chances for each fighter
    total_score = fighter1_score + fighter2_score
    fighter1_chance = (fighter1_score / total_score) * 100
    fighter2_chance = (fighter2_score / total_score) * 100

    print(f"\nHypothetical Fight Prediction:")
    print(f"{fighter1}: {fighter1_chance:.2f}% chance of winning")
    print(f"{fighter2}: {fighter2_chance:.2f}% chance of winning")


def main():
    # List available files in the ufc_stats folder
    folder_path = "ufc_stats"
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    files = [f for f in os.listdir(folder_path) if f.endswith("_top15.csv")]
    if not files:
        print(f"No division files found in the '{folder_path}' folder.")
        return

    # Display available files
    print("Available divisions:")
    for i, file_name in enumerate(files):
        print(f"{i + 1}: {file_name}")

    # Ask user to select a division
    while True:
        try:
            choice = int(input("Enter the number of the division you want to analyze: "))
            if 1 <= choice <= len(files):
                selected_file = files[choice - 1]
                break
            else:
                print(f"Please select a number between 1 and {len(files)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Process the selected file
    file_path = os.path.join(folder_path, selected_file)
    print(f"\nAnalyzing {selected_file}...")
    df = calculate_winning_chance(file_path)

    # Predict a hypothetical fight between two fighters
    while True:
        print("\nEnter the names of two fighters for a hypothetical matchup (or type 'exit' to quit):")
        fighter1 = input("Fighter 1: ").strip()
        if fighter1.lower() == 'exit':
            break
        fighter2 = input("Fighter 2: ").strip()
        if fighter2.lower() == 'exit':
            break

        predict_matchup(df, fighter1, fighter2)


if __name__ == "__main__":
    main()
