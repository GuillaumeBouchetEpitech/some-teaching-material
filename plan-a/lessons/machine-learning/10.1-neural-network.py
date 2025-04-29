
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

import pandas as pd
import numpy as np

csv_filepath = f"{_get_current_folder()}/10.0.deep-learning-neural-network-data.csv"

dataset = pd.read_csv(csv_filepath)

#
#
#

import tensorflow as tf

X = dataset.iloc[:, 3:-1].values # CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary
y = dataset.iloc[:, -1].values # Exited

print("X", X)
print("y", y)

#
#
# preprocess categorical data "Gender" in place

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X[:, 2] = le.fit_transform(X[:, 2])

print("Gender is now encoded", X)

#
#
# preprocess categorical data "Geography" as multiple columns

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

print("Geography is now encoded over multiple columns", X)

#
#
#

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


from pathlib import Path

model_filepath = f"{_get_current_folder()}/10.1.deep-learning-model.keras"

model_file = Path(model_filepath)
if model_file.exists() and model_file.is_file():

  print("model file was found")
  print("reusing previously trained model")

  ann = tf.keras.models.load_model(model_filepath)

else:

  print("model file was not found")
  print("training new model")

  ann = tf.keras.models.Sequential()
  ann.add(tf.keras.layers.Dense(units=6, activation='relu'))
  ann.add(tf.keras.layers.Dense(units=6, activation='relu'))
  ann.add(tf.keras.layers.Dense(units=1, activation='relu'))

  ann.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

  ann.fit(X_train, y_train, batch_size = 32, epochs = 100)

  # Save the model
  ann.save(model_filepath)



print(ann.predict(sc.transform([[1, 0, 0, 600, 1, 40, 3, 60000, 2, 1, 1, 50000]])) > 0.5)


y_pred = ann.predict(X_test)
y_pred = (y_pred > 0.5)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print("confusion matrix", cm)
print(f" -> did not purchase prediction")
print(f"   -> correct   {cm[0][0]}")
print(f"   -> incorrect {cm[1][0]}")
print(f" -> did purchase prediction")
print(f"   -> correct   {cm[1][1]}")
print(f"   -> incorrect {cm[0][1]}")


print("accuracy_score", accuracy_score(y_test, y_pred))

