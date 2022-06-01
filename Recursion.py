def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


def add_recursive(n):
    if n == 1:
        return 1
    else:
        return n + add_recursive(n - 1)


def list_sum_recursive(input_list):
    if not input_list:
        return 0
    else:
        head = input_list[0]
        smaller_list = input_list[1:]
        return head + list_sum_recursive(smaller_list)


def fibonacci_recursive(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
