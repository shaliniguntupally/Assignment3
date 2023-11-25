import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('your_data_file.csv')

# a) Random Sample
seed = 42  # set seed for reproducibility
sample = data.sample(25, random_state=seed)

# Calculate mean and highest values for Glucose in the sample
sample_mean_glucose = sample['Glucose'].mean()
sample_highest_glucose = sample['Glucose'].max()

# Compare with population statistics
population_mean_glucose = data['Glucose'].mean()
population_highest_glucose = data['Glucose'].max()

# Create comparison charts
plt.figure(figsize=(10, 6))

# Plotting sample and population means
plt.bar(['Sample Mean', 'Population Mean'], [sample_mean_glucose, population_mean_glucose], color=['blue', 'orange'])
plt.title('Comparison of Glucose Means')
plt.ylabel('Glucose')
plt.show()

# Plotting sample and population highest values
plt.figure(figsize=(10, 6))
plt.bar(['Sample Highest', 'Population Highest'], [sample_highest_glucose, population_highest_glucose], color=['green', 'red'])
plt.title('Comparison of Highest Glucose Values')
plt.ylabel('Glucose')
plt.show()


