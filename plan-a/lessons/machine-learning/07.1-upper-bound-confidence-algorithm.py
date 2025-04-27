
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

csv_filepath = f"{_get_current_folder()}/07-upper-bound-confidence-algorithm-data.csv"

dataset = pd.read_csv(csv_filepath)

#
#
#

import math
# total_rows = 500 # not enough rows
total_rows = 10000 # proper number of rows
total_columns = 10 # 10 ads
all_selected_ads: list[int] = []
numbers_of_selections: list[int] = [0] * total_columns
sums_of_rewards: list[int] = [0] * total_columns
# total_reward: int = 0
for row_index in range(0, total_rows):

  # determine the best ad index for this row
  best_ad_index: int = 0

  max_upper_bound: float = 0.0
  for col_index in range(0, total_columns):

    if (numbers_of_selections[col_index] > 0):
      # ad selected more than once -> calculate the current upper bound

      # average reward
      average_reward = sums_of_rewards[col_index] / numbers_of_selections[col_index]

      # confidence interval
      confidence_interval = math.sqrt(3/2 * math.log(row_index + 1) / numbers_of_selections[col_index])

      # actual upper bound
      upper_bound = average_reward + confidence_interval

    else:
      # ad selected for the first time -> start low
      upper_bound = 1e400

    # update the best ad for this row
    if (upper_bound > max_upper_bound):
      max_upper_bound = upper_bound
      best_ad_index = col_index

  all_selected_ads.append(best_ad_index)
  numbers_of_selections[best_ad_index] = numbers_of_selections[best_ad_index] + 1
  reward = dataset.values[row_index, best_ad_index]
  sums_of_rewards[best_ad_index] = sums_of_rewards[best_ad_index] + reward
  # total_reward = total_reward + reward

#
#
#

plt.hist(all_selected_ads)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show(block=True)
