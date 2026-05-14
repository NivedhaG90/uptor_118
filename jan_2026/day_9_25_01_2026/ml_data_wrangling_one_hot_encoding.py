# Option 1
# import pandas as pd

# df = pd.read_csv("D:/PycharmProjects/Uptor_118/jan_2026/day_8_24_01_2026/diamonds.csv")
# print(df)
#
# encoded_data = pd.get_dummies(df['cut'])
# print(encoded_data)
#
# final_df = pd.concat([df, encoded_data], axis =1)
# print(final_df)
#
# modified_df = final_df.drop(columns='cut')
# print(modified_df)

# Option 2

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv("D:/PycharmProjects/Uptor_118/jan_2026/day_8_24_01_2026/diamonds.csv")
print(df)

one_hot = OneHotEncoder(sparse_output=False)

encoded_data = one_hot.fit_transform(df[['cut']])
print(encoded_data)

new_df = pd.DataFrame(encoded_data, columns=one_hot.get_feature_names_out())
print(new_df)