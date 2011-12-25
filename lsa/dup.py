# Duplicate case (same sentence)
# a1: Japanese man's focus on Roger's interest from his visit.
# k1: Japanese man's focus on Roger's interest from his visit.
# Show that points map on the same space

from numpy import *
from nltk.cluster.util import *
from numpy.linalg import svd, norm
import matplotlib.pyplot as plt
from math import acos

A = array([
  [1,1],
  [1,1],
  [1,1],
  [1,1],
  [1,1],
  [1,1]
])

U,S,V = svd(A, full_matrices=False)

U2 = U[:,0:2]
S2 = S[0:2]
V2 = V[0:2,:]

A2 = dot(dot(U2,diag(S2)), V2)
print A2[:,0]
print A2[:,1]

def cosine_similarity(a, b):
  return dot(a, b) / (norm(a) * norm(b))
  
print cosine_similarity(A2[:,0], A2[:,1])

#print dot(A2[:,0], A2[:,0]) / norm(A2[:,0]) * norm(A2[:,1])
#print cosine_distance([1,2],[1,2])
#print dot(A2[:,0], A2[:,1])

#print A2