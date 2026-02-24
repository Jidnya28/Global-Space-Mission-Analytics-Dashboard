import pandas as pd

# Load dataset
df = pd.read_csv('Global_Space_Mission_Dataset.csv')

# Basic KPIs
total_missions = len(df)
successful_missions = len(df[df['Mission_Status'] == 'Success'])
failure_rate = len(df[df['Mission_Status'] == 'Failure']) / total_missions * 100

print("Total Missions:", total_missions)
print("Successful Missions:", successful_missions)
print("Failure Rate (%):", round(failure_rate,2))

# Company Success Rate
company_performance = df.groupby('Company')['Mission_Status'].value_counts(normalize=True).unstack().fillna(0)
print(company_performance)

# Cost Analysis
cost_by_satellite = df.groupby('Satellite_Type')['Rocket_Cost'].sum()
print(cost_by_satellite)
