import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load dataset
df = pd.read_csv('data/titanic.csv')

# Initial inspection
print("First 5 rows:")
print(df.head())

print("\nData info:")
print(df.info())

print("\nBasic statistics:")
print(df.describe())

# Data cleaning
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Visualization setup
plt.style.use('seaborn')
sns.set_palette("husl")

# Age distribution
plt.figure(figsize=(10,6))
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Age Distribution of Passengers')
plt.savefig('visualizations/age_distribution.png')
plt.close()

# Survival by class
plt.figure(figsize=(10,6))
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title('Survival Count by Passenger Class')
plt.savefig('visualizations/survival_by_class.png')
plt.close()

# Correlation heatmap
plt.figure(figsize=(12,8))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.savefig('visualizations/correlation_heatmap.png')
plt.close()

# Boxplot of fares by class
plt.figure(figsize=(10,6))
sns.boxplot(x='Pclass', y='Fare', data=df)
plt.title('Fare Distribution by Passenger Class')
plt.savefig('visualizations/fare_by_class.png')
plt.close()

# Interactive plot (Plotly)
fig = px.scatter(df, x='Age', y='Fare', color='Survived', 
                 hover_data=['Name', 'Sex', 'Pclass'])
fig.write_html('visualizations/interactive_plot.html')