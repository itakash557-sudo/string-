name = "akash it"

# len(): returns the length of the string
print(len(name))          # Output: 8

# upper(): converts the string into uppercase
print(name.upper())       # Output: AKASH IT

# lower(): converts the string into lowercase
print(name.lower())       # Output: akash it

# capitalize(): makes only the first character uppercase
print(name.capitalize())  # Output: Akash it

# title(): makes the first letter of each word uppercase
print(name.title())       # Output: Akash It

# isalnum(): checks if string contains only alphabets and numbers (no spaces/symbols)
print(name.isalnum())     # Output: False   (because space is there)

# isalpha(): checks if string contains only alphabets
print(name.isalpha())     # Output: False   (because space is there)

# isascii(): checks if all characters are ASCII
print(name.isascii())     # Output: True

# isdecimal(): checks if string has only decimal digits (0–9)
print(name.isdecimal())   # Output: False

# isdigit(): checks if string has only digits (0–9, includes Unicode digits)
print(name.isdigit())     # Output: False

# islower(): checks if all characters are lowercase
print(name.islower())     # Output: True

# isupper(): checks if all characters are uppercase
print(name.isupper())     # Output: False

# isspace(): checks if string has only whitespace
print(name.isspace())     # Output: False

# swapcase(): swaps lowercase to uppercase and vice versa
print(name.swapcase())    # Output: AKASH IT

# split(): splits string into list based on separator
print(name.split('a'))    # Output: ['', 'k', 'sh it']  (splits wherever "a" comes)

# startswith(): checks if string starts with given substring
print(name.startswith("a"))  # Output: True

# endswith(): checks if string ends with given substring
print(name.endswith("02"))   # Output: False

# find(): returns first index of substring, or -1 if not found
print(name.find("it"))    # Output: 6

# count(): counts occurrences of substring/character
print(name.count("a"))    # Output: 2

# replace(): replaces substring with another
print(name.replace("s", "it")) # Output: akait it
