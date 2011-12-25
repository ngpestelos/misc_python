# From the LSA Paper
# Columns: c1, c2, c3, c4, c5, m1, m2, m3, m4
# Rows: human, interface, computer, user, system, response, time, EPS, survey, trees, graph, minors
#
# *** Documents ***
# c1: Human machine interface for ABC computer applications
# c2: A survey of user opinion of computer system response time
# c3: The EPS user interface management system
# c4: System and human system engineering testing of EPS
# c5: Relation of user perceived response time to error measurement
# m1: The generation of random, binary, ordered trees
# m2: The intersection graph of paths in trees
# m3: Graph minors IV: Widths of trees and well-quasi-ordering
# m4: Graph minors: A survey

from numpy import *
from nltk.cluster.util import *
from numpy.linalg import svd
import matplotlib.pyplot as plt

A = array([
  [1,0,0,1,0,0,0,0,0],
  [1,0,1,0,0,0,0,0,0],
  [0,1,1,0,1,0,0,0,0],
  [0,1,1,2,0,0,0,0,0],
  [0,1,0,0,1,0,0,0,0],
  [0,1,0,0,1,0,0,0,0],
  [0,0,1,1,0,0,0,0,0],
  [0,1,0,0,0,0,0,0,1],
  [0,0,0,0,0,1,1,1,0],
  [0,0,0,0,0,0,1,1,1],
  [0,0,0,0,0,0,0,1,1]
])

#print cosine_distance(A[:,8], A[:,6])
U,S,V = svd(A, full_matrices=False)

#C = zip(V[0,:], V[1,:])
#M = V[5:9,:]

# Create a set of 2D points from the sentences
#Points = V[0:2,:].T

# Create a M x N matrix where each row is the distance from each column
#A = array([[euclidean_distance(Points[i], Points[j]) for j in [5,6,7,8]] for i in [0,1,2,3,4]])

# Plot Points
#plt.plot(Points[:,0], Points[:,1], 'ro')
#plt.plot(Points[:,0], Points[:,1], 'ro')
#labels = ["c1", "c2", "c3", "c4", "c5", "m1", "m2", "m3", "m4"]
#for label, x, y in zip(labels, Points[:,0], Points[:,1]):
#  plt.annotate(label,
#    xy=(x,y), xytext=(-20,5), textcoords='offset points'
#  )
#plt.show()

# C1 vs M1
#P = array([V[0,0],V[1,0]])
#Q = array([V[0,5],V[1,5]])
#print euclidean_distance(P,Q)
#print euclidean_distance(Points[0],Points[5])

# C1 vs M2
#P = array([V[0,0],V[1,0]])
#Q = array([V[0,6],V[1,6]])
#print euclidean_distance(P,Q)

# C1 vs M3
#P = array([V[0,0],V[1,0]])
#Q = array([V[0,7],V[1,7]])
#print euclidean_distance(P,Q)

# C1 vs M4
#P = array([V[0,0],V[1,0]])
#Q = array([V[0,8],V[1,8]])
#print euclidean_distance(P,Q)

# Create a 5x4 matrix

#print P

#for i in range(C.shape[1]):
#  print "*** C%d ***" % (i + 1)
#  ci = C[:,i]
#  for j in range(M.shape[1]):
#    mj = M[:,j]
#    print cosine_distance(ci, mj)

#plt.plot(V[0,:], V[1,:], 'ro')
#labels = ["c1", "c2", "c3", "c4", "c5", "m1", "m2", "m3", "m4"]
#for label, x, y in zip(labels, V[0,:], V[1,:]):
#  plt.annotate(label,
#    xy=(x,y), xytext=(-20,5), textcoords='offset points'
#  )
#plt.show()

#################### Debug Here ####################

U2 = U[:,0:2]
S2 = S[0:2]
V2 = V[0:2,:]

A2 = dot(dot(U2,diag(S2)), V2)
print A2

# Plot V
#plt.plot(V[1,:], V[2,:], 'o')

#labels = ["c1", "c2", "c3", "c4", "c5", "m1", "m2", "m3", "m4"]
#for label, x, y in zip(labels, V[1,:], V[2,:]):
#  plt.annotate(label,
#    xy=(x,y), xytext=(-20,5), textcoords='offset points'
#  )

# Plot U
#plt.plot(U[:,1], U[:,2], 'ro')

# Split into two parts (C2 and M2)
#C2 = A2[:,0:5]
#M2 = A2[:,5:9]

# Compare distances for each column of C with each column of M
# A small score means the two vectors are close
#for i in range(C2.shape[1]):
#  print "*** C%d ***" % (i + 1)
#  ci = C2[:,i]
#  for j in range(M2.shape[1]):
#    mj = M2[:,j]
#    print cosine_distance(ci, mj)

#print "===="
#print cosine_distance(C2[:,0], M2[:,0])

#print euclidean_distance(array([0, 0]), array([1, 1])) # 1.41421356237 sqrt(2)

# Show plot
#plt.show()

#print M2
#print cosine_distance(M2[:,0], C2[:,0])

#plt.plot(U[:,0], U[:,1], 'o')
#plt.plot(U[:,1], U[:,2], 'o')
#labels = ["human", "interface", "computer", "user", "system", "response", "time", "EPS", "survey", "trees", "graph", "minors"]
#for label,x,y in zip(labels,U[:,1],U[:,2]):
#  plt.annotate(label,
#    xy=(x,y),
#    xytext=(-20,20),
#    textcoords='offset points',
#    ha='right',
#    va='bottom',
#    bbox=dict(boxstyle='round,pad=0.5',fc='yellow',alpha=0.5),
#    arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=0'))
#plt.show()