# Titanic Dataset EDA

This repository contains exploratory data analysis of the Titanic dataset.

## Files
- `titanic_eda.py`: Main analysis script
- `requirements.txt`: Python dependencies
- `data/titanic.csv`: Dataset
- `visualizations/`: Generated plots

## Key Findings
1. Higher survival rates among:
   - Women (74% vs 19% for men)
   - 1st class passengers (63% vs 47% 2nd, 24% 3rd)
   - Children (<10 years old)
2. Strong correlation between:
   - Fare and passenger class (-0.55)
   - SibSp and Parch (0.41)
3. 20% of Age data was missing (filled with median)

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run analysis: `python titanic_eda.py`
