# Python DSA — Beginner to Advanced

A practical, interview-focused collection of **Data Structures and Algorithms implemented in Python**. The goal is to write code that is readable, explainable, testable, and efficient—not merely short.

> Learning repository for a Python Full Stack Trainee. Each topic includes a clear implementation, a short explanation, complexity notes, and examples.

## Learning path

| Level | Topics | Folder |
|---|---|---|
| 01 · Foundations | Complexity, arrays, strings, basic patterns | `01_fundamentals/` |
| 02 · Core data structures | Linked lists, stacks, queues, hash maps | `02_data_structures/` |
| 03 · Searching & sorting | Binary search, merge sort, quick sort | `03_searching_sorting/` |
| 04 · Problem-solving patterns | Two pointers, sliding window, prefix sums | `04_problem_patterns/` |
| 05 · Recursion & backtracking | Recursion, subsets, permutations | `05_recursion_backtracking/` |
| 06 · Trees & graphs | Traversals, BFS, DFS, shortest paths | `06_trees_graphs/` |
| 07 · Dynamic programming | Memoization, tabulation, classic problems | `07_dynamic_programming/` |

## Repository structure

```text
PFS-67-python/
├── 01_fundamentals/
│   ├── arrays.py
│   └── strings.py
├── 02_data_structures/
│   ├── linked_list.py
│   ├── stack_queue.py
│   └── hash_map.py
├── 03_searching_sorting/
│   ├── searching.py
│   └── sorting.py
├── 04_problem_patterns/
│   └── two_pointers.py
├── 05_recursion_backtracking/
│   └── recursion.py
├── 06_trees_graphs/
│   └── graph_traversal.py
├── 07_dynamic_programming/
│   └── dynamic_programming.py
├── tests/
│   └── test_algorithms.py
├── .gitignore
├── pyproject.toml
└── README.md
```

## Run the examples

Requires Python 3.10 or newer.

```bash
git clone https://github.com/PRAWEEN-KPC/PFS-67-python.git
cd PFS-67-python
python -m venv .venv
```

Activate the environment:

- Windows PowerShell: `.venv\\Scripts\\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

Run a module:

```bash
python -m 01_fundamentals.arrays
```

Run tests:

```bash
python -m unittest discover -s tests -v
```

## Code conventions

- Use descriptive names and small functions with one responsibility.
- Validate important input assumptions.
- Prefer Python's built-in data structures when they are the right tool.
- State time and space complexity for each algorithm.
- Include examples and edge cases.
- Keep implementations dependency-free unless a dependency is genuinely useful.

## Complexity quick reference

| Operation / algorithm | Typical time |
|---|---:|
| List indexing | O(1) |
| Linear search | O(n) |
| Binary search on sorted data | O(log n) |
| Merge sort | O(n log n) |
| Hash table lookup (average) | O(1) |
| BFS / DFS | O(V + E) |
| Standard comparison sorting | O(n log n) |

Complexity can vary with the input and implementation. Notes in each module explain the relevant assumptions.

## Progress

This repository is built progressively. Topics should be marked complete only after the implementation, examples, and tests have been reviewed and run.

## Author

**Praween Kamani**  
Python Full Stack Trainee

---

If you find an issue or have a better edge case, open an issue or suggest an improvement.