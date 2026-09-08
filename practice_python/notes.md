# random notes to self

- mutable default args are a trap!! never use [] or {} as default param, use None then set inside
- f-strings > .format() > % formatting, just use f-strings always
- list comprehension is basically a for loop that returns a list, don't overdo nesting tho
- `is` checks identity, `==` checks value. for None always use `is None`
- shallow copy vs deep copy bit me once, use copy.deepcopy for nested stuff
- generators save memory bc lazy evaluation, yield instead of return
- decorators = functions that wrap other functions, still not 100% comfortable with these
- context managers (`with`) call __enter__ / __exit__, good for files/locks/db connections
- venv commands (keep forgetting these):
    python -m venv venv
    source venv/bin/activate   (mac/linux)
    venv\Scripts\activate      (windows)
- remember: PEP8 -> 4 spaces, snake_case for vars/functions, PascalCase for classes

things to revisit later:
- asyncio, haven't touched it yet
- metaclasses (probably don't need these for a while)
- proper unit testing with pytest instead of print() debugging like a caveman
