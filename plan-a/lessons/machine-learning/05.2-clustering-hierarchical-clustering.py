
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

# import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

csv_filepath = f"{_get_current_folder()}/05-clustering-data.csv"

dataset = pd.read_csv(csv_filepath)
X = dataset.iloc[:, [3, 4]].values # only keep the "Age" and "Annual Income (k$)"

#
#
#

import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distances')
plt.show()

# the graph showed us that 5 clusters is good enough -> we'll assume 5 clusters
best_total_clusters = 5

#
#
#

# training phase
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = best_total_clusters, linkage = 'ward')
y_hc = hc.fit_predict(X)

#
#
#

all_colors = ['red', 'brown', 'blue', 'green', 'cyan', 'magenta']

# render clusters
for ii in range(0, best_total_clusters):

  curr_color = all_colors[ii % len(all_colors)]

  all_pos_x = X[y_hc == ii, 0]
  all_pos_y = X[y_hc == ii, 1]

  plt.scatter(all_pos_x, all_pos_y, s = 50, c = curr_color, label = f'Cluster {ii}')

plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show(block=True) # <- force the window to open and stay open
