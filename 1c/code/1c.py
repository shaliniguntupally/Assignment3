# c) Bootstrap Samples for BloodPressure
bootstrap_samples = [data['BloodPressure'].sample(150, replace=True) for _ in range(500)]

# Calculate statistics for each bootstrap sample
bootstrap_means = [sample.mean() for sample in bootstrap_samples]
bootstrap_std_devs = [sample.std() for sample in bootstrap_samples]
bootstrap_percentiles = [np.percentile(sample, 95) for sample in bootstrap_samples]

# Calculate population statistics for BloodPressure
population_mean_bp = data['BloodPressure'].mean()
population_std_dev_bp = data['BloodPressure'].std()
population_percentile_95_bp = np.percentile(data['BloodPressure'], 95)

# Create comparison charts
plt.figure(figsize=(10, 6))

# Plotting means
plt.bar(['Sample Mean', 'Population Mean'], [np.mean(bootstrap_means), population_mean_bp], color=['purple', 'brown'])
plt.title('Comparison of BloodPressure Means')
plt.ylabel('BloodPressure')
plt.show()

# Plotting standard deviations
plt.figure(figsize=(10, 6))
plt.bar(['Sample Std Dev', 'Population Std Dev'], [np.mean(bootstrap_std_devs), population_std_dev_bp], color=['pink', 'gray'])
plt.title('Comparison of BloodPressure Standard Deviations')
plt.ylabel('BloodPressure')
plt.show()

# Plotting percentiles
plt.figure(figsize=(10, 6))
plt.bar(['Sample Percentile', 'Population Percentile'], [np.mean(bootstrap_percentiles), population_percentile_95_bp], color=['yellow', 'green'])
plt.title('Comparison of BloodPressure 95th Percentile')
plt.ylabel('BloodPressure')
plt.show()