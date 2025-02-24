# UFC Fight Predictor

Welcome to the **UFC Fight Predictor**, a Python-based project designed to provide predictive insights into UFC fights using statistical analysis, machine learning, and data visualization. This repository contains scripts to analyze fighter statistics, predict fight outcomes, and visualize key metrics, helping fans and analysts understand UFC matchups. It leverages data from UFC fighter stats updated as of UFC 308 (October 2024) to deliver predictions and comparisons.

## Project Overview

The UFC Fight Predictor combines statistical comparisons, weighted scoring, machine learning, and visualization to evaluate fighters and predict hypothetical matchups. Whether you're a casual fan or a data enthusiast, these tools allow you to explore fighter performance and forecast fight outcomes.

## Repository Structure

Below is a list of the files and folders in this repository with their purposes:

### Files

1. **`UFC_fight_predictor.py`**
   - **Description**: Calculates a "Winning Chance" percentage for fighters in a division using weighted metrics (e.g., Age, Reach, Strikes Landed per Minute). Predicts hypothetical matchups by comparing performance scores.
   - **Features**: Weighted scoring, division selection, matchup prediction.
   - **Usage**: Run the script, select a division, and enter two fighter names for a prediction.

2. **`UFC_data_visualizations.py`**
   - **Description**: Generates visualizations (histograms, boxplots, scatter plots, heatmaps) for fighter stats in a selected division. Identifies trends and correlations (e.g., Strike Accuracy vs. Strike Defense).
   - **Features**: Visualizes key metrics, adds fighter names to scatter plots, saves charts to a `charts` folder.
   - **Usage**: Run the script, select a division, and check the `charts` folder for output.

3. **`UFC_stats_view.py`**
   - **Description**: An interactive tool for exploring UFC data through scatter plots, regression analysis, and box plots. Users specify metrics and divisions for custom analysis.
   - **Features**: Flexible plotting, supports all or specific divisions, depends on `load_data.py`, `scatter_plot.py`, `regression_analysis.py`, and `box_plot.py`.
   - **Usage**: Run the script and choose menu options for custom visualizations or regressions.

4. **`UFC_non_linear_predictor.py`**
   - **Description**: Uses Random Forest and Gradient Boosting models to predict fight outcomes based on fighter stats. Trains models and predicts hypothetical matchups.
   - **Features**: ML-based predictions, performance evaluation with classification reports, matchup probabilities.
   - **Usage**: Run the script, select a division, and input two fighter names for model predictions.

5. **`UFC_winning_margin.py`**
   - **Description**: Compares two fighters head-to-head, counting advantages in metrics (e.g., Reach, Takedown Defense) to predict a winner.
   - **Features**: Detailed stat comparison, advantage tracking, winner prediction based on advantage count.
   - **Usage**: Run the script, specify the `ufc_stats` folder and a division, and enter two fighter names for a comparison.

6. **`loadData.py`**
   - **Description**: Helper script to load and combine UFC data from multiple CSV files in the `ufc_stats` folder into a single DataFrame.
   - **Features**: Adds a `Division` column, supports aggregation across divisions.
   - **Usage**: Used by `interactive_analysis.py` and other scripts to load data.

7. **`box_plot.py`**
   - **Description**: Helper script to create box plots of a specified metric across divisions or a single division.
   - **Features**: Visualizes metric distribution, customizable by division.
   - **Usage**: Called by `interactive_analysis.py` for box plot generation.

8. **`regression_analysis.py`**
   - **Description**: Helper script to perform regression analysis between two metrics, showing the relationship and statistical significance.
   - **Features**: Linear regression with slope, intercept, R-squared, and p-value output.
   - **Usage**: Called by `interactive_analysis.py` for regression analysis.

9. **`scatter_plot.py`**
   - **Description**: Helper script to create scatter plots comparing two metrics, optionally filtered by division.
   - **Features**: Visualizes relationships between metrics with division-specific or aggregated data.
   - **Usage**: Called by `interactive_analysis.py` for scatter plot generation.

### Folders

- **`ufc_stats/`**
   - **Description**: Contains CSV files with divisional fighter stats (e.g., `lightweight_top15.csv`) updated as of UFC 308 (October 2024). Includes columns like `Fighter Name`, `Age`, `Reach (in)`, `SLpM`, etc.
   - **Usage**: Place these files in the `ufc_stats` folder for scripts to process.

## Prerequisites

- **Python 3.8+**
- **Libraries**:
  - `pandas` (data manipulation)
  - `numpy` (numerical operations)
  - `matplotlib` (plotting)
  - `seaborn` (enhanced visualizations)
  - `scikit-learn` (machine learning)

Install dependencies with pip:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn