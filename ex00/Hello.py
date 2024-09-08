ft_list = ["Hello", "World!"]
ft_tuple = ("Hello", "France!")
ft_set = {"Hello", "Paris!"}
ft_dict = {"Hello": "42Paris!"}

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

# These are different types of data structures : containers.
# A container is mutable as long as it has methods that modify its content
# - adds / deletes / modify an item. Mutable containers include dict,
# list, bytearray and set.
# Immutable containers include frozenset, tuple, string...
# An immutable object can’t be changed after it is created.
# Accessig item[x] in a tuple would raise TypeError: 'tuple' object does
# not support item assignment.
# Same for string TypeError: 'str' object does not support item assignment
