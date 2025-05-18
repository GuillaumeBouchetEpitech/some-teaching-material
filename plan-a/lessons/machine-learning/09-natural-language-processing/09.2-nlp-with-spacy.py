
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

corpus: list[str] = []
output: list[int] = []

import spacy

# Define language model
# -> must run -> python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")

for i in range(0, total_rows):

  review = dataset['Review'][i]

  doc = nlp(review)

  tokens_filtrered = []

  for token in doc:
    if token.is_stop or token.is_punct:
      continue

    tokens_filtrered.append(token.lemma_)

  review = " ".join(tokens_filtrered)

  # skip empty reviews
  if (len(review) == 0):
    continue

  corpus.append(review)
  output.append(dataset['Liked'][i])

print("len(corpus)", len(corpus))

import numpy as np

X = np.array(corpus)
y = np.array(output)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

bag_of_word_size = 1500

from sklearn.feature_extraction.text import TfidfVectorizer
cv = TfidfVectorizer(max_features=bag_of_word_size, ngram_range=(1, 2))
X_train = cv.fit_transform(X_train).toarray()
X_test = cv.transform(X_test).toarray()

print("X.shape", X.shape)


X_train_dense = X_train
X_test_dense = X_test


# Training the Naive Bayes model on the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)


y_pred = classifier.predict(X_test)

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
  y_raw = classifier.predict(X_raw)
  y_raw = (y_raw >= 0.5)

  print(f"#################################################")
  print(f" -> custom sentence    -> '{sentence}'")
  print(f" ---> did they like it -> {y_raw[0]}")
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
