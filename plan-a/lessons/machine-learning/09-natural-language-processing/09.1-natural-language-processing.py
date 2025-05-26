
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

csv_filepath = f"{_get_current_folder()}/09-natural-language-processing-data.csv"

dataset = pd.read_csv(csv_filepath, delimiter = '\t', quoting = 3)

total_rows = dataset.shape[0]
print(f"total_rows {total_rows}")


import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet') # downloaded only once
nltk.download('stopwords') # downloaded only once

corpus: list[str] = []

all_stopwords = stopwords.words('english')
# keep the 'not' stopword out of the list of words to remove
all_stopwords.remove('not')
# keep it as a set[str]
all_stopwords = set(all_stopwords)

# # suffix removal (Porter stemming algorithm)
# # stemming : A process for removing the inflexional, and sometimes derivational, affixes from words.
# # ex: lets -> let
# porter_stemmer = PorterStemmer()

# a lemmatizer will returns the shortest lemma for a word
# ex: "churches" -> "church"
lemmatizer = WordNetLemmatizer()

for i in range(0, total_rows):

  review = dataset['Review'][i]

  # replace any non-letter character by a space character
  # ex: "Let's go to churches" -> "Lets go to churches"
  review = re.sub('[^a-zA-Z]', ' ', review)

  # lower case only
  # ex: "Lets go to churches" -> "lets go to churches"
  review = review.lower()

  # as list of words -> list[str]
  # ex: "lets go to churches" -> ["lets", "go", "to", "churches"]
  review = review.split()

  # # suffix removal (Porter stemming algorithm)
  # # ex: ["lets", "go", "to", "churches"] -> ["let", "go", "to", "churches"]
  # review = [porter_stemmer.stem(word) for word in review if not word in set(all_stopwords)]

  # lemmatize the words -> ensure the shortest "lemma" for a word
  #  a "lemma" is the canonical form of a word
  # ex: ["lets", "go", "to", "churches"] -> ["let", "go", "to", "church"]
  review = [lemmatizer.lemmatize(word) for word in review]

  # make the list of words a string of words
  # ex: ["let", "go", "to", "churches"] -> "let go to churches"
  review = ' '.join(review)

  corpus.append(review)

# print("corpus", corpus)
print("len(corpus)", len(corpus))

# keep the 1500 most use words as part of the "bag of words"
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, -1].values

print("X.shape", X.shape)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)





X_train_dense = X_train
X_test_dense = X_test


model_filepath = f"{_get_current_folder()}/09.1.natural-language-processing-model.keras"

from pathlib import Path
import tensorflow as tf

model_file = Path(model_filepath)
if model_file.exists() and model_file.is_file():

  print("model file was found")
  print("reusing previously trained model")

  ann = tf.keras.models.load_model(model_filepath)
  ann.summary()

else:

  input_size = X_train.shape[1]

  ann = tf.keras.models.Sequential()
  ann.add(tf.keras.layers.Input(shape=(input_size,)))

  ann.add(tf.keras.layers.Dense(units=256, activation='relu'))
  ann.add(tf.keras.layers.Dense(units=256, activation='relu'))
  ann.add(tf.keras.layers.Dense(units=128, activation='relu'))
  ann.add(tf.keras.layers.Dense(units=64, activation='relu'))
  ann.add(tf.keras.layers.Dense(units=32, activation='relu'))

  # output layer of 1
  ann.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

  ann.compile(

    # optimizer='sgd', # stochastic gradient descent -> worst (max accuracy was 0.6)
    # optimizer=tf.keras.optimizers.Adam(0.01), # Adam algorithm -> best (max accuracy was 0.765)
    # optimizer=tf.keras.optimizers.Adam(), # Adam algorithm -> best (max accuracy was 0.765)
    optimizer='adamw',

    # loss='huber', # less sensitive to outlier values
    # loss='sparse_categorical_crossentropy', # less sensitive to outlier values
    loss='binary_crossentropy', # less sensitive to outlier values


    # metrics=['mean_absolute_error']
    metrics=['accuracy']
    # metrics=['accuracy', 'mean_absolute_error']

  )
  ann.summary()


  early_stopping = tf.keras.callbacks.EarlyStopping(
    # monitor='val_loss',
    monitor='val_accuracy',
    # monitor='accuracy',

    # here "patience" is the same as "epoch"
    # -> we're just after the 'restore_best_weights' feature
    patience=100,

    restore_best_weights=True,
    verbose=1
  )

  history = ann.fit(
    X_train_dense, y_train,
    epochs=300,
    batch_size=16,
    validation_data=(X_test_dense, y_test),
    callbacks=[early_stopping],
    verbose=1
  )

  # Save the model
  ann.save(model_filepath)


y_pred = ann.predict(X_test_dense, verbose=0)

# y_pred is of shape (200, 1) -> 2D matrix
y_pred = y_pred.flatten()
# y_pred is now of shape (200,) -> 1D array

y_pred = (y_pred >= 0.5)
# y_pred now an array of Boolean value (True/False)


from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)

print("confusion matrix prediction", cm)
print(f" -> did like")
print(f"   -> correct   {cm[0][0]}")
print(f"   -> incorrect {cm[1][0]}")
print(f" -> did not like")
print(f"   -> correct   {cm[1][1]}")
print(f"   -> incorrect {cm[0][1]}")


print("accuracy_score", accuracy_score(y_test, y_pred))


def _predict_my_sentence(sentence: str, expected: bool):

  # convert to the bag of words we trained
  X_raw = cv.transform([sentence]).toarray()
  # predict
  y_raw = ann.predict(X_raw, verbose=0)
  y_raw = (y_raw >= 0.5)

  print(f"#################################################")
  print(f" -> custom sentence    -> '{sentence}'")
  print(f" ---> did they like it -> {y_raw[0][0]}")
  if y_raw[0] == expected:
    print(f" ---> and we expected  -> {expected} -----> SUCCESS")
  else:
    print(f" ---> and we expected  -> {expected} -----> FAILURE")


all_custom_sentences: list[tuple[str, bool]] = []
all_custom_sentences.append(("the food was amazing", True))
all_custom_sentences.append(("the food was great", True))
all_custom_sentences.append(("the food was good", True))
all_custom_sentences.append(("slow service but great taste", True))
all_custom_sentences.append(("the food was bad", False))
all_custom_sentences.append(("I'll will not order from them again", False))
all_custom_sentences.append(("avoid that place", False))

for sentence in all_custom_sentences:
  _predict_my_sentence(sentence[0], sentence[1])


#
#
#

# Visualizing

import matplotlib.pyplot as plt
import seaborn as sns

fig, axs = plt.subplots(nrows = 1, ncols = 1, figsize = (10,4.2))

labels = ['like', 'dislike']
sns.heatmap(cm, cmap = 'Reds',
            annot = True, annot_kws = {'fontweight':'bold'},
            fmt = " ", square = True, cbar = False,
            xticklabels = labels, yticklabels = labels, ax = axs)
axs.set_title("Confusion Matrix", fontsize = 12, fontweight = "bold", color = "black")

# plt.legend()
plt.show(block=True) # <- force the window to open and stay open
