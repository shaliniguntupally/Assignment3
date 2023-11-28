sample_98th_percentile_bmi = np.percentile(sample['BMI'], 98)
population_98th_percentile_bmi = np.percentile(data['BMI'], 98)

# Create comparison charts
plt.figure(figsize=(10, 6))
sns.kdeplot(sample['BMI'], label='Sample BMI')
sns.kdeplot(data['BMI'], label='Population BMI')
plt.axvline(sample_98th_percentile_bmi, color='blue', linestyle='dashed', label='Sample 98th Percentile')
plt.axvline(population_98th_percentile_bmi, color='orange', linestyle='dashed', label='Population 98th Percentile')
plt.title('Comparison of BMI 98th Percentile')
plt.xlabel('BMI')
plt.legend()
plt.show()
