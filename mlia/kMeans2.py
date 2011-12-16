from numpy import *
from matplotlib import pyplot as plt

def euclidean(v1, v2):
  # as the crow flies
  return sqrt(sum(power(v1 - v2, 2)))
  
def pearson(v1, v2):
  # Simple sums
  sum1 = sum(v1)
  sum2 = sum(v2)

  # Sums of the squares
  sum1Sq = sum([pow(v,2) for v in v1])
  sum2Sq = sum([pow(v,2) for v in v2])

  # Sum of the products
  pSum = sum([v1[i] * v2[i] for i in range(len(v1))])

  # Calculate r
  num = pSum - (sum1 * sum2 / len(v1))
  den = sqrt((sum1Sq - pow(sum1, 2) / len(v1)) * (sum2Sq - pow(sum2, 2) / len(v1)))
  if den == 0: return 0

  return 1.0 - num / den

def randomCentroids(dataSet, k):
  #n = shape(dataSet)[1]
  n = 2
  centroids = mat(zeros((k,n)))
  for j in range(n): # for each column
    minJ = min(dataSet[:,j]) # pick the smallest
    rangeJ = float(max(dataSet[:,j]) - minJ) # max - min
    centroids[:,j] = minJ + rangeJ * random.rand(k, 1) # n random numbers within range
  return centroids

def kMeans(dataSet, k, distMeas=euclidean, createCentroids=randomCentroids):
  m = shape(dataSet)[0] # number of points in the data set
  #print m
  clusterAssignment = mat(zeros((m,2)))
  centroids = createCentroids(dataSet, k) # random locations
  clusterChanged = True
  while clusterChanged:
    clusterChanged = False
    for i in range(m): # for each point
      minDist = inf; minIndex = -1
      for j in range(k): # for each centroid, compute the distance bet each point (m x k)
        distJI = distMeas(centroids[j,:], dataSet[i,:]) # centroids[j,:] is a random point
        if distJI < minDist:
          minDist = distJI; minIndex = j # save min distance and index (j = current centroid)
      if clusterAssignment[i,0] != minIndex: clusterChanged = True # re-positioned
      clusterAssignment[i,:] = minIndex,minDist ** 2 # (centroid id, distance from centroid)

    for cent in range(k):
      # compute the mean point for each cluster
      pointsIndices = nonzero(clusterAssignment[:,0].A == cent)[0]
      pointsInCluster = dataSet[pointsIndices]
      centroids[cent,:] = mean(pointsInCluster, axis=0) # re-align centroid based on mean points in the cluster

  return centroids, clusterAssignment
  
def ptsInCluster(dataSet, clusterAssignment, clustid):
  print "Cluster %d" % clustid
  indices = nonzero(clusterAssignment[:,0].A == clustid)[0]
  return dataSet[indices]

if __name__ == "__main__":
  k = 4
  dataMat = []
  #fr = open("testSet-mini.txt")
  fr = open("testSet.txt")
  for line in fr.readlines():
    curLine = line.strip().split('\t')
    fltLine = map(float, curLine)
    dataMat.append(fltLine)
  
  dataSet = mat(dataMat)
  centroids, clusterAssignment = kMeans(dataSet, k)
  print euclidean(centroids[0].A, centroids[0].A)
  print euclidean(centroids[0].A, centroids[1].A)
  print euclidean(centroids[0].A, centroids[2].A)
  print euclidean(centroids[0].A, centroids[3].A)
  print centroids
  
  plt.plot(centroids[:,0], centroids[:,1], 'o')
  plt.show()
  #for cent in range(k):
  #print ptsInCluster(dataSet, clusterAssignment, 0)
  #print ptsInCluster(dataSet, clusterAssignment, 1)
  #print ptsInCluster(dataSet, clusterAssignment, 2)