import numpy

# adds two vectors using Python lists
def pythonsum(n):
  a = range(n)
  b = range(n)
  c = []
  for i in range(len(a)):
    a[i] = i ** 2
    b[i] = i ** 3
    c.append(a[i] + b[i])
  return c

# adds two vectors using NumPy arrays
def numpysum(n):
  a = numpy.arange(n) ** 2
  b = numpy.arange(n) ** 3
  c = a + b # look ma, no for loop!
  return c

if __name__ == "__main__":
  print pythonsum(5)
  print numpysum(5)