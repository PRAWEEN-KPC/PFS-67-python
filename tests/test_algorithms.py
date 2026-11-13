"""Unit tests for the learning repository. Run: python -m unittest discover -s tests -v."""

import unittest

from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(name, relative_path):
    """Load a module from a folder whose name may start with a digit."""
    path = ROOT / relative_path
    spec = spec_from_file_location(name, path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


arrays = load_module("arrays", "01_fundamentals/arrays.py")
strings = load_module("strings", "01_fundamentals/strings.py")
searching = load_module("searching", "03_searching_sorting/searching.py")
sorting = load_module("sorting", "03_searching_sorting/sorting.py")
patterns = load_module("patterns", "04_problem_patterns/two_pointers.py")
dynamic = load_module("dynamic", "07_dynamic_programming/dynamic_programming.py")


class ArrayTests(unittest.TestCase):
    def test_maximum(self):
        self.assertEqual(arrays.find_maximum([-4, 2, 9, 1]), 9)

    def test_empty_maximum_raises(self):
        with self.assertRaises(ValueError):
            arrays.find_maximum([])

    def test_remove_duplicates_preserves_order(self):
        self.assertEqual(arrays.remove_duplicates([2, 1, 2, 3, 1]), [2, 1, 3])

    def test_second_largest_is_distinct(self):
        self.assertEqual(arrays.second_largest([5, 5, 4, 4]), 4)
        self.assertIsNone(arrays.second_largest([7, 7]))


class StringTests(unittest.TestCase):
    def test_palindrome_ignores_spaces_and_case(self):
        self.assertTrue(strings.is_palindrome("Never odd or even"))

    def test_first_unique_character(self):
        self.assertEqual(strings.first_non_repeating_character("swiss"), "w")


class SearchAndSortTests(unittest.TestCase):
    def test_binary_search_found_and_missing(self):
        self.assertEqual(searching.binary_search([1, 3, 5, 7], 5), 2)
        self.assertEqual(searching.binary_search([1, 3, 5, 7], 4), -1)

    def test_sorts(self):
        sample = [4, 1, 3, 1, -2]
        expected = [-2, 1, 1, 3, 4]
        self.assertEqual(sorting.merge_sort(sample), expected)
        self.assertEqual(sorting.quick_sort(sample), expected)
        self.assertEqual(sample, [4, 1, 3, 1, -2])  # Original is unchanged.


class PatternAndDynamicTests(unittest.TestCase):
    def test_two_pointer_pair(self):
        self.assertEqual(patterns.pair_sum_sorted([1, 2, 4, 6, 8], 10), (1, 3))
        self.assertIsNone(patterns.pair_sum_sorted([1, 2, 3], 20))

    def test_sliding_window(self):
        self.assertEqual(patterns.longest_unique_substring_length("abcabcbb"), 3)

    def test_dynamic_programming(self):
        self.assertEqual(dynamic.climbing_stairs(5), 8)
        self.assertEqual(dynamic.maximum_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(dynamic.coin_change_minimum([1, 2, 5], 11), 3)
        self.assertEqual(dynamic.coin_change_minimum([2], 3), -1)


if __name__ == "__main__":
    unittest.main()
