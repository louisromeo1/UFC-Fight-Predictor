import pandas as pd
from loadData import load_ufc_data
from scatter_plot import plot_scatter
from regression_analysis import run_regression
from box_plot import plot_box

def main():
    folder = "ufc_stats"
    data = load_ufc_data(folder)

    print("Data loaded successfully.")

    while True:
        print("\nOptions:")
        print("1. View Scatter Plot")
        print("2. Run Regression Analysis")
        print("3. View Box Plot")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            x_metric = input("Enter X-axis metric: ")
            y_metric = input("Enter Y-axis metric: ")
            division = input("Enter Division (or press Enter for all): ").capitalize() or None
            plot_scatter(data, x_metric, y_metric, division)
        elif choice == "2":
            x_metric = input("Enter X-axis metric: ")
            y_metric = input("Enter Y-axis metric: ")
            division = input("Enter Division (or press Enter for all): ").capitalize() or None
            run_regression(data, x_metric, y_metric, division)
        elif choice == "3":
            metric = input("Enter metric for Box Plot: ")
            division = input("Enter Division (or press Enter for all): ").capitalize() or None
            plot_box(data, metric, division)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()