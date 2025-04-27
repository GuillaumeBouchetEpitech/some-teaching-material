
from pre_process import pre_process


X_train, X_test, y_train, y_test = pre_process()


def ann_test():

  #
  #
  #
  # PREDICTION PREDICTION PREDICTION PREDICTION PREDICTION
  # PREDICTION PREDICTION PREDICTION PREDICTION PREDICTION
  # PREDICTION PREDICTION PREDICTION PREDICTION PREDICTION

  import tensorflow as tf

  X_train_dense = X_train.toarray()
  X_test_dense = X_test.toarray()
  input_dim = X_train.shape[1]

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

    # here "patience" = "epoch"
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

