from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.datasets import load_iris

load_iris_input = load_iris()

x = load_iris_input.data
y = load_iris_input.target

print(x)
print('--------------')
print(y)
print('--------------')

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state = 42)

print(x_train, x_test, y_train, y_test)
print('--------------')

#model = LogisticRegression()
#model = LogisticRegression(penalty="l2") #l1 for linear, l2 for classifier. Wantedly adding penalty points so the model is not overfit.
# It will add errors and reduce accuracy.
#got deprecated warning, so using below
model = LogisticRegression(l1_ratio=0)
model.fit(x_train,y_train)

prediction = model.predict(x_test)
print(prediction)

predicted_names = load_iris_input.target_names[prediction]
print(predicted_names)

final_accuracy_check = accuracy_score(y_test, prediction)
print(final_accuracy_check)