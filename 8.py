#  8.⁠ ⁠Write a python function that accepts a string and counts the number of upper and lower case letters
def counter(strin):
    lowcount=0
    upcount=0
    for char in strin:
        if char.islower():
            lowcount+=1
        else:
            upcount+=1
    return lowcount, upcount

str1=input('Enter string:')
print(counter(str1))