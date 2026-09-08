# loops - for, while, break, continue

# basic for loop over range
for i in range(5):
    print(i)

print("---")

# range with start, stop, step
for i in range(2, 10, 2):
    print(i)

print("---")

# looping over a list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# enumerate when you need index too, better than range(len(fruits))
for idx, fruit in enumerate(fruits):
    print(idx, fruit)

# while loop
count = 0
while count < 5:
    print("count is", count)
    count += 1

# break example
for i in range(10):
    if i == 5:
        break
    print("break loop:", i)

# continue example
for i in range(10):
    if i % 2 == 0:
        continue
    print("odd number:", i)

# infinite loop with break (careful with these, almost froze my terminal once)
n = 0
while True:
    n += 1
    if n > 3:
        break
    print("infinite-ish loop:", n)

# nested loops - multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}", end="  ")
    print()  # newline after inner loop

# for-else (rarely used but good to know, else runs if loop completes without break)
for i in range(3):
    print("checking", i)
else:
    print("loop finished without break")
