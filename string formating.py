name = "Akash"
dept = "Information Technology"

# 1. using % operator
print("My name is %s and my department is %s" % (name, dept))
# Output: My name is Akash and my department is Information Technology

# 2. Using str.format() method
print("My name is {} and my department is {}".format(name, dept))
# Output: My name is Akash and my department is Information Technology

# 3. Named arguments
print("My name is {n} and my department is {d}".format(n=name, d=dept))
# Output: My name is Akash and my department is Information Technology

# 4. f-strings
print(f"My name is {name} and my department is {dept}")
# Output: My name is Akash and my department is Information Technology

print(f"{name} studies in {dept.upper()}")
# Output: Akash studies in INFORMATION TECHNOLOGY
