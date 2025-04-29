
import pandas as pd

def pre_process(df: pd.DataFrame):

  # remove any unwanted extra spaces
  df.columns = df.columns.str.strip()

  # print("df", df)
  # print(df.isnull().sum())

  #
  #
  #
  # PRE-PROCESS PRE-PROCESS PRE-PROCESS PRE-PROCESS PRE-PROCESS
  # PRE-PROCESS PRE-PROCESS PRE-PROCESS PRE-PROCESS PRE-PROCESS
  # PRE-PROCESS PRE-PROCESS PRE-PROCESS PRE-PROCESS PRE-PROCESS

  #
  #
  #
  # process the column "Review Highlights"

  import re
  import nltk
  from nltk.corpus import stopwords
  from nltk.stem import WordNetLemmatizer

  nltk.download('wordnet') # download only once
  nltk.download('stopwords') # download only once

  raw_text = df['Review Highlights'].astype(str)

  def remove_stopwords(text: str) -> str:
    stop_words: set[str] = set(stopwords.words('english'))
    good_words: list[str] = [word.lower() for word in str(text).split() if word.lower() not in stop_words]
    return " ".join(good_words)

  def sanitize_text(text: str) -> str:
    # remove any "no-word + space"
    text = re.sub(r'[^\w\s]', ' ', text)
    # remove all digits
    text = re.sub(r'\d+', ' ', text)
    # remove all extra spaces, only keep "in between words" spaces
    text = re.sub(r'\s+', ' ', text).strip()
    lemmatizer = WordNetLemmatizer()
    text = " ".join([lemmatizer.lemmatize(word) for word in text.split()])
    return text

  sanitized_text = raw_text.apply(remove_stopwords).apply(sanitize_text)

  # print(sanitized_text)

  from sklearn.feature_extraction.text import TfidfVectorizer

  vectorizer = TfidfVectorizer(max_features=5000)
  vector_text = vectorizer.fit_transform(sanitized_text)

  # print(vector_text)

  # process the column "Review Highlights"
  #
  #
  #


  from sklearn.preprocessing import StandardScaler

  scaler = StandardScaler()


  df['Suggested to Friends/Family'] = df['Suggested to Friends/Family (Y/N %)'].str.extract(r'(\d+)').astype(float)

  df_numerics = df[['Suggested to Friends/Family', 'Number of Reviews', 'Release Year']].fillna(0)
  numeric_features = scaler.fit_transform(df_numerics)



  from scipy.sparse import hstack

  X = hstack([vector_text, numeric_features])

  # print(X)



  y = df['Average Rating'].fillna(df['Average Rating'].mean())
  # y = df['Average Rating']

  # print(y)



  return X, y

