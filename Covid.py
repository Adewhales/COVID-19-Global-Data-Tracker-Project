import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("owid_covid_data.csv")

# Data Cleaning
df = df[['location', 'date', 'total_cases', 'total_deaths', 'total_vaccinations']]
df['date'] = pd.to_datetime(df['date'], dayfirst=True)
df = df.dropna()

# Filter for selected countries
countries = ["Nigeria", "South Africa", "Japan", "Egypt", "Russia", "Canada"]
df_selected = df[df['location'].isin(countries)]

# Analyze time trends
df_grouped = df_selected.groupby(['location', 'date']).sum().reset_index()

# Visualization: Cases and Deaths over time
plt.figure(figsize=(10, 5))
sns.lineplot(data=df_grouped, x='date', y='total_cases', hue='location')
plt.title("COVID-19 Cases Over Time")
plt.xticks(rotation=45)
plt.show()

# Visualization: Vaccination rates comparison
plt.figure(figsize=(10, 5))
sns.barplot(data=df_grouped, x='location', y='total_vaccinations')
plt.title("Vaccination Rates Across Selected Countries")
plt.xticks(rotation=45)
plt.show()
