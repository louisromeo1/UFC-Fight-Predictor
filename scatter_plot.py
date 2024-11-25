import matplotlib.pyplot as plt

def plot_scatter(data, x_metric, y_metric, division=None):
    filtered_data = data if division is None else data[data["Division"] == division]

    plt.figure(figsize=(10, 6))
    for div in filtered_data["Division"].unique():
        subset = filtered_data[filtered_data["Division"] == div]
        plt.scatter(subset[x_metric], subset[y_metric], label=div)

    plt.title(f"Scatter Plot: {x_metric} vs {y_metric}")
    plt.xlabel(x_metric)
    plt.ylabel(y_metric)
    plt.legend(title="Division")
    plt.grid()
    plt.show()