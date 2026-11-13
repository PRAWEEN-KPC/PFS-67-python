"""Beginner-friendly array (Python list) algorithms.

Run: python 01_fundamentals/arrays.py
"""


def find_maximum(numbers):
    """Return the largest number without using max().

    Time: O(n) | Extra space: O(1)
    """
    if not numbers:
        raise ValueError("numbers must not be empty")

    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest


def reverse_list(numbers):
    """Return a reversed copy; the original list stays unchanged.

    Time: O(n) | Extra space: O(n)
    """
    reversed_numbers = []
    for index in range(len(numbers) - 1, -1, -1):
        reversed_numbers.append(numbers[index])
    return reversed_numbers


def remove_duplicates(numbers):
    """Keep the first occurrence of each value, preserving order.

    Time: O(n) average | Extra space: O(n)
    """
    seen = set()
    unique_numbers = []

    for number in numbers:
        if number not in seen:
            seen.add(number)
            unique_numbers.append(number)

    return unique_numbers


def second_largest(numbers):
    """Return the second distinct largest value, or None if it doesn't exist.

    Time: O(n) | Extra space: O(1)
    """
    largest = second = None

    for number in numbers:
        if largest is None or number > largest:
            second = largest
            largest = number
        elif number != largest and (second is None or number > second):
            second = number

    return second


if __name__ == "__main__":
    sample = [12, 5, 8, 12, 3, 9]
    print("Input:", sample)
    print("Maximum:", find_maximum(sample))
    print("Reversed copy:", reverse_list(sample))
    print("Without duplicates:", remove_duplicates(sample))
    print("Second largest distinct value:", second_largest(sample))
