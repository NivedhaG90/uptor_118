import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips') #tips is inbuilt dataset available in seaborn library

sns.boxplot(x='day', y='total_bill', data=tips)
plt.title('Boxplot: Total bill by day')
plt.show()