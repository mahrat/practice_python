# lists practice

nums = [5, 3, 8, 1, 9, 2]

print(nums)
print(len(nums))

nums.append(10)
print(nums)

nums.remove(3)      # removes value 3, not index 3 (mixed this up before)
print(nums)

popped = nums.pop()  # removes last item by default
print("popped:", popped, nums)

nums.sort()
print("sorted:", nums)

nums.sort(reverse=True)
print("reverse sorted:", nums)

# slicing
print(nums[1:3])
print(nums[:2])
print(nums[-2:])

# list comprehension - still my favorite python feature tbh
squares = [n**2 for n in range(10)]
print(squares)

evens = [n for n in range(20) if n % 2 == 0]
print(evens)

# nested list comprehension (had to write this out on paper first time to get it)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)

# copying lists - this bit me hard once
original = [1, 2, 3]
bad_copy = original          # this is NOT a copy, just another reference
bad_copy.append(4)
print("original got changed too:", original)

good_copy = original.copy()  # or original[:] or list(original)
good_copy.append(99)
print("original:", original, "| good_copy:", good_copy)

# list as stack
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack.pop())  # 3, LIFO

# list unpacking
first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)

# checking membership
print(3 in [1, 2, 3])

# zip - combining two lists together, useful
names = ["a", "b", "c"]
scores = [90, 85, 70]
combined = list(zip(names, scores))
print(combined)
