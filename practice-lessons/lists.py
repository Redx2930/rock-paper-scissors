users = ["Dave", "John", "Sara"]

data = ["dave", 42, True]

emptylist = []

print("Dave" in users)

print(users[0])
print(users[-1])

print(users.index("Sara"))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append("Tom")
print(users)

users += ["Jason"]
print(users)

users.extend(["Mike", "Emily"])
print(users)

# users.extend(data)
# print(users)

users.insert(0, "Alice")
print(users)

users[2:2] = ["Bob", "Charlie"]
print(users)

users[1:3] = ["Eve", "Frank"]
print(users)

users.remove("Sara")
print(users)

print(users.pop())

del users[0]
print(users)

# del data
# print(data)

data.clear()
print(data)

users.sort()
print(users)

users[2:4] = ["dave"]
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)

# Tuples

mytuple = tuple(("Dave", 42, True))

anothertuple = ("Sara", 3.14, False, 2)

print(mytuple)
print(type(anothertuple))
print(type(mytuple))

newlist = list(mytuple)
newlist.append("John")
newtuple = tuple(newlist)
print(newtuple)

one, *two, hey = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))
