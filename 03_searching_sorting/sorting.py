"""Sorting algorithms written for clarity and interview practice."""


def merge_sort(values):
    """Return a sorted copy using merge sort.

    Time: O(n log n) | Extra space: O(n)
    """
    if len(values) <= 1:
        return values.copy()

    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])

    merged = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


def quick_sort(values):
    """Return a sorted copy using a readable recursive quick sort.

    Average time: O(n log n); worst time: O(n^2).
    This simple version allocates new lists for clarity.
    """
    if len(values) <= 1:
        return values.copy()

    pivot = values[len(values) // 2]
    smaller = [value for value in values if value < pivot]
    equal = [value for value in values if value == pivot]
    larger = [value for value in values if value > pivot]

    return quick_sort(smaller) + equal + quick_sort(larger)


if __name__ == "__main__":
    sample = [8, 3, 1, 7, 0, 10, 2]
    print("Merge sort:", merge_sort(sample))
    print("Quick sort:", quick_sort(sample))
