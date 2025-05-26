
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






from sklearn.metrics import accuracy_score

def my_keras_code(
  units,
  total_layers,
  optimizer
):

  # Build model
  model = tf.keras.models.Sequential()

  for i in range(0, total_layers):
    model.add(tf.keras.layers.Dense(units=units, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)))

  model.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

  model.compile(
    optimizer=optimizer,
    # loss="mean_squared_error",
    loss = 'binary_crossentropy',
    metrics = ['accuracy'],
  )

  # model.summary()

  early_stopping = tf.keras.callbacks.EarlyStopping(
    # monitor='val_loss',
    monitor='val_accuracy',

    # how much stalled epoch do we wait before stopping
    patience=50,

    restore_best_weights=True,
    verbose=0
  )

  model.fit(
    X_train,
    y_train,
    batch_size = 32,
    validation_data=(X_test, y_test),
    # callbacks=[early_stopping],
    callbacks=[early_stopping],
    epochs = 2,
    verbose=0
  )

  y_pred = model.predict(X_test, verbose=0)
  y_pred = (y_pred > 0.5)

  score = accuracy_score(y_test, y_pred)
  print("accuracy_score", score)

  # Return a single float as the objective value.
  return score # lower is better


class MyTuner(keras_tuner.RandomSearch):
  def run_trial(self, trial, **kwargs):
    hp = trial.hyperparameters
    return my_keras_code(
      units=hp.Int("units", 32, 128, 32),
      total_layers=hp.Int("total_layers", 1, 6, 1),
      optimizer=hp.Choice("optimizer", ["adam", "adadelta", "adamw", "adagrad"]),
    )


tuner = MyTuner(
  # important: this set it
  objective=keras_tuner.Objective("val_accuracy", direction="max"),
  max_trials=100,
  executions_per_trial=2,
  overwrite=True,
  directory=f"{_get_current_folder()}/my_dir",
  project_name="keep_code_separate",
)

# tuner.search_space_summary()

tuner.search()

# Retraining the model
best_hp = tuner.get_best_hyperparameters()[0]

print("best_hp", best_hp.values)

my_keras_code(
  **best_hp.values
)




