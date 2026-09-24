my_dict = {"a": 1}
print(my_dict)  # Output: {'a': 1}

# Add multiple items at once
my_dict.update({"b": 2, "c": 3})
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# Or using keyword arguments
my_dict.update(d=4, e=5)
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}