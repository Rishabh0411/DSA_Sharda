def count_digits(num):
    num_len = 0
    while num > 0:
        num //= 10
        num_len += 1
    return num_len

def sum_of_digit_powers(num, num_len):
    sum_of_powers = 0
    while num > 0:
        digit = num % 10
        sum_of_powers += digit ** num_len
        num //= 10
    return sum_of_powers

def is_armstrong_number(num):
    num_len = count_digits(num)
    return sum_of_digit_powers(num, num_len) == num

# Test Case
number = 372
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
    