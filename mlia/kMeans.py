from numpy import *
import matplotlib.pyplot as plt

def loadDataSet(filename):
  dataMat = []
  fr = open(filename)
  for line in fr.readlines():
    curLine = line.strip().split('\t')
    fltLine = map(float, curLine)
    dataMat.append(fltLine)
  return dataMat

def distEclud(vecA, vecB):
  return sqrt(sum(power(vecA - vecB, 2)))
  
def randCent(dataSet, k):
  n = shape(dataSet)[1]
  centroids = mat(zeros((k, n)))
  for j in range(n):
    minJ = min(dataSet[:,j])
    rangeJ = float(max(dataSet[:,j]) - minJ)
    centroids[:,j] = minJ + rangeJ * random.rand(k,1)
  return centroids

def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
  m = shape(dataSet)[0]
  clusterAssment = mat(zeros((m,2)))
  centroids = createCent(dataSet, k)
  clusterChanged = True
  while clusterChanged:
    clusterChanged = False
    for i in range(m):
      minDist = inf; minIndex = -1
      for j in range(k):
        distJI = distMeas(centroids[j,:], dataSet[i,:])
        if distJI < minDist:
          minDist = distJI; minIndex = j
      if clusterAssment[i,0] != minIndex: clusterChanged = True
      clusterAssment[i,:] = minIndex,minDist ** 2
    #print centroids
    for cent in range(k):
      ptsInClust = dataSet[nonzero(clusterAssment[:,0].A == cent)[0]]
      centroids[cent,:] = mean(ptsInClust, axis=0)
  return centroids, clusterAssment

def plot(centroids):
  plt.plot(centroids[:,0], centroids[], 'r--')
  plt.show()

def biKMeans(dataSet, k, distMeas=distEclud):
  return None

def geoGrab(stdAddress, city):
  return None

def massPlaceFind(fileName):
  return None

def distSLC(vecA, vecB):
  return None

def clusterClubs(numClust=5):
  return None