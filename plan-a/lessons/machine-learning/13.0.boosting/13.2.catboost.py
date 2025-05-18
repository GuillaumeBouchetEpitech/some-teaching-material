
#
#
# UTILITY FUNCTION

def _get_current_folder() -> str:
  # import os path namespace
  import os.path
  # get the absolute path from the current file we're in
  absolute_path = os.path.abspath(__file__)
  # get the folder of the absolute path
  return os.path.dirname(absolute_path)

# UTILITY FUNCTION
#
#

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

csv_filepath = f"{_get_current_folder()}/12.0.boosting-data.csv"

dataset = pd.read_csv(csv_filepath)

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

y = (y > 3) # [2/4] -> [0/1]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)



#
#
#
# NEW STUFF HERE NEW STUFF HERE NEW STUFF HERE

from catboost import CatBoostClassifier
classifier = CatBoostClassifier()
classifier.fit(X_train, y_train)

# NEW STUFF HERE NEW STUFF HERE NEW STUFF HERE
#
#
#



from sklearn.metrics import confusion_matrix, accuracy_score
y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10)
print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))
