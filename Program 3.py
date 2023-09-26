# Task 1: Convert decimal numbers to octal numbers
def decimal_to_octal(decimal_num):
    return oct(decimal_num)

# Task 2: Reverse an integer
def reverse_integer(number):
    if number < 0:
        return -int(str(-number)[::-1])
    else:
        return int(str(number)[::-1])

# Task 3: Print the Fibonacci series using the recursive method
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci_recursive(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

# Task 4: Return the Nth value from the Fibonacci Sequence
def fibonacci_nth(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

decimal_number = 24
print(f"Decimal to Octal: {decimal_to_octal(decimal_number)}")

integer_to_reverse = 12345
print(f"Reversed Integer: {reverse_integer(integer_to_reverse)}")

n_fibonacci_series = 5
print(f"Fibonacci Series (Recursive): {fibonacci_recursive(n_fibonacci_series)}")

nth_fibonacci = 15
print(f"{nth_fibonacci}th Fibonacci Number: {fibonacci_nth(nth_fibonacci)}")
