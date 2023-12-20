def is_binary_string(input_string):
    for char in input_string:
        if char != '0' and char != '1':
            return False
    return True

user_input = input("Enter a string: ")

if is_binary_string(user_input):
    print("String is a binary string.")
else:
    print("String is not a binary string.")