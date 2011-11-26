from numpy import *

def ex_1():
  U,Sigma,Vt = linalg.svd([[1,1],[1,7]])
  print "U ="
  print U
  print "Sigma ="
  print Sigma
  print "Vt ="
  print Vt

def ex_2():
  data = [[1,1,1,0,0],
         [2,2,2,0,0],
         [1,1,1,0,0],
         [5,5,5,0,0],
         [1,1,0,2,2],
         [0,0,0,3,3],
         [0,0,0,1,1]]
  U,Sigma,VT = linalg.svd(data)
  print Sigma
  print "***"
  Sig3 = mat([[Sigma[0],0,0],[0,Sigma[1],0],[0,0,Sigma[2]]])
  print U[:,:3]*Sig3*VT[:3,:]
  
if __name__ == "__main__":
  ex_2()