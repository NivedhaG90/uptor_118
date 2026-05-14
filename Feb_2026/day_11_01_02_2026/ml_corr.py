import matplotlib.pyplot as plt
import seaborn as sns

#correlation is only for numbers

# Load sample dataset
iris = sns.load_dataset('iris')

# Calculate correlation matrix for numeric columns only
correlation_matrix = iris.select_dtypes(include='number').corr()

#Plot heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap of Correlation Matrix (Iris Dataset)')

plt.show()