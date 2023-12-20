#9.⁠ ⁠Write a python function to check weather a number is perfect or not
def is_perfect_number(number):
    if number <= 0:
        return False
    divisors_sum = sum([divisor for divisor in range(1, number) if number % divisor == 0])
    return divisors_sum == number
num = int(input('Enter Number: '))
result = is_perfect_number(num)
if result:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
