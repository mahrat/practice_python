# file handling practice

# writing to a file
with open("sample.txt", "w") as f:
    f.write("line 1\n")
    f.write("line 2\n")
    f.writelines(["line 3\n", "line 4\n"])

# reading whole file
with open("sample.txt", "r") as f:
    content = f.read()
print(content)

# reading line by line (better for big files, doesn't load everything at once)
with open("sample.txt", "r") as f:
    for line in f:
        print("line ->", line.strip())   # strip to remove the trailing \n

# readlines() gives a list of all lines
with open("sample.txt", "r") as f:
    lines = f.readlines()
print(lines)

# appending instead of overwriting - used "w" earlier which wipes the file, "a" adds to it
with open("sample.txt", "a") as f:
    f.write("line 5 (appended)\n")

with open("sample.txt", "r") as f:
    print(f.read())

# checking if file exists before doing stuff with it
import os
if os.path.exists("sample.txt"):
    print("file size in bytes:", os.path.getsize("sample.txt"))

# working with paths (os.path is fine, pathlib is the more modern way apparently)
from pathlib import Path

p = Path("sample.txt")
print(p.name)
print(p.suffix)
print(p.exists())
print(p.absolute())

# cleanup so this script is repeatable
os.remove("sample.txt")
print("cleaned up sample.txt")
