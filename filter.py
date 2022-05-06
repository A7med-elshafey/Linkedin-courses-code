# define a set of items that we want to reduce duplicates
from unittest import result


items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# ok create a hashtable to perform a filter
filter = dict()

# ok loop over each item and add to the hashtable
for item in items:
    filter[item] = 0

# ok create a set from the resulting keys in the hashtable
result = set(filter.keys())
print(result)