# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page",
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access items
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# verify a key exists
print("guitar" in band)
print("Triangle" in band)

# Change values
band["vocals"] = "coverdale"
band.update({"bass": "JPJ"})

print(band)

# Remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())  # tupple
print(band)

# Delete and Clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# Coppying dictionaries

# band2 = band  # create a reference to band
# print("Bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

band2 = band.copy()  # create a copy of band
band2["drums"] = "Dave"
print("Good copy!")
print(band)
print(band2)

# or use the dict() constructor function

band3 = dict(band)
print("Good copy!")
print(band3)

# Nested dictionaries

member1 = {"name": "plant", "instrument": "vocals"}
member2 = {"name": "page", "instrument": "guitar"}

band = {"member1": member1, "member2": member2}

print(band)
print(band["member1"]["name"])

# Sets

nums = {
    1,
    2,
    3,
    4,
}

nums2 = set([1, 2, 3, 4])

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicates allowed
nums = {1, 2, 2, 3}
print(nums)

# True is a dupe of 1, False is a dupe of 0
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# Check if a value is in a set
print(2 in nums)

# but you cannot refere to an element in the set with an index or a key

# Add a new element to the set
nums.add(8)
print(nums)

# Add elements form one to another set
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# You can use update with lists, tuples, and dictionaries.

# Merge 2 sets to create a new set
one = {1, 2, 3}
two = {3, 4, 5}

mynewset = one.union(two)
print(mynewset)

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# Keep everything that is not a duplicate
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
