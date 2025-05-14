
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


csv_filepath = f"{_get_current_folder()}/../assets/Netflix Life Impact Dataset (NLID).csv"

import pandas as pd

# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.countplot(x='Genre', data=df, color='red')
# # sns.countplot(x='How Discovered', data=df, color='red')
# plt.xticks(rotation=45)
# plt.title('Frequency of Genres')
# plt.show(block=True)

df = pd.read_csv(csv_filepath)


from pre_process import pre_process

X, y = pre_process(df)

# X_my_test = pre_process(df[:1])

# print(type(df[:1]))

# print(df[:1].to_string())

# X_raw = pre_process(df.iloc[1:])

# import sys
# sys.exit(0)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


def get_or_create_ann_from_file():

  X_train_dense = X_train.toarray()
  X_test_dense = X_test.toarray()
  input_dim = X_train.shape[1]

  from pathlib import Path

  model_filepath = f"{_get_current_folder()}/../assets/mode.keras"

  import tensorflow as tf

  my_file = Path(model_filepath)
  if my_file.exists() and my_file.is_file():

    print("model file was found")
    print("reusing previously trained model")

    return tf.keras.models.load_model(model_filepath)

  print("model file was not found")
  print("training new model")

  ann = tf.keras.models.Sequential()
  ann.add(tf.keras.layers.Input(shape=(input_dim,)))

  # add 4 dense layer
  for i in range(0, 4):
    ann.add(tf.keras.layers.Dense(units=128, activation='relu'))
    ann.add(tf.keras.layers.Dropout(rate=0.3))

  # funnel previous layer of 128 to new layer of 64
  ann.add(tf.keras.layers.Dense(units=64, activation='relu'))
  ann.add(tf.keras.layers.Dropout(rate=0.3))

  # funnel previous layer of 64 to new layer of 1
  ann.add(tf.keras.layers.Dense(units=32, activation='relu'))
  ann.add(tf.keras.layers.Dropout(rate=0.3))

  # output layer of 1
  ann.add(tf.keras.layers.Dense(units=1, activation='relu'))

  ann.compile(

    optimizer='adam', # Adam algorithm
    # optimizer='sgd', # stochastic gradient descent

    loss='huber', # less sensitive to outlier values
    metrics=['mean_absolute_error']
  )
  ann.summary()

  epochs = 500

  early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss',

    # here "patience" is the same as "epoch"
    # -> we're just after the 'restore_best_weights' feature
    patience=epochs,

    restore_best_weights=True,
    verbose=1
  )

  history = ann.fit(
    X_train_dense, y_train,
    epochs=epochs,
    batch_size=40,
    validation_data=(X_test_dense, y_test),
    callbacks=[early_stopping],
    verbose=1
  )

  # Save the model
  ann.save(model_filepath)

  return ann

def ann_test():

  #
  #
  #
  # PREDICTION PREDICTION PREDICTION PREDICTION PREDICTION
  # PREDICTION PREDICTION PREDICTION PREDICTION PREDICTION
  # PREDICTION PREDICTION PREDICTION PREDICTION PREDICTION

  X_train_dense = X_train.toarray()
  X_test_dense = X_test.toarray()
  # input_dim = X_train.shape[1]

  ann = get_or_create_ann_from_file()

  # loss, mae = ann.evaluate(X_test_dense, y_test, verbose=1)
  y_pred = ann.predict(X_test_dense).flatten()

  from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

  print(f"Neural Network Test")
  mse = mean_squared_error(y_test, y_pred)
  print(f" -> MSE = {mse:.4f}")
  mae = mean_absolute_error(y_test, y_pred)
  print(f" -> MAE = {mae:.4f}")
  score = r2_score(y_test, y_pred)
  print(f' -> performance score (higher is better) {score}')


  print("--------------------------")

  limited_df = df.iloc[0:2, :] # all columns

  print(type(limited_df))
  print(limited_df)


  # X_raw, y_raw = pre_process(limited_df)

  # X_train2, X_test2, y_train2, y_test2 = train_test_split(X_raw, y_raw, test_size=0.0001, random_state=42)


  # print(f"X_train:       {type(X_train)}")
  # print(f"X_train_dense: {type(X_train_dense)}")
  # print(f"X_raw:         {type(X_raw)}")
  # print(f"X_train2:      {type(X_train2)}")

  # import numpy as np
  # print(f"X_raw:         {type(np.ndarray(X_raw))}")

  # print("X_raw", X_raw)
  # print("list(X_raw)", list(X_raw))

  # y_raw = ann.predict(X_raw.toarray()).flatten()
  # print(f' -> y_raw {y_raw}')




  # import matplotlib.pyplot as plt

  # plt.figure(figsize=(12, 8))
  # plt.subplot(1, 2, 1)
  # plt.plot(history.history['loss'], label='Training Loss')
  # plt.plot(history.history['val_loss'], label='Validation Loss')
  # plt.title('Neural Network Training & Validation Loss')
  # plt.xlabel('Epoch')
  # plt.ylabel('Loss')
  # plt.legend()
  # plt.tight_layout()
  # plt.show()

  # PREDICTION PREDICTION PREDICTION PREDICTION PREDICTION
  # PREDICTION PREDICTION PREDICTION PREDICTION PREDICTION
  # PREDICTION PREDICTION PREDICTION PREDICTION PREDICTION
  #
  #
  #

ann_test()








from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor

#
#
#
# PREDICTION PREDICTION PREDICTION PREDICTION PREDICTION
# PREDICTION PREDICTION PREDICTION PREDICTION PREDICTION
# PREDICTION PREDICTION PREDICTION PREDICTION PREDICTION

best_params_KNN = {'n_neighbors': [3, 5, 10, 20, 30, 50]}
KNN = GridSearchCV(estimator=KNeighborsRegressor(), param_grid=best_params_KNN, cv=5, scoring='neg_mean_absolute_error')

best_params_RFC = {'n_estimators': [10, 100, 200, 300]}
RFC = GridSearchCV(estimator=RandomForestRegressor(random_state=42), param_grid=best_params_RFC, cv=5, scoring='neg_mean_absolute_error')

LR = LinearRegression()


models = [
  (KNN, 'KNeighborsRegressor  '),
  (RFC, 'RandomForestRegressor'),
  (LR,  'LinearRegression     '),
]

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

for model, name in models:

  print(f'Model: {name}')

  model.fit(X_train, y_train)
  y_pred = model.predict(X_test)
  mse = mean_squared_error(y_test, y_pred)
  print(f' -> MSE = {mse:.4f}')
  mae = mean_absolute_error(y_test, y_pred)
  print(f' -> MAE = {mae:.4f}')
  score = r2_score(y_test, y_pred)
  print(f' -> performance score (higher is better) {score}')

# PREDICTION PREDICTION PREDICTION PREDICTION PREDICTION
# PREDICTION PREDICTION PREDICTION PREDICTION PREDICTION
# PREDICTION PREDICTION PREDICTION PREDICTION PREDICTION
#
#
#

