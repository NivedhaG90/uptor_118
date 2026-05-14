import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips') #tips is inbuilt dataset available in seaborn library

sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.title('Scatter plot: Total bill vs tip')
plt.show()