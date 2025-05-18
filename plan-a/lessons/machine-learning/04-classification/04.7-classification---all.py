
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

csv_filepath = f"{_get_current_folder()}/04-classification-data.csv"

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

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

#
#
#

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#
#
#

def get_logistic_regression_classification_predictions(X_input) -> np.ndarray:

  # Training the Logistic Regression model on the Training set
  from sklearn.linear_model import LogisticRegression
  classifier = LogisticRegression(random_state = 0, C=1) # <- C=1 stronger means overfitting protection
  classifier.fit(X_train, y_train)

  # Predicting the Test set results
  return classifier.predict(X_input)

def get_k_nearest_neighbors_classification_predictions(X_input) -> np.ndarray:

  # Training the K-NN model on the Training set
  from sklearn.neighbors import KNeighborsClassifier
  classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
  classifier.fit(X_train, y_train)

  # Predicting the Test set results
  return classifier.predict(X_input)

def get_svm_classification_predictions(X_input) -> np.ndarray:

  # Training the Kernel SVM model on the Training set
  from sklearn.svm import SVC
  classifier = SVC(kernel = 'rbf', random_state = 0)
  classifier.fit(X_train, y_train)

  # Predicting the Test set results
  return classifier.predict(X_input)

def get_naive_bayes_classification_predictions(X_input) -> np.ndarray:

  # Training the Naive Bayes model on the Training set
  from sklearn.naive_bayes import GaussianNB
  classifier = GaussianNB()
  classifier.fit(X_train, y_train)

  # Predicting the Test set results
  return classifier.predict(X_input)

def get_decision_tree_classification_predictions(X_input) -> np.ndarray:

  # Training the Decision Tree Classification model on the Training set
  from sklearn.tree import DecisionTreeClassifier
  classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
  classifier.fit(X_train, y_train)

  # Predicting the Test set results
  return classifier.predict(X_input)

def get_random_forest_classification_predictions(X_input) -> np.ndarray:

  # Training the Random Forest Classification model on the Training set
  from sklearn.ensemble import RandomForestClassifier
  classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)

  classifier.fit(X_train, y_train)

  # Predicting the Test set results
  return classifier.predict(X_input)


#
#
#

# Evaluating the Model Performance
from sklearn.metrics import confusion_matrix, accuracy_score

class my_prediction_class:
  name: str
  color: str
  y_pred: np.ndarray
  score: float

  def __init__(self, name: str, color: str, predict_callback):
    self.name = name
    self.color = color
    self.predict_callback = predict_callback
    self.y_pred = predict_callback(X_test)
    self.score = accuracy_score(y_test, self.y_pred)
    self.confusion_matrix = confusion_matrix(y_test, self.y_pred)

all_predictions: list[my_prediction_class] = []


all_predictions.append(my_prediction_class("logistic regression", "red", get_logistic_regression_classification_predictions))
all_predictions.append(my_prediction_class("k-nearest-neighbors", "orange", get_k_nearest_neighbors_classification_predictions))
all_predictions.append(my_prediction_class("svm", "blue", get_svm_classification_predictions))
all_predictions.append(my_prediction_class("naive bayes", "purple", get_naive_bayes_classification_predictions))
all_predictions.append(my_prediction_class("decision tree", "brown", get_decision_tree_classification_predictions))
all_predictions.append(my_prediction_class("random forest", "yellow", get_random_forest_classification_predictions))

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

# x_axis = [x for x in range(0, len(y_test))]

# import matplotlib.pyplot as plt

# plt.figure(figsize=(10,10))  # set plot size (denoted in inches)

# # plot the test set
# plt.plot(
#   x_axis,
#   y_test.reshape(len(y_test), 1),
#   3,
#   color='green',
#   label='test set',
#   linestyle='dashed'
# )

# for values in all_predictions:
#   # plot this predicted set
#   plt.plot(
#     x_axis,
#     # reshape from a table of 1 columns and X rows to as single continuous row
#     values.y_pred.reshape(len(values.y_pred), 1),
#     3,
#     color=values.color,
#     # label is name + score
#     label=f"{values.name} ({values.score})"
#   )

# #
# #
# #

# plt.legend()

# plt.xlabel('Indices')
# plt.ylabel('Profits')
# plt.title('Profits test/predictions comparison')
# plt.grid()
# plt.show(block=True) # <- force the window to open and stay open


from matplotlib.colors import ListedColormap
color_map = ListedColormap(('salmon', 'dodgerblue'))

# X_set, y_set = sc.inverse_transform(X_train), y_train
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(
  # np.arange(start = X_set[:, 0].min() - 5, stop = X_set[:, 0].max() + 5, step = 5),
  # np.arange(start = X_set[:, 1].min() - 5, stop = X_set[:, 1].max() + 5, step = 5)
  np.arange(start = X_set[:, 0].min() - 0.1, stop = X_set[:, 0].max() + 0.1, step = 0.01),
  np.arange(start = X_set[:, 1].min() - 0.1, stop = X_set[:, 1].max() + 0.1, step = 0.01)
)

# raw_data = sc.transform(np.array([X1.ravel(), X2.ravel()]).T)
raw_data = np.array([X1.ravel(), X2.ravel()]).T

labels = ['did buy', 'did not']

import matplotlib.pyplot as plt
import seaborn as sns

fig, axs = plt.subplots(nrows = 2, ncols = 6, figsize=(2.5*6, 2.5*2))  # 1 row, 6 columns

for index in range(0, len(all_predictions)):

  result = all_predictions[index].predict_callback(raw_data).reshape(X1.shape)

  axs[0, index].contourf(X1, X2, result, alpha = 0.5, cmap = color_map)
  for i, j in enumerate(np.unique(y_set)):
      axs[0, index].scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], color = color_map(i), label = j, s=1)
  axs[0, index].set_title("{}\nscore: {:.2f} %".format(all_predictions[index].name, all_predictions[index].score))
  axs[0, index].set_xlabel('Age')
  axs[0, index].set_ylabel('Estimated Salary')

  sns.heatmap(all_predictions[index].confusion_matrix,
              cmap = "Reds", annot = True, annot_kws = {'fontweight':'bold'},
              fmt = " ", square = True, cbar = False,
              xticklabels = labels, yticklabels = labels, ax = axs[1, index])
  axs[1, index].set_title("Confusion Matrix", fontsize = 12, fontweight = "bold", color = "black")

plt.tight_layout()
plt.show(block=True) # <- force the window to open and stay open
