# 10.⁠ ⁠Write a python function that checks weather a passed string is a palindrome or not
def is_palindrome(input_string):
    clean = ""
    for char in input_string:
        if char.isalnum():
            clean += char.lower()
    return clean == clean[::-1]

str1 = str(input("Enter string: "))
result = is_palindrome(str1)
print(f'"{str1}" is a palindrome: {result}')