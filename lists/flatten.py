# http://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python
numbers = [[1], [2], [3], [4, 5, 6]]
print [item for sublist in numbers for item in sublist]