name = "Snehal IBM Angular"
print("First Char is: ",name[0])
print("Last Char is: ",name[len(name) - 1])
print("Length of name is: ",len(name))
print("Hello" + " " + "World" )

text = "Python Programming"
print(text[0:6])
print(text[-6:])
print(len(text))
print(text[::2])
print(text[::-1])

program = " i love python programming "
print(program.strip());
print(program.title().strip())
print(program.count('o'))
text = "123abc"
print(text.isalnum())
name = "John"
age = 25
print(f"My name is {name} and I am {age} years old.")

sentence = "Coding in Python is fun"
print(sentence.replace("fun","awesome"))
print(sentence.index("Python"))
print(sentence.upper())

# user_input=input("Enter string for palindrome: ")
# if user_input == user_input[::-1]:
#     print("String is palindrome")
# else:
#     print("String is not palindrome")
    
s = "Python is the best"
vowels = {'a','e','i','o','u','A','E','I','O','U'}
c = sum(1 for ch in s if ch in vowels)
print("Number of vowels:", c)
