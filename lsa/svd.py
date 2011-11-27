# http://www.puffinwarellc.com/index.php/news-and-articles/articles/30-singular-value-decomposition-tutorial.html

# Singular Value Decomposition is a way of factoring matrices into a series of linear approximations that expose the underlying structure of the matrix.
from numpy import *

def loadData():
  return [[4,4,4],
          [5,5,5],
          [3,3,3],
          [4,4,4],
          [4,4,4],
          [4,4,4],
          [4,4,4],
          [3,3,3],
          [5,5,5]]

def loadData2():
  A = [[4,4,5],
       [4,5,5],
       [3,3,2],
       [4,5,4],
       [4,4,4],
       [3,5,4],
       [4,4,3],
       [2,4,4],
       [5,5,5]]
  return matrix(A)

if __name__ == '__main__':
  #data = loadData()
  data = loadData2()
  #print data.shape
  U,Sig,VT = linalg.svd(data,full_matrices=True)
  print U.shape
  S = matrix([[Sig[0],0,0],[0,Sig[1],0],[0,0,Sig[2]],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]])
  # not quite there
  #S = matrix([[Sig[0],0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]])
  print S.shape
  print VT.shape
  print U*S*VT # should get back A
