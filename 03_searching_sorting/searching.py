"""Searching algorithms. Binary search requires sorted input."""


def linear_search(values, target):
    """Return the first matching index, or -1. Time: O(n)."""
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def binary_search(sorted_values, target):
    """Find target in ascending data. Time: O(log n), space: O(1).

    The input must already be sorted; this function does not sort it.
    """
    left = 0
    right = len(sorted_values) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_value = sorted_values[middle]

        if middle_value == target:
            return middle
        if middle_value < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


if __name__ == "__main__":
    numbers = [2, 5, 8, 12, 16, 23, 38]
    print("Linear search:", linear_search(numbers, 12))
    print("Binary search:", binary_search(numbers, 23))
