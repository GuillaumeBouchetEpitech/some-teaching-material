
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

def get_multiple_linear_regression_predictions() -> np.ndarray:

  # Training the Multiple Linear Regression model on the Training set
  from sklearn.linear_model import LinearRegression
  regressor = LinearRegression()
  regressor.fit(X_train, y_train)

  # Predicting the Test set results
  return regressor.predict(X_test)

def get_polynomial_linear_regression() -> np.ndarray:

  # Training the Polynomial Regression model on the Training set
  from sklearn.preprocessing import PolynomialFeatures
  from sklearn.linear_model import LinearRegression
  poly_reg = PolynomialFeatures(degree = 4)
  X_poly = poly_reg.fit_transform(X_train)
  regressor = LinearRegression()
  regressor.fit(X_poly, y_train)

  # Predicting the Test set results
  return regressor.predict(poly_reg.transform(X_test))

def get_random_forest_regression() -> np.ndarray:

  # Training the Random Forest Regression model on the whole dataset
  from sklearn.ensemble import RandomForestRegressor
  regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
  regressor.fit(X_train, y_train)

  # Predicting the Test set results
  return regressor.predict(X_test)

def get_decision_tree_regression() -> np.ndarray:

  # Training the Decision Tree Regression model on the Training set
  from sklearn.tree import DecisionTreeRegressor
  regressor = DecisionTreeRegressor(random_state = 0)
  regressor.fit(X_train, y_train)

  # Predicting the Test set results
  return regressor.predict(X_test)

def get_support_vector_regression() -> np.ndarray:

  # for the "support vector regression" (SVR) -> we have to scale the features

  # Feature Scaling
  from sklearn.preprocessing import StandardScaler
  sc_X = StandardScaler()
  sc_y = StandardScaler()
  scaled_X_train = sc_X.fit_transform(X_train) # fit AND transform
  scaled_X_test = sc_X.transform(X_test) # do not fit -> just transform
  scaled_y_train = sc_y.fit_transform(y_train.reshape(-1, 1)) # reshape as a table of one column of X rows

  # Training the SVR model on the Training set
  from sklearn.svm import SVR
  regressor = SVR(kernel = 'rbf')
  regressor.fit(scaled_X_train, scaled_y_train)

  # Predicting the Test set results
  return sc_y.inverse_transform(regressor.predict(scaled_X_test).reshape(-1,1)) # reshape as a table of one column of X rows

#
#
#

# Evaluating the Model Performance
from sklearn.metrics import r2_score

class my_prediction_class:
  name: str
  color: str
  y_pred: np.ndarray
  score: float

  def __init__(self, name: str, color: str, y_pred: np.ndarray):
    self.name = name
    self.color = color
    self.y_pred = y_pred
    self.score = r2_score(y_test, y_pred)

all_predictions: list[my_prediction_class] = []

all_predictions.append(my_prediction_class("multiple linear regression", "red", get_multiple_linear_regression_predictions()))
all_predictions.append(my_prediction_class("polynomial linear regression", "orange", get_polynomial_linear_regression()))
all_predictions.append(my_prediction_class("random forest regression", "blue", get_random_forest_regression()))
all_predictions.append(my_prediction_class("decision tree regression", "purple", get_decision_tree_regression()))
all_predictions.append(my_prediction_class("support vector regression", "brown", get_support_vector_regression()))

#
#
#

# sort by score
def my_sort_func_by_score(values: my_prediction_class):
  return values.score

all_predictions.sort(reverse=True, key=my_sort_func_by_score)

# print sorted score
print(f"print performance score: (higher is better)")
for values in all_predictions:
  print(f"performance score for '{values.name}' {values.score}")

#
#
#

x_axis = [x for x in range(0, len(y_test))]

import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))  # set plot size (denoted in inches)

# plot the test set
plt.plot(
  x_axis,
  y_test.reshape(len(y_test), 1),
  100,
  color='green',
  label='test set',
  linestyle='dashed'
)

for values in all_predictions:
  # plot this predicted set
  plt.plot(
    x_axis,
    # reshape from a table of 1 columns and X rows to as single continuous row
    values.y_pred.reshape(len(values.y_pred), 1),
    100,
    color=values.color,
    # label is name + score
    label=f"{values.name} ({values.score})"
  )

#
#
#

plt.legend()

plt.xlabel('Indices')
plt.ylabel('Profits')
plt.title('Profits test/predictions comparison')
plt.grid()
plt.show(block=True) # <- force the window to open and stay open
