import time

# This is an exercise that allows me to compare the time complexity difference
# between a recursive algorithm and an iterative algorithm that do the same thing.


def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    fib_num = [0, 1]  # These are the first 2 numbers of the Fibonacci series
    # From now on, just append the sum of the previous 2 numbers.
    for i in range(2, n + 1):
        fib_num.append(fib_num[i - 1] + fib_num[i - 2])
    return fib_num[n]


while True:
    user_int = int(input("\nType in a number:\t"))

    start = time.time()
    iterative_result = fibonacci_iterative(user_int - 1)
    end = time.time()
    iterative_time = end - start
    print("The iterative method took " + str(iterative_time) + " (s) and gave the answer " + str(iterative_result))

    start = time.time()
    recursive_result = fibonacci_recursive(user_int - 1)  # So that 1 maps the the first item in array arr[i]
    end = time.time()
    recursive_time = end - start
    print("The recursive method took " + str(recursive_time) + " (s) and gave the answer " + str(recursive_result))
