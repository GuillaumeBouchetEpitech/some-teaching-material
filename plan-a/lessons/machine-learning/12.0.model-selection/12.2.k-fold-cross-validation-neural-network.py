
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

X = dataset.iloc[:, :-1].values # Age,EstimatedSalary
y = dataset.iloc[:, -1].values # Purchased

#
#
#

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

#
#
#

import os

import tensorflow as tf

tf.keras.backend.set_floatx("float64")

from pathlib import Path

model_filepath = f"{_get_current_folder()}/12.2.k-fold-cross-validation-neural-network.keras"

model_file = Path(model_filepath)
if model_file.exists() and model_file.is_file() and False:

  print("model file was found")
  print("reusing previously trained model")

  ann = tf.keras.models.load_model(model_filepath)

else:

  print("model file was not found")
  print("training new model")

  # results: list[tuple[float, float]] = []
  original_acc_per_fold: list[float] = []
  acc_per_fold: list[float] = []
  loss_per_fold: list[float] = []

  num_folds = 10

  from sklearn.model_selection import KFold

  kfold = KFold(n_splits=num_folds, shuffle=True, random_state=0)

  # K-fold Cross Validation model evaluation
  fold_no = 1
  for train_indices, test_indices in kfold.split(X, y):

    X_train = X[train_indices, :]
    y_train = y[train_indices]
    X_test = X[test_indices, :]
    y_test = y[test_indices]


    model = tf.keras.models.Sequential()

    # # mean_accuracy: 85.667
    # # mean_loss:     0.437
    # model.add(tf.keras.layers.Dense(units=256, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.1)))
    # model.add(tf.keras.layers.Dense(units=256, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.1)))
    # model.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

    # # mean_accuracy: 64.250
    # # mean_loss:     1.790
    # model.add(tf.keras.layers.Dense(units=256, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.1)))
    # model.add(tf.keras.layers.Dense(units=256, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.1)))
    # model.add(tf.keras.layers.Dense(units=128, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.1)))
    # model.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

    # # mean_accuracy: 90.250
    # # mean_loss:     0.573
    # model.add(tf.keras.layers.Dense(units=256, activation='relu'))
    # model.add(tf.keras.layers.Dense(units=256, activation='relu'))
    # model.add(tf.keras.layers.Dense(units=128, activation='relu'))
    # model.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

    # mean_accuracy: 90.250
    # mean_loss:     0.437
    model.add(tf.keras.layers.Dense(units=16, activation='relu'))
    model.add(tf.keras.layers.Dense(units=16, activation='relu'))
    model.add(tf.keras.layers.Dense(units=8, activation='relu'))
    model.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

    # # mean_accuracy:  89.66
    # # mean_loss:      0.327
    # model.add(tf.keras.layers.Dense(units=64, activation='relu'))
    # model.add(tf.keras.layers.Dense(units=64, activation='relu'))
    # model.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

    # # mean_accuracy:  90.667
    # # mean_loss:      0.290
    # model.add(tf.keras.layers.Dense(units=64, activation='relu'))
    # model.add(tf.keras.layers.Dense(units=64, activation='relu'))
    # model.add(tf.keras.layers.Dense(units=32, activation='relu'))
    # model.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

    # # mean_accuracy:  88.000
    # # mean_loss:      0.743
    # model.add(tf.keras.layers.Dense(units=64, activation='relu'))
    # model.add(tf.keras.layers.Dense(units=64, activation='relu'))
    # model.add(tf.keras.layers.Dense(units=32, activation='relu'))
    # model.add(tf.keras.layers.Dense(units=1, activation='linear'))

    model.compile(
      optimizer = tf.keras.optimizers.Adam(0.01),

      loss = tf.keras.losses.BinaryCrossentropy(),
      # loss = tf.keras.losses.BinaryFocalCrossentropy(),
      # loss = tf.keras.losses.Huber(),

      metrics = ['accuracy']
      # metrics = ['mean_absolute_error']
    )
    # model.summary()

    early_stopping = tf.keras.callbacks.EarlyStopping(
      # monitor='val_loss',
      monitor='accuracy',

      # how much stalled epoch do we wait before stopping
      patience=100,

      restore_best_weights=True,
      verbose=1
    )

    total_epoch = 300

    best_model_filepath = f"{_get_current_folder()}/best_model---fold-no-{fold_no}.keras"

    checkpoint = tf.keras.callbacks.ModelCheckpoint(
      best_model_filepath,  # Path to save the best model
      # monitor='val_loss',   # Metric to monitor
      # mode='min',           # Mode for the monitored metric ('min' for loss, 'max' for accuracy)
      monitor='val_accuracy',   # Metric to monitor
      mode='max',           # Mode for the monitored metric ('min' for loss, 'max' for accuracy)
      save_best_only=True,  # Only save if the monitored metric improves
      verbose=0
    )

    class my_log_callback(tf.keras.callbacks.Callback):

      def on_epoch_end(self, epoch, logs=None):
        # print every 10 epochs
        if ((epoch % 10) == 0):

          msg = ""
          msg += f"\r -> {epoch}/{total_epoch}"
          msg += f", loss={logs['loss']:3.3f}"
          msg += f", accuracy={logs['accuracy'] * 100:3.3f}%"

          print(msg, end="")

      def on_train_end(self, logs=None):

        msg = ""
        # msg += f"\r -> {epoch}/{total_epoch}"
        msg += f", loss={logs['loss']:3.3f}"
        msg += f", accuracy={logs['accuracy'] * 100:3.3f}%"

        print(msg)

    print('------------------------------------------------------------------------')
    print(f'Training for fold {fold_no} ...')

    model.fit(
      X_train,
      y_train,
      epochs = total_epoch,
      batch_size = 16,
      validation_data=(X_test, y_test),
      callbacks=[my_log_callback(), checkpoint, early_stopping],
      verbose=0
    )

    scores = model.evaluate(X_test, y_test, verbose=0)

    loss_metric = scores[0]
    accuracy_metric = scores[1] * 100

    print(f'Score for fold {fold_no}: loss={loss_metric:.3f}, accuracy={accuracy_metric:.3f}%')

    acc_per_fold.append(accuracy_metric)
    loss_per_fold.append(loss_metric)

    fold_no += 1

  print(f"Accuracy (higher is better):          {np.mean(acc_per_fold):.3f}%")
  print(f"Standard Deviation (lower is better): {np.std(acc_per_fold):.3f}%")
  print(f"Loss (lower is better):               {np.mean(loss_per_fold):.3f}")


