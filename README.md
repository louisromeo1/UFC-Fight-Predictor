# UFC Fight Predictor

Welcome to the **UFC Fight Predictor**, a Python-based project designed to provide predictive insights into UFC fights using statistical analysis, machine learning, and data visualization. This repository contains scripts to analyze fighter statistics, predict fight outcomes, and visualize key metrics to help fans and analysts understand UFC matchups. It uses data from UFC rankings and fighter stats updated as of UFC 308 (October 2024) to deliver predictions and comparisons.

## Project Overview

The UFC Fight Predictor combines statistical comparisons, weighted scoring, machine learning, and visualization to evaluate fighters and predict hypothetical matchups. It's designed for casual fans and data enthusiasts alike to explore fighter performance and forecast fight outcomes.

## Repository Structure

Below is a list of the files and folders in this repository with their purposes:

### Files

1. **`fight_winning_chance.py`**
   - **Description**: Calculates a "Winning Chance" percentage for fighters in a division based on weighted metrics (e.g., Age, Reach, Strikes Landed per Minute). Predicts hypothetical matchups by comparing performance scores.
   - **Features**: Weighted scoring, division selection, matchup prediction.
   - **Usage**: Run the script, select a division, and enter two fighter names for a prediction.

2. **`visualize_stats.py`**
   - **Description**: Generates visualizations (histograms, boxplots, scatter plots, heatmaps) for fighter stats in a selected division. Identifies trends and correlations (e.g., Strike Accuracy vs. Strike Defense).
   - **Features**: Visualizes key metrics, adds fighter names to scatter plots, saves charts to a 'charts' folder.
   - **Usage**: Run the script, select a division, and check the 'charts' folder for output.

3. **`interactive_analysis.py`**
   - **Description**: An interactive tool for exploring UFC data via scatter plots, regression analysis, and box plots. Users specify metrics and divisions for custom analysis.
   - **Features**: Flexible plotting, supports all or specific divisions, requires helper scripts (e.g., loadData.py, box_plot.py).
   - **Usage**: Run the script and choose menu options for custom visualizations or regressions.

4. **`machine_learning_predictor.py`**
   - **Description**: Uses Random Forest and Gradient Boosting models to predict fight outcomes based on stats. Trains models and predicts hypothetical matchups.
   - **Features**: ML-based predictions, performance evaluation with classification reports, matchup probabilities.
   - **Usage**: Run the script, select a division, and input two fighter names for model predictions.

5. **`statistical_comparison.py`**
   - **Description**: Compares two fighters head-to-head, counting advantages in metrics (e.g., Reach, Takedown Defense) to predict a winner.
   - **Features**: Detailed stat comparison, advantage tracking, winner prediction based on advantage count.
   - **Usage**: Run the script, specify a folder and division, and enter two fighter names for a comparison.

6. **`ufc_rankings_scraper.py`**
   - **Description**: Web scrapes current UFC rankings from ufc.com/rankings and saves them to 'ufcrankings.csv'.
   - **Features**: Scrapes Pound-for-Pound, men's, and women's divisions, includes rank changes.
   - **Usage**: Run the script to generate an updated 'ufcrankings.csv' file.

7. **`loadData.py`**
   - **Description**: Helper script to load and combine UFC data from multiple CSV files in the 'ufc_stats' folder into a single DataFrame.
   - **Features**: Adds a 'Division' column, supports aggregation across divisions.
   - **Usage**: Used by other scripts (e.g., interactive_analysis.py) to load data.

8. **`box_plot.py`**
   - **Description**: Helper script to create box plots of a specified metric across divisions or a single division.
   - **Features**: Visualizes metric distribution, customizable by division.
   - **Usage**: Called by interactive_analysis.py for box plot generation.

### Folders

- **`ufc_stats/`**
   - **Description**: Contains CSV files with divisional fighter stats (e.g., lightweight_top15.csv) updated as of UFC 308 (October 2024). Includes columns like Fighter Name, Age, Reach (in), SLpM, etc.
   - **Usage**: Place these files in the 'ufc_stats' folder for scripts to process.

## Prerequisites

- **Python 3.8+**
- **Libraries**:
  - `pandas` (data manipulation)
  - `numpy` (numerical operations)
  - `matplotlib` (plotting)
  - `seaborn` (enhanced visualizations)
  - `scikit-learn` (machine learning)
  - `beautifulsoup4` (web scraping)
  - `requests` (HTTP requests)

Install dependencies with pip:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn beautifulsoup4 requests