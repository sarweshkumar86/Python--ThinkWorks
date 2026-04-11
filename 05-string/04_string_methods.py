# Q. What will be the output of the following Python code?


s = "hello world"

print(s.upper())      # HELLO WORLD → converts all to uppercase
print(s.lower())      # hello world → converts all to lowercase
print(s.capitalize()) # Hello world → first letter capital
print(s.title())      # Hello World → first letter of each word capital

print('...........................end...............................')

text = " \nhello world "

print(text.strip())   # hello world → removes spaces + newline from both sides
print(text.lstrip())  # hello world  → removes spaces + newline from left side only
print(text.rstrip())  #  \nhello world → removes spaces from right side only

print('...........................end...............................')

text = "Python is fun and fun and fun"

print(text.find("is"))  
# 7 → returns index of first occurrence of "is"
print(text.replace("fun", "awesome"))  
# replaces all "fun" with "awesome"

print('...........................end...............................')



