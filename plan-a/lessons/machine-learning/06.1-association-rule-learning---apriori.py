
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

csv_filepath = f"{_get_current_folder()}/06-association-rule-learning-data.csv"

dataset = pd.read_csv(csv_filepath, header = None)
transactions = []
for i in range(0, 7501):
  transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

from apyori import apriori
rules = apriori(transactions = transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 2)

results = list(rules)

# print(results)

def inspect(results):
    lhs         = [tuple(result[2][0][0])[0] for result in results]
    rhs         = [tuple(result[2][0][1])[0] for result in results]
    supports    = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts       = [result[2][0][3] for result in results]
    return list(zip(lhs, rhs, supports, confidences, lifts))

resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['Product 1', 'Product 2', 'Support', 'Confidence', 'Lift'])

print()
print("#")
print("#")
print()
print("## UNSORTED ##")
print()
print(resultsinDataFrame)

print()
print()
print("## SORTED ##")
print()
print(resultsinDataFrame.nlargest(n = 10, columns = 'Lift'))
print()
print("#")
print("#")
print()
