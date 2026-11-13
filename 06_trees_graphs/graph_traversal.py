"""Breadth-first and depth-first graph traversal.

The graph is represented as an adjacency list:
{node: [neighbour, ...]}.
"""


from collections import deque


def breadth_first_search(graph, start):
    """Visit reachable nodes level by level. Time: O(V + E)."""
    if start not in graph:
        return []

    visited = {start}
    order = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return order


def depth_first_search(graph, start):
    """Visit reachable nodes depth-first. Time: O(V + E)."""
    if start not in graph:
        return []

    visited = set()
    order = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node in visited:
            continue

        visited.add(node)
        order.append(node)

        # Reverse keeps the displayed visit order aligned with adjacency order.
        for neighbour in reversed(graph.get(node, [])):
            if neighbour not in visited:
                stack.append(neighbour)

    return order


if __name__ == "__main__":
    network = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "E"],
        "D": ["B"],
        "E": ["C"],
    }
    print("BFS:", breadth_first_search(network, "A"))
    print("DFS:", depth_first_search(network, "A"))
