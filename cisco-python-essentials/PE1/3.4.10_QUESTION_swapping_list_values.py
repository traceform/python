# Imagine that you need to rearrange the elements of a list,
# i.e., reverse the order of the elements: the first and the
# fifth as well as the second and fourth elements will be swapped. The third one will remain untouched.
#
# Question: how can you swap the values of two variables?

list = [1, 2, 3, 4, 5]

list[0], list[4] = list[4], list[0]
list[1], list[3] = list[3], list[1]

print(list)
