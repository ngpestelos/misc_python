# merge two lists
A = [1, 2, 3]
B = [4, 5, 6]

print [item for sublist in zip(A, B) for item in sublist] # [1, 4, 2, 5, 3, 6]