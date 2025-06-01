
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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify=y, random_state = 0)


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)






import tensorflow as tf
import keras_tuner

tf.keras.config.set_floatx('float64')




def build_model(hp: keras_tuner.HyperParameters):
  model = tf.keras.models.Sequential()
  model.add(tf.keras.layers.Flatten())
  # Tune the number of layers.
  for i in range(hp.Int("num_layers", 1, 3)):
    model.add(
      tf.keras.layers.Dense(
        # Tune number of units separately.
        units=hp.Int(f"units_{i}", min_value=32, max_value=512, step=32),
        activation=hp.Choice("activation", ["relu", "tanh"]),
      )
    )

  if hp.Boolean("dropout"):
    model.add(tf.keras.layers.Dropout(rate=0.25))

  # model.add(tf.keras.layers.Dense(1, activation="softmax"))
  model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

  learning_rate = hp.Float("lr", min_value=1e-4, max_value=1e-2, sampling="log")
  model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
    # loss="categorical_crossentropy",
    loss="binary_crossentropy",
    metrics=["accuracy"],
  )
  return model


build_model(keras_tuner.HyperParameters())

tuner = keras_tuner.GridSearch(
  hypermodel=build_model,
  objective=keras_tuner.Objective("val_accuracy", direction="max"),
  # max_trials=100,
  seed=0,
  executions_per_trial=2,
  overwrite=True,
  directory=f"{_get_current_folder()}/_keras_tuner",
  project_name="keras_tuner-1",
)

tuner.search_space_summary()

tuner.search(
  X_train,
  y_train,
  epochs=3,
  batch_size=256,
  validation_data=(X_test, y_test)
)

models = tuner.get_best_models(num_models=2)
best_model = models[0]
best_model.summary()

tuner.results_summary()




from sklearn.metrics import accuracy_score

y_pred = best_model.predict(X_test, verbose=0)
y_pred = (y_pred > 0.5)

score = accuracy_score(y_test, y_pred)
print("best_model.accuracy_score", score)

