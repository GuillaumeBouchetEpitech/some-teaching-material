
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

#
#
#

import pandas as pd

csv_filepath = f"{_get_current_folder()}/03-regression-data.csv"

# df -> means "data frame"
df = pd.read_csv(csv_filepath)

#
#
#

import numpy as np

# take all the rows, take all the columns except the last column one

X = df.iloc[:, :-1].values # will contains the values of the columns 'R&D Spend', 'Administration', 'Marketing Spend', 'State'

# take all the rows, take only the last column

y = df.iloc[:, -1].values # will contains the values of the columns 'Profit'

print(f"X {X}")
print(f"y {y}")

#
#
#

# some categorical values -> 'State' column

# encoding the categorical values next

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
my_encoder = OneHotEncoder()
ct = ColumnTransformer(
  transformers=[('encoder', my_encoder, [3])], # <- [3] is list of columns indices to transform
  remainder='passthrough' # <- so we keep all the other columns
)
# must convert to numpy array, just to be sure
X = np.array(ct.fit_transform(X))

#
#
#

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#
#
#

#
#
#
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE

# Training the Multiple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
#
#
#

#
#
#

# Evaluating the Model Performance
from sklearn.metrics import r2_score
score = r2_score(y_test, y_pred)
print(f"performance score (higher is better) {score}")

#
#
#

import matplotlib.pyplot as plt
x_axis = [x for x in range(0, len(y_pred))]

plt.plot(x_axis, y_pred.reshape(len(y_pred), 1), 100, color='red', label='prediction')
plt.plot(x_axis, y_test.reshape(len(y_test), 1), 100, color='green', label='test set', linestyle='dashed')
plt.legend()

plt.xlabel('Indices')
plt.ylabel('Profits')
plt.title('Profits test/predictions comparison')
plt.grid()
plt.show(block=True) # <- force the window to open and stay open
