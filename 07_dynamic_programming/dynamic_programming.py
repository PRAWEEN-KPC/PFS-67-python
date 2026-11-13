"""Dynamic programming examples: solve smaller overlapping problems once."""


def climbing_stairs(number_of_steps):
    """Count ways to climb 1 or 2 steps at a time.

    Time: O(n) | Extra space: O(1)
    """
    if number_of_steps < 0:
        return 0
    if number_of_steps <= 1:
        return 1

    one_step_before = 1
    two_steps_before = 1

    for _ in range(2, number_of_steps + 1):
        current = one_step_before + two_steps_before
        two_steps_before = one_step_before
        one_step_before = current

    return one_step_before


def maximum_subarray_sum(numbers):
    """Kadane's algorithm: largest sum of a non-empty contiguous subarray.

    Time: O(n) | Extra space: O(1)
    """
    if not numbers:
        raise ValueError("numbers must not be empty")

    best_ending_here = best_overall = numbers[0]

    for number in numbers[1:]:
        best_ending_here = max(number, best_ending_here + number)
        best_overall = max(best_overall, best_ending_here)

    return best_overall


def coin_change_minimum(coins, amount):
    """Minimum number of coins needed to make amount; return -1 if impossible.

    Assumes all coin values are positive integers.
    Time: O(amount * len(coins)) | Extra space: O(amount)
    """
    if amount < 0:
        raise ValueError("amount must be non-negative")
    if any(coin <= 0 for coin in coins):
        raise ValueError("coin values must be positive")

    unreachable = amount + 1
    best = [unreachable] * (amount + 1)
    best[0] = 0

    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                best[current_amount] = min(
                    best[current_amount],
                    best[current_amount - coin] + 1,
                )

    return -1 if best[amount] == unreachable else best[amount]


if __name__ == "__main__":
    print("Ways to climb 5 steps:", climbing_stairs(5))
    print("Maximum subarray sum:", maximum_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print("Minimum coins:", coin_change_minimum([1, 2, 5], 11))
