//palindrome program
name=input("enter the word:")
if name [::-1] == name:
  print("palindrome")
else:
  print("not a palindrome")

//count vowels and consonants

s = input("Enter a string: ")

vowels = "aeiou"
v_count = 0
c_count = 0

for ch in s.lower():
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1

print(f"Vowels = {v_count}, Consonants = {c_count}")




