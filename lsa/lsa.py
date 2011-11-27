# http://www.puffinwarellc.com/index.php/news-and-articles/articles/33.html

from numpy import *
from numpy import linalg
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def loadData():
  """
  Rows: words (11)
  Columns: titles (9)
  """
  A = [[0,0,1,1,0,0,0,0,0],
       [0,0,0,0,0,1,0,0,1],
       [0,1,0,0,0,0,0,1,0],
       [0,0,0,0,0,0,1,0,1],
       [1,0,0,0,0,1,0,0,0],
       [1,1,1,1,1,1,1,1,1],
       [1,0,1,0,0,0,0,0,0],
       [0,0,0,0,0,0,1,0,1],
       [0,0,0,0,0,2,0,0,1],
       [1,0,1,0,0,0,0,1,0],
       [0,0,0,1,1,0,0,0,0]]
  labels = ['book','dads','dummies','estate','guide','investing','market','real','rich','stock','value']
  titles = ['T1','T2','T3','T4','T5','T6','T7','T8','T9']
  return mat(A), labels

if __name__ == "__main__":
  A, labels = loadData()
  print A.shape
  U,Sig,VT = linalg.svd(A)
  #print U.shape
  #print Sig.shape
  #print VT.shape
  #SigSq = Sig ** 2
  #print sum(SigSq) * 0.9
  #print sum(SigSq[:5])
  #print U
  #print U[:,:1]
  #print U[:,:5]
  #S = eye(9) * Sig[:9]
  #Xform = U[:,:9] * S * VT[:9,:]
  #print -1.0*Xform
  
  points = -1*U[:, 0:3]
  
  plt.plot(points[:,1], points[:,2], 'o')

  for label,x,y in zip(labels,points[:,1],points[:,2]):
    plt.annotate(label,
      xy=(x,y),
      xytext=(-20,20),
      textcoords='offset points',
      ha='right',
      va='bottom',
      bbox=dict(boxstyle='round,pad=0.5',fc='yellow',alpha=0.5),
      arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=0'))

  points = -1*VT[0:3,:]

  plt.plot(points[1,:], points[2,:], 'ro')
 
  plt.show()

  #print Sig[:3]
  
  #Sig3 = mat([[Sigma[0],0,0],[0,Sigma[1],0],[0,0,Sigma[2]]])
    #print U[:,:3]*Sig3*VT[:3,:]
  
  #print U
  #print Sig
  #print VT
  #print -1.52835558e-01 * 3.90941804 * -0.35383506

  
  #B = zeros((1,2), float)
  #C = append(B, [1,1])
  #print C
