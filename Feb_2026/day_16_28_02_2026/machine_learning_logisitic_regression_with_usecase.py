# Import necessary libraries
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load the dataset of images of handwritten digits
digits = load_digits()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(digits.data,
                                                    digits.target,
                                                    random_state=0)

# Create a logistic regression classifier
clf = LogisticRegression(max_iter=5000, random_state=0)

# Train the model using the training set
clf.fit(X_train, y_train)

# Evaluate the model's performance on the test set
accuracy = clf.score(X_test, y_test)
print("Accuracy: %0.2f" % accuracy)