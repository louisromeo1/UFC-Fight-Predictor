import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report


def preprocess_data(file_path):
    """
    Preprocess the data from the CSV file for modeling.
    """
    df = pd.read_csv(file_path)

    # Process percentage columns (convert to numeric)
    for col in ["Str. Acc.", "Str. Def.", "TD Acc.", "TD Def."]:
        df[col] = df[col].str.rstrip('%').astype(float) / 100.0

    # Define features and target
    features = [
        "Age", "Reach (in)", "SLpM", "Str. Acc.", "SApM",
        "Str. Def.", "TD Avg.", "TD Acc.", "TD Def.", "Sub. Avg."
    ]
    target = "Last Fight Result"

    # Map fight results to numerical values (Win = 1, Loss = 0)
    df[target] = df[target].apply(lambda x: 1 if x.startswith('W') else 0)

    # Return features (X) and target (y)
    X = df[features]
    y = df[target]

    return X, y, df


def train_models(X, y):
    """
    Train Random Forest and Gradient Boosting models.
    """
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Standardize features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train Random Forest
    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(X_train_scaled, y_train)
    rf_preds = rf_model.predict(X_test_scaled)

    # Train Gradient Boosting
    gb_model = GradientBoostingClassifier(random_state=42)
    gb_model.fit(X_train_scaled, y_train)
    gb_preds = gb_model.predict(X_test_scaled)

    # Evaluate both models
    print("\nRandom Forest Model Performance:")
    print(classification_report(y_test, rf_preds, target_names=["Loss", "Win"]))

    print("\nGradient Boosting Model Performance:")
    print(classification_report(y_test, gb_preds, target_names=["Loss", "Win"]))

    # Return trained models and scaler
    return rf_model, gb_model, scaler


def predict_matchup_with_models(df, rf_model, gb_model, scaler, fighter1, fighter2):
    """
    Predict a matchup using trained models.
    """
    features = [
        "Age", "Reach (in)", "SLpM", "Str. Acc.", "SApM",
        "Str. Def.", "TD Avg.", "TD Acc.", "TD Def.", "Sub. Avg."
    ]

    # Get data for the fighters
    fighter1_data = df[df['Fighter Name'].str.lower() == fighter1.lower()]
    fighter2_data = df[df['Fighter Name'].str.lower() == fighter2.lower()]

    if fighter1_data.empty or fighter2_data.empty:
        print(f"Error: One or both fighters not found in the division.")
        return

    # Prepare data for prediction
    fighter1_features = fighter1_data[features]
    fighter2_features = fighter2_data[features]

    # Standardize features
    fighter1_scaled = scaler.transform(fighter1_features)
    fighter2_scaled = scaler.transform(fighter2_features)

    # Calculate probabilities
    fighter1_rf_prob = rf_model.predict_proba(fighter1_scaled)[0][1]
    fighter2_rf_prob = rf_model.predict_proba(fighter2_scaled)[0][1]

    fighter1_gb_prob = gb_model.predict_proba(fighter1_scaled)[0][1]
    fighter2_gb_prob = gb_model.predict_proba(fighter2_scaled)[0][1]

    # Normalize and calculate percentages
    rf_total = fighter1_rf_prob + fighter2_rf_prob
    gb_total = fighter1_gb_prob + fighter2_gb_prob

    fighter1_rf_win = (fighter1_rf_prob / rf_total) * 100
    fighter2_rf_win = (fighter2_rf_prob / rf_total) * 100

    fighter1_gb_win = (fighter1_gb_prob / gb_total) * 100
    fighter2_gb_win = (fighter2_gb_prob / gb_total) * 100

    # Display results
    print("\nMatchup Prediction:")
    print(f"Using Random Forest:")
    print(f"  {fighter1}: {fighter1_rf_win:.2f}% chance of winning")
    print(f"  {fighter2}: {fighter2_rf_win:.2f}% chance of winning")
    print(f"\nUsing Gradient Boosting:")
    print(f"  {fighter1}: {fighter1_gb_win:.2f}% chance of winning")
    print(f"  {fighter2}: {fighter2_gb_win:.2f}% chance of winning")


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
    X, y, df = preprocess_data(file_path)

    # Train models
    rf_model, gb_model, scaler = train_models(X, y)

    # Predict a hypothetical fight between two fighters
    while True:
        print("\nEnter the names of two fighters for a hypothetical matchup (or type 'exit' to quit):")
        fighter1 = input("Fighter 1: ").strip()
        if fighter1.lower() == 'exit':
            break
        fighter2 = input("Fighter 2: ").strip()
        if fighter2.lower() == 'exit':
            break

        predict_matchup_with_models(df, rf_model, gb_model, scaler, fighter1, fighter2)


if __name__ == "__main__":
    main()
