import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips') #tips is inbuilt dataset available in seaborn library

#bins - for better visibility. background Boxes in the chart
#kde - density

sns.histplot(tips['total_bill'], bins=20, kde=True)
plt.title('Histogram: Distribution of Total bill')
plt.show()