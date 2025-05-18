
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

csv_filepath = f"{_get_current_folder()}/12.0.model-selection-data.csv"

dataset = pd.read_csv(csv_filepath)

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

#
#
#

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#
#
#

from sklearn.svm import SVC
classifierA = SVC(kernel = 'rbf', random_state = 0)
classifierA.fit(X_train, y_train)

#
#
#

from sklearn.metrics import confusion_matrix, accuracy_score
y_pred = classifierA.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)
print("accuracy_score", accuracy_score(y_test, y_pred))

#
#
#
# NEW STUFF HERE NEW STUFF HERE NEW STUFF HERE

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(
  estimator = classifierA,
  X = X_train,
  y = y_train,
  cv = 10 # k-fold -> will chunk-ify 10 times and train/test over it all
)
print("Accuracy (higher is better): {:.2f} %".format(accuracies.mean()*100))
print("Standard Deviation (lower is better): {:.2f} %".format(accuracies.std()*100))
print("All Accuracies:", accuracies.reshape(len(accuracies), 1))


# NEW STUFF HERE NEW STUFF HERE NEW STUFF HERE
#
#
#

#
#
#
# NEW STUFF HERE NEW STUFF HERE NEW STUFF HERE

classifierB = SVC(kernel = 'rbf', random_state = 0)
classifierB.fit(X_train, y_train)

from sklearn.model_selection import GridSearchCV
parameters = [
  {'C': [1.0, 1.1, 1.2, 1.3, 1.4, 1.5], 'kernel': ['linear']},
  {'C': [1.0, 1.1, 1.2, 1.3, 1.4, 1.5], 'kernel': ['rbf'], 'gamma': [2.5,2.6,2.7,2.8,2.9,3.0]}
]
# will also refit the classifier and keep the best one
grid_search = GridSearchCV(
  estimator = classifierB,
  param_grid = parameters,

  scoring = 'accuracy',

  # k-fold -> will chunk-ify 10 times and train/test over it all
  cv = 10,

  # once done, refit the classifier with the best parameters
  refit = True,

  # n_jobs = -1 # use all cpu cores (a bit much...)
  # n_jobs = 4 # use 4 cpu cores
  n_jobs = 8 # use 8 cpu cores
)
grid_search.fit(X_train, y_train)
best_accuracy = grid_search.best_score_
best_parameters = grid_search.best_params_
print("Best Accuracy: {:.2f} %".format(best_accuracy*100))
print("Best Parameters:", best_parameters)

# NEW STUFF HERE NEW STUFF HERE NEW STUFF HERE
#
#
#

# from matplotlib.colors import ListedColormap
# color_map = ListedColormap(('salmon', 'dodgerblue'))

# # X_set, y_set = sc.inverse_transform(X_train), y_train
# X_set, y_set = X_train, y_train
# X1, X2 = np.meshgrid(
#   # np.arange(start = X_set[:, 0].min() - 5, stop = X_set[:, 0].max() + 5, step = 5),
#   # np.arange(start = X_set[:, 1].min() - 5, stop = X_set[:, 1].max() + 5, step = 5)
#   np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
#   np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01)
# )

# # raw_data = sc.transform(np.array([X1.ravel(), X2.ravel()]).T)
# raw_data = np.array([X1.ravel(), X2.ravel()]).T

# fig, axs = plt.subplots(1, 2, figsize=(10, 5))  # 1 row, 2 columns

# axs[0].contourf(X1, X2, classifierA.predict(raw_data).reshape(X1.shape), alpha = 0.75, cmap = color_map)
# for i, j in enumerate(np.unique(y_set)):
#     axs[0].scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], color = color_map(i), label = j)
# axs[0].set_title('Kernel SVM (classic)')
# axs[0].set_xlabel('Age')
# axs[0].set_ylabel('Estimated Salary')

# axs[1].contourf(X1, X2, classifierB.predict(raw_data).reshape(X1.shape), alpha = 0.75, cmap = color_map)
# for i, j in enumerate(np.unique(y_set)):
#     axs[1].scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], color = color_map(i), label = j)
# axs[1].set_title('Kernel SVM (grid search)')
# axs[1].set_xlabel('Age')
# axs[1].set_ylabel('Estimated Salary')

# plt.tight_layout()
# plt.show(block=True) # <- force the window to open and stay open
