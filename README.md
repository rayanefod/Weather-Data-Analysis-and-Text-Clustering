# Weather-Data-Analysis-and-Text-Clustering

This repository contains two projects:

1. Weather Data Analysis using MapReduce
2. Text Clustering with Apache Mahout

## Weather Data Analysis
This project focuses on analyzing weather data from the National Climatic Data Center (NCDC) for the year 2007. The goal is to calculate the following descriptive statistics for each day of the month, using MapReduce framework in Python:

- Difference between the maximum and minimum wind speed from all weather stations
- Daily minimum relative humidity from all weather stations
- Daily mean and variance of dew point temperature from all weather stations
- Monthly correlation matrix among relative humidity, wind speed, and dry bulb temperature from all weather stations

The repository includes the following files for this project:

- Pseudocode for mapper and reducer functions
- Python implementation of mapper and reducer functions
- Instructions on how to run the code and reproduce the results


## Text Clustering with Apache Mahout
This project involves performing cluster analysis on a text dataset using Apache Mahout. The provided dataset consists of text files, which can also be replaced with a custom dataset. The project includes the following tasks:

- Implementing K-Means clustering algorithm with Euclidean and Manhattan distance measures
- Finding the optimum number of clusters (K) for K-Means clustering
- Implementing K-Means clustering algorithm with Cosine distance measure
- Verifying the relation between the average distance to the centroid and the K value
- Plotting the elbow graph for K-Means clustering with Cosine measure and smoothing the graph to explain the best value for K
- Comparing the different clusters obtained with different distance measures and discussing the best setting for K-Means clustering for the dataset

The repository includes the following files for this project:

- Code implementation of the K-Means clustering algorithm with different distance measures
- Summary of the impact of parameter changes on the performance of the K-Means algorithm
