
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

#
#
#
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE

# Training the Logistic Regression model on the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0, C=1) # <- C=1 stronger means overfitting protection
classifier.fit(X_train, y_train)

# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
#
#
#

#
#
#

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(f" -> did not purchase prediction")
print(f"   -> correct   {cm[0][0]}")
print(f"   -> incorrect {cm[1][0]}")
print(f" -> did purchase prediction")
print(f"   -> correct   {cm[1][1]}")
print(f"   -> incorrect {cm[0][1]}")

score = accuracy_score(y_test, y_pred)
print(f"score: {score}")

#
#
#

# Visualizing

import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib.colors import ListedColormap
color_map = ListedColormap(['#FA8072', '#1E90FF'])

# X_set, y_set = sc.inverse_transform(X_train), y_train
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(
  # np.arange(start = X_set[:, 0].min() - 10, stop = X_set[:, 0].max() + 10, step = 5.0),
  # np.arange(start = X_set[:, 1].min() - 10, stop = X_set[:, 1].max() + 10, step = 5.0)
  np.arange(start = X_set[:, 0].min() - 0.1, stop = X_set[:, 0].max() + 0.1, step = 0.01),
  np.arange(start = X_set[:, 1].min() - 0.1, stop = X_set[:, 1].max() + 0.1, step = 0.01)
)
# raw_data = sc.transform(np.array([X1.ravel(), X2.ravel()]).T)
raw_data = np.array([X1.ravel(), X2.ravel()]).T


fig,ax = plt.subplots(nrows = 1, ncols = 2, figsize = (10,4.2))
ax = ax.flat

labels = ['did buy', 'did not']
sns.heatmap(cm, cmap = 'Reds', annot = True, annot_kws = {'fontweight':'bold'}, fmt = " ", square = True, cbar = False,
            xticklabels = labels, yticklabels = labels, ax = ax[0])
ax[0].set_title("Confusion Matrix", fontsize = 12, fontweight = "bold", color = "black")


ax[1].contourf(X1, X2, classifier.predict(raw_data).reshape(X1.shape), alpha = 0.75, cmap = color_map)
for i, j in enumerate(np.unique(y_set)):
  ax[1].scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], color = color_map(i), label = j)
ax[1].set_title('Purchased by age')
ax[1].set_xlabel('Age')
ax[1].set_ylabel('Estimated Salary')
plt.legend()
plt.show(block=True) # <- force the window to open and stay open
