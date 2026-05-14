
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# load the iris dataset as an example
my_data = load_iris()
X = my_data.data
y = my_data.target


# split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# standardize the data
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, auc
from sklearn.metrics import roc_curve
from matplotlib import pyplot

# fit a logistic regression model to the data
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

# make predictions on the test set
y_pred = logreg.predict(X_test)

# calculate the roc auc for each class
roc_auc = dict()
for i in range(3):
    fpr, tpr, _ = roc_curve(y_test == i, y_pred == i)
    roc_auc[i] = auc(fpr, tpr)

# Plot of a ROC curve for a specific class
for i in range(3):
    pyplot.figure()
    pyplot.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc[i])
    pyplot.plot([0, 1], [0, 1], 'k--')
    pyplot.xlim([0.0, 1.0])
    pyplot.ylim([0.0, 1.05])
    pyplot.xlabel('False Positive Rate')
    pyplot.ylabel('True Positive Rate')
    pyplot.title('ROC Curve for class {}'.format(i))
    pyplot.legend(loc="lower right")
pyplot.show()
