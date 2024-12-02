import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns


def preprocess_data(file_path):
    """
    Preprocess the data from the CSV file for visualization.
    """
    df = pd.read_csv(file_path)

    # Process percentage columns (convert to numeric)
    for col in ["Str. Acc.", "Str. Def.", "TD Acc.", "TD Def."]:
        df[col] = df[col].str.rstrip('%').astype(float) / 100.0

    # Add a new column to map fight outcomes for correlation analysis
    df['Outcome'] = df['Last Fight Result'].apply(lambda x: 1 if x.startswith('W') else 0)

    return df


def create_charts(df, division_name):
    """
    Generate charts for important statistics and correlations.
    """
    output_folder = "charts"
    os.makedirs(output_folder, exist_ok=True)

    # Set style
    sns.set_theme(style="whitegrid")

    # 1. Histogram for Strike Accuracy
    plt.figure(figsize=(8, 6))
    sns.histplot(df["Str. Acc."], bins=10, kde=True, color="blue")
    plt.title(f"Strike Accuracy Distribution - {division_name}")
    plt.xlabel("Strike Accuracy")
    plt.ylabel("Frequency")
    plt.savefig(os.path.join(output_folder, f"{division_name}_strike_accuracy_histogram.png"))
    plt.close()

    # 2. Boxplot for Strikes Landed per Minute (SLpM)
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=df["SLpM"], color="green")
    plt.title(f"Strikes Landed Per Minute (SLpM) - {division_name}")
    plt.xlabel("SLpM")
    plt.savefig(os.path.join(output_folder, f"{division_name}_slpm_boxplot.png"))
    plt.close()

    # 3. Scatter plot: Strike Accuracy vs. Strike Defense with Fighter Names
    plt.figure(figsize=(10, 8))
    scatter = sns.scatterplot(
        data=df,
        x="Str. Acc.",
        y="Str. Def.",
        hue="Outcome",
        palette="coolwarm",
        s=100,
        legend='full'
    )
    plt.title(f"Strike Accuracy vs. Strike Defense - {division_name}")
    plt.xlabel("Strike Accuracy")
    plt.ylabel("Strike Defense")
    plt.legend(title="Outcome", loc="upper left", labels=["Loss", "Win"])

    # Add fighter names to the data points
    for i, point in df.iterrows():
        plt.text(
            point["Str. Acc."],
            point["Str. Def."],
            point["Fighter Name"],
            fontsize=9,
            ha='right',  # horizontal alignment can be adjusted
            va='bottom'  # vertical alignment can be adjusted
        )

    plt.savefig(os.path.join(output_folder, f"{division_name}_accuracy_vs_defense_scatter.png"))
    plt.close()

    # 4. Correlation heatmap
    correlation_columns = [
        "Age", "Reach (in)", "SLpM", "Str. Acc.", "SApM",
        "Str. Def.", "TD Avg.", "TD Acc.", "TD Def.", "Sub. Avg.", "Outcome"
    ]
    corr_matrix = df[correlation_columns].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title(f"Correlation Heatmap - {division_name}")
    plt.savefig(os.path.join(output_folder, f"{division_name}_correlation_heatmap.png"))
    plt.close()

    print(f"Charts for {division_name} saved to the '{output_folder}' folder.")


def main():
    folder_path = "ufc_stats"
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    files = [f for f in os.listdir(folder_path) if f.endswith("_top15.csv")]
    if not files:
        print(f"No division files found in the '{folder_path}' folder.")
        return

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
    division_name = selected_file.replace("_top15.csv", "").capitalize()
    print(f"\nGenerating charts for {division_name}...")
    df = preprocess_data(file_path)
    create_charts(df, division_name)


if __name__ == "__main__":
    main()
