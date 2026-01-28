def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
def digit_count(num):
    count = 0
    while num > 0:
        count += 1
        num = num//10
    return count
def sum_of_digits(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit
        num = num//10
    return sum
def is_prime(num):
    if num <= 1:
        return "Not Prime."
    for i in range(2,num):
        if num % i == 0:
            return "Not Prime."
        else:
            return "Prime."
number = int(input("Enter a number:"))
print("Odd/Even:",even_odd(number))
print("Digit Count:",digit_count(number))
print("Sum of Digits:",sum_of_digits(number))
print("Prime or not:",is_prime(number))