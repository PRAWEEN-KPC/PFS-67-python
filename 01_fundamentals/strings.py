"""Useful string problems with straightforward Python implementations."""


def is_palindrome(text):
    """Check whether text reads the same forward and backward.

    This version ignores spaces, punctuation, and letter case.
    Time: O(n) | Extra space: O(n)
    """
    cleaned = "".join(character.lower() for character in text if character.isalnum())
    return cleaned == cleaned[::-1]


def count_vowels(text):
    """Count English vowels, without treating y as a vowel.

    Time: O(n) | Extra space: O(1)
    """
    vowels = set("aeiou")
    return sum(1 for character in text.lower() if character in vowels)


def first_non_repeating_character(text):
    """Return the first character that appears exactly once, or None.

    Time: O(n) | Extra space: O(k), where k is the number of distinct characters.
    """
    frequencies = {}
    for character in text:
        frequencies[character] = frequencies.get(character, 0) + 1

    for character in text:
        if frequencies[character] == 1:
            return character
    return None


if __name__ == "__main__":
    phrase = "Never odd or even"
    print("Palindrome:", is_palindrome(phrase))
    print("Vowels:", count_vowels("Python Full Stack"))
    print("First unique character:", first_non_repeating_character("swiss"))
