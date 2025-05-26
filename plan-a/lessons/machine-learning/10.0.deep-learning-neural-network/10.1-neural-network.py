
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



model_filepath = f"{_get_current_folder()}/10.1.deep-learning-model.keras"

from pathlib import Path

model_file = Path(model_filepath)
if model_file.exists() and model_file.is_file() and False:

  print("model file was found")
  print("reusing previously trained model")

  ann = tf.keras.models.load_model(model_filepath)

else:

  print("model file was not found")
  print("training new model")

  ann = tf.keras.models.Sequential()
  ann.add(tf.keras.layers.Dense(units=64, activation='relu'))
  ann.add(tf.keras.layers.Dense(units=64, activation='relu'))
  ann.add(tf.keras.layers.Dense(units=32, activation='relu'))
  ann.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

  ann.compile(
    optimizer = tf.keras.optimizers.Adam(0.01),
    loss = 'binary_crossentropy',
    metrics = ['accuracy']
  )

  ann.fit(X_train, y_train, batch_size = 256, epochs = 100)

  # Save the model
  ann.save(model_filepath)


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



def predict_if_custom_exit(
  CreditScore: int,
  Geography: str, # France, Spain, Germany
  Gender: str, # Female, Male
  Age: int,
  Tenure: int,
  Balance: int,
  NumOfProducts: int,
  HasCrCard: int,
  IsActiveMember: int,
  EstimatedSalary: int
):

  print("----------------------------------------------")
  print("will my customer exit?")
  print(f" -> CreditScore:     {CreditScore}")
  print(f" -> Geography:       {Geography}")
  print(f" -> Gender:          {Gender}")
  print(f" -> Age:             {Age}")
  print(f" -> Tenure:          {Tenure}")
  print(f" -> Balance:         {Balance}")
  print(f" -> NumOfProducts:   {NumOfProducts}")
  print(f" -> HasCrCard:       {HasCrCard}")
  print(f" -> IsActiveMember:  {IsActiveMember}")
  print(f" -> EstimatedSalary: {EstimatedSalary}")
  print("------------")

  X_raw = np.array([[
    CreditScore,
    Geography, # (must be OneHotEncoded)
    Gender, # (must be LabelEncoded)
    Age,
    Tenure,
    Balance,
    NumOfProducts,
    HasCrCard,
    IsActiveMember,
    EstimatedSalary
  ]])

  # label encoded -> Gender -> 0 or 1
  X_raw[:, 2] = le.transform(X_raw[:, 2])

  # column transformer -> Geography -> translated as 3 columns at the front
  X_raw = np.array(ct.transform(X_raw))

  y_pred = ann.predict(sc.transform(X_raw), verbose=0)

  y_pred = y_pred.reshape(1,) # one dimension numpy array

  print(f"exit chances: {y_pred[0]:.3f}")
  print(f"exit result:  {y_pred[0] > 0.5}")

predict_if_custom_exit(300, "France", "Male", 20, 1, 7000, 1, 1, 0, 14000)
predict_if_custom_exit(800, "Spain", "Female", 40, 3, 70000, 2, 1, 1, 80000)

