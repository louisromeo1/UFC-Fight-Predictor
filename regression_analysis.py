import statsmodels.api as sm
import pandas as pd

def run_regression(data, x_metric, y_metric, division=None):
    filtered_data = data if division is None else data[data["Division"] == division]

    X = filtered_data[x_metric]
    y = filtered_data[y_metric]

    X = sm.add_constant(X)  # Add constant term for intercept
    model = sm.OLS(y, X).fit()

    print(model.summary())
    return model