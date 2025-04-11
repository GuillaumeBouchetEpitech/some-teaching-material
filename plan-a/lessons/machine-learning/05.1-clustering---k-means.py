
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

# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
wcss = [] # Within Cluster Sum of Squares -> WCSS
for i in range(1, 11):

  kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)

  # training phase
  kmeans.fit(X)

  # save the wcss value
  wcss.append(kmeans.inertia_)

#
#
#

# render optimal number of clusters
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('Within Cluster Sum of Squares (WCSS)')
plt.show(block=True) # <- force the window to open and stay open

# the graph showed us that the WCSS start dropping significantly
# faster at around 5 clusters -> we'll assume 5 clusters
best_total_clusters = 5

#
#
#

# training phase
kmeans = KMeans(n_clusters = best_total_clusters, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(X)

#
#
#

all_colors = ['red', 'brown', 'blue', 'green', 'cyan', 'magenta']

# render clusters
for ii in range(0, best_total_clusters):

  curr_color = all_colors[ii % len(all_colors)]

  all_pos_x = X[y_kmeans == ii, 0]
  all_pos_y = X[y_kmeans == ii, 1]

  plt.scatter(all_pos_x, all_pos_y, s = 50, c = curr_color, label = f'Cluster {ii}')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = '#888800', label = 'Centroids')

plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show(block=True) # <- force the window to open and stay open
