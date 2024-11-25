import matplotlib.pyplot as plt

def plot_box(data, metric, division=None):
    filtered_data = data if division is None else data[data["Division"] == division]

    plt.figure(figsize=(10, 6))
    filtered_data.boxplot(column=metric, by="Division", grid=False, figsize=(12, 8))
    plt.title(f"Box Plot of {metric} by Division")
    plt.suptitle("")  # Remove default title for grouped boxplot
    plt.xlabel("Division")
    plt.ylabel(metric)
    plt.xticks(rotation=45)
    plt.show()