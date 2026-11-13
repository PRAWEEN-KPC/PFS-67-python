"""Common interview patterns: two pointers and sliding window."""


def pair_sum_sorted(numbers, target):
    """Return indices of two values adding to target in sorted input.

    Returns None when no pair exists.
    Time: O(n) | Extra space: O(1)
    """
    left, right = 0, len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return left, right
        if total < target:
            left += 1
        else:
            right -= 1

    return None


def longest_unique_substring_length(text):
    """Length of the longest substring with no repeated characters.

    Time: O(n) average | Extra space: O(k)
    """
    last_seen = {}
    window_start = 0
    longest = 0

    for index, character in enumerate(text):
        if character in last_seen and last_seen[character] >= window_start:
            window_start = last_seen[character] + 1

        last_seen[character] = index
        longest = max(longest, index - window_start + 1)

    return longest


if __name__ == "__main__":
    print("Pair indices:", pair_sum_sorted([1, 2, 4, 6, 8], 10))
    print("Longest unique substring:", longest_unique_substring_length("abcabcbb"))
