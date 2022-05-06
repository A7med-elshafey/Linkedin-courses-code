# ok create a hashtable all at once

items1 = dict({"key1" : 1, "key2" : 2, "key3": 'three'})
print(items1)

# ok: create a hashtable progressively
items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3
items2["key4"] = 4
print(items2)

# ok: try to access a nonexistent key
# print(items2["key2"])

# ok: replace an item
items2["key2"] = "two"
print(items2)

# ok: iterate the keys and values in the dictionary
for key ,value in items2.items():
    print("key: ", key, "value :", value)
