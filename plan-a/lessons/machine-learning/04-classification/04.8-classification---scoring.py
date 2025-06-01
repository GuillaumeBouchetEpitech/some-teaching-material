
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

# print(f"X {X}")
# print(f"y {y}")

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

class my_logistic_regression_classifier:
  def __init__(self):
    from sklearn.linear_model import LogisticRegression
    self.classifier = LogisticRegression(random_state = 0, C=1) # <- C=1 stronger means overfitting protection

  def fit(self, X, y):
    self.classifier.fit(X, y)

  def predict(self, X):
    return self.classifier.predict(X)

  def predict_proba(self, X):
    return self.classifier.predict_proba(X)

class my_knn_classifier:
  def __init__(self):
    from sklearn.neighbors import KNeighborsClassifier
    self.classifier = KNeighborsClassifier(n_neighbors = 6, metric = 'minkowski', p = 2)

  def fit(self, X, y):
    self.classifier.fit(X, y)

  def predict(self, X):
    return self.classifier.predict(X)

  def predict_proba(self, X):
    return self.classifier.predict_proba(X)

class my_svc_classifier:
  def __init__(self):
    from sklearn.svm import SVC
    self.classifier = SVC(kernel = 'rbf', probability=True, random_state = 0)

  def fit(self, X, y):
    self.classifier.fit(X, y)

  def predict(self, X):
    return self.classifier.predict(X)

  def predict_proba(self, X):
    return self.classifier.predict_proba(X)

class my_naive_bayes_classifier:
  def __init__(self):
    from sklearn.naive_bayes import GaussianNB
    self.classifier = GaussianNB()

  def fit(self, X, y):
    self.classifier.fit(X, y)

  def predict(self, X):
    return self.classifier.predict(X)

  def predict_proba(self, X):
    return self.classifier.predict_proba(X)

class my_decision_tree_classifier:
  def __init__(self):
    from sklearn.tree import DecisionTreeClassifier
    self.classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)

  def fit(self, X, y):
    self.classifier.fit(X, y)

  def predict(self, X):
    return self.classifier.predict(X)

  def predict_proba(self, X):
    return self.classifier.predict_proba(X)

class my_random_forest_classifier:
  def __init__(self):
    from sklearn.ensemble import RandomForestClassifier
    self.classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)

  def fit(self, X, y):
    self.classifier.fit(X, y)

  def predict(self, X):
    return self.classifier.predict(X)

  def predict_proba(self, X):
    return self.classifier.predict_proba(X)

#
#
#

# Evaluating the Model Performance
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, classification_report


class my_prediction_class:
  name: str
  color: str
  y_pred: np.ndarray
  score: float

  def __init__(self, name: str, classification_class):
    self.name = name

    print(self.name)

    self.classifier = classification_class()

    self.classifier.fit(X_train, y_train)
    self.y_pred = self.classifier.predict(X_test)
    self.y_pred_proba = self.classifier.predict_proba(X_test)[:, 1]

    print(classification_report(y_test, self.y_pred))

    # Calculate metrics
    self.results = {
        'Accuracy': accuracy_score(y_test, self.y_pred),
        'Precision': precision_score(y_test, self.y_pred),
        'Recall': recall_score(y_test, self.y_pred),
        'F1-Score': f1_score(y_test, self.y_pred),
        "confusion-matrix": confusion_matrix(y_test, self.y_pred),
        # ROC, ROC AUC, Receiver Operating Characteristic Area Under the Curve
        # -> how well the model can distinguish between positive and negative classes, with a score closer to 1 representing better performance
        'ROC-AUC': roc_auc_score(y_test, self.y_pred_proba)
    }

all_predictions: list[my_prediction_class] = []

all_predictions.append(my_prediction_class("log reg ", my_logistic_regression_classifier))
all_predictions.append(my_prediction_class("knn     ", my_knn_classifier))
all_predictions.append(my_prediction_class("svm     ", my_svc_classifier))
all_predictions.append(my_prediction_class("n. bayes", my_naive_bayes_classifier))
all_predictions.append(my_prediction_class("dec tree", my_decision_tree_classifier))
all_predictions.append(my_prediction_class("r.forest", my_random_forest_classifier))

#
#
#

# sort by score
def my_sort_func_by_score(values: my_prediction_class):
  return values.results["F1-Score"]

all_predictions.sort(reverse=True, key=my_sort_func_by_score)

# print sorted score
print(f"print performance F1-Score: (higher is better)")
for values in all_predictions:
  print(f"performance F1-Score '{values.name:40}' {values.results["F1-Score"]}")

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

# fig, axs = plt.subplots(nrows = 3, ncols = 6, figsize=(2.5*6, 2.5*3))  # 3 rows, 6 columns
n_rows=3
n_cols=6

plt.figure(figsize=(4 * n_cols, 4 * n_rows))  # Adjust height based on rows


for index in range(0, len(all_predictions)):

  result1 = all_predictions[index].classifier.predict(raw_data).reshape(X1.shape)
  result2 = all_predictions[index].classifier.predict_proba(raw_data)[:, 1].reshape(X1.shape)

  #
  #

  plt.subplot(n_rows, n_cols, index + 1 + n_cols * 0)

  plt.contourf(X1, X2, result1, alpha = 0.5, cmap = color_map)
  for i, j in enumerate(np.unique(y_set)):
      plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], color = color_map(i), label = j, s=1)
  plt.title(f"{all_predictions[index].name}\nscore: {all_predictions[index].results["F1-Score"]:.3f} %")
  plt.xlabel('Age')
  plt.ylabel('Estimated Salary')

  #
  #

  plt.subplot(n_rows, n_cols, index + 1 + n_cols * 1)

  plt.contourf(X1, X2, result2, alpha = 0.5, cmap = color_map)
  for i, j in enumerate(np.unique(y_set)):
      plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], color = color_map(i), label = j, s=1)
  plt.xlabel('Age')
  plt.ylabel('Estimated Salary')

  #
  #

  plt.subplot(n_rows, n_cols, index + 1 + n_cols * 2)

  sns.heatmap(all_predictions[index].results["confusion-matrix"],
              cmap = "Reds", annot = True, annot_kws = {'fontweight':'bold'},
              fmt = " ", square = True, cbar = False,
              xticklabels = labels, yticklabels = labels)
  plt.title("Confusion Matrix", fontsize = 12, fontweight = "bold", color = "black")

plt.tight_layout()
plt.show(block=True) # <- force the window to open and stay open
