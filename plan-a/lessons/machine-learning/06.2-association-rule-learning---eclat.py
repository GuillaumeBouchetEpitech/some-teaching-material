
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

transactions: list[list[str]] = []
for row in range(0, 7501):
  transactions.append([str(dataset.values[row,col]) for col in range(0, 20)])

from apyori import apriori, RelationRecord
rules = apriori(transactions = transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 2)

results = list(rules)

print(results)

#
#
#
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE

def inspect(results: list[RelationRecord]) -> list[tuple]:
  prod1       = [tuple(result[2][0][0])[0] for result in results]
  prod2       = [tuple(result[2][0][1])[0] for result in results]
  supports    = [result[1] for result in results]
  return list(zip(prod1, prod2, supports))

resultsInDataFrame = pd.DataFrame(inspect(results), columns = ['Product 1', 'Product 2', 'Support'])

# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
#
#
#

print()
print("#")
print("#")
print()
print("## UNSORTED ##")
print()
print(resultsInDataFrame)

print()
print()
print("## SORTED ##")
print()
print(resultsInDataFrame.nlargest(n = 10, columns = 'Support'))
print()
print("#")
print("#")
print()
