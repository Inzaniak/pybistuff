# This code only works in Power BI for the example dataset.
# 'dataset' holds the input data for this script
from sklearn.cluster import KMeans
import numpy as np
dataset['Attack Defense Cluster'] = KMeans(n_clusters=6).fit(dataset[['Attack','Defense']]).labels_
dataset['Attack Defense Both Cluster'] = KMeans(n_clusters=6).fit(dataset[['Attack','Defense','Sp. Attack','Sp. Defense']]).labels_