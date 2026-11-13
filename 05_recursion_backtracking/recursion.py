"""Recursion and backtracking fundamentals."""


def factorial(number):
    """Calculate n! recursively. Time: O(n), call stack: O(n)."""
    if number < 0:
        raise ValueError("factorial is not defined for negative integers")
    if number <= 1:
        return 1
    return number * factorial(number - 1)


def fibonacci(number):
    """Return the nth Fibonacci number using memoization.

    Time: O(n) | Extra space: O(n)
    """
    if number < 0:
        raise ValueError("number must be non-negative")

    memo = {0: 0, 1: 1}

    def calculate(index):
        if index not in memo:
            memo[index] = calculate(index - 1) + calculate(index - 2)
        return memo[index]

    return calculate(number)


def generate_subsets(values):
    """Return every subset of values using backtracking.

    For n values, there are 2**n subsets; time and output space: O(n * 2**n).
    """
    results = []
    current = []

    def build(start):
        results.append(current.copy())

        for index in range(start, len(values)):
            current.append(values[index])
            build(index + 1)
            current.pop()  # Undo the choice before trying the next value.

    build(0)
    return results


if __name__ == "__main__":
    print("5! =", factorial(5))
    print("Fibonacci(8) =", fibonacci(8))
    print("Subsets:", generate_subsets([1, 2, 3]))
