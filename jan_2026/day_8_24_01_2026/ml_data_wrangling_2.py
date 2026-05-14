import pandas as pd

df = pd.read_csv("diamonds.csv")
print(df['cut'])

finding_cut_category = df['cut'].value_counts()
print(finding_cut_category)

unique_finding_cut_category = df['cut'].unique()
print(unique_finding_cut_category)

#every column we choose to be numeric in data science

category_filling = {'Ideal': 10, 'Good' : 20, 'Premium' : 30, 'Very Good': 40, 'Fair': 50}
df['cut'] = df['cut'].map(category_filling)
print(df['cut'])