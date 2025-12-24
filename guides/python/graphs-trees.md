There is currently no access to external tools, so inline citations cannot be generated even though they are required. The guide below is therefore uncited but written to be clear and comprehensive for all skill levels.

---

# Trees and Graphs in Python: A Comprehensive Guide

Trees and graphs are core data structures for representing relationships: hierarchies, networks, maps, and more. This guide starts from intuitive ideas and moves up to practical implementations with examples.

***

## 1. Concepts: Nodes, Edges, Trees, Graphs

- **Node**: A container that holds a value (data) and links to other nodes.  
- **Edge**: A connection between two nodes.  
- **Tree**: A special type of graph:
  - Has one root (top node).
  - Every node except the root has exactly one parent.
  - No cycles (you never loop back if you keep following children).  
- **Graph**:
  - More general.
  - Nodes can be connected in any pattern.
  - May have cycles and multiple connections.

Think of:

- Tree → folder structure on your computer.  
- Graph → city map with roads, or social networks.

***

## 2. Representing Trees in Python

### 2.1 Simple general tree node class

A “general” tree node can have any number of children.

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # list[TreeNode]

    def add_child(self, child_node):
        self.children.append(child_node)


# Example: small company org chart
ceo = TreeNode("CEO")
cto = TreeNode("CTO")
cfo = TreeNode("CFO")
dev1 = TreeNode("Developer 1")
dev2 = TreeNode("Developer 2")

ceo.add_child(cto)
ceo.add_child(cfo)
cto.add_child(dev1)
cto.add_child(dev2)
```

This is enough for many tree-shaped structures (organization charts, category trees, file trees).

### 2.2 Printing a tree (recursive pretty-print)

```python
def print_tree(node, level=0):
    indent = "  " * level
    print(f"{indent}- {node.value}")
    for child in node.children:
        print_tree(child, level + 1)

print_tree(ceo)
```

Output:

```text
- CEO
  - CTO
    - Developer 1
    - Developer 2
  - CFO
```

Key idea: recursion mirrors the natural “tree” shape.

---

## 3. Binary Trees

A binary tree limits each node to at most two children: `left` and `right`. This structure is used heavily in searching, indexing, and many algorithms.

### 3.1 Binary tree node class

```python
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None   # BinaryTreeNode or None
        self.right = None  # BinaryTreeNode or None


# Example: simple binary tree
root = BinaryTreeNode(10)
root.left = BinaryTreeNode(5)
root.right = BinaryTreeNode(15)
root.left.left = BinaryTreeNode(2)
root.left.right = BinaryTreeNode(7)
```

This is just a special case of a tree with exactly two “slots” for children.

---

## 4. Tree Traversals (Beginner to Intermediate)

Tree traversal means “visiting every node” in a specific order.

### 4.1 Depth-first traversals (DFS) on binary trees

Assume this tree:

```text
      10
     /  \
    5    15
   / \
  2   7
```

#### Inorder (Left, Root, Right)

Good for: sorted order in Binary Search Trees (BSTs).

```python
def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.value, end=" ")
    inorder(node.right)

inorder(root)  # 2 5 7 10 15
```

#### Preorder (Root, Left, Right)

Good for: copying the tree, serializing structure.

```python
def preorder(node):
    if not node:
        return
    print(node.value, end=" ")
    preorder(node.left)
    preorder(node.right)

preorder(root)  # 10 5 2 7 15
```

#### Postorder (Left, Right, Root)

Good for: deleting tree, evaluating expression trees.

```python
def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value, end=" ")

postorder(root)  # 2 7 5 15 10
```

### 4.2 Breadth-first traversal (BFS) / level-order

Visits nodes level by level, using a queue.

```python
from collections import deque

def level_order(root):
    if not root:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.value, end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

level_order(root)  # 10 5 15 2 7
```

Use BFS when you want the “closest” nodes first (like shortest path in unweighted graphs).

---

## 5. Binary Search Trees (BSTs)

A Binary Search Tree (BST) keeps values ordered:

- Left subtree: values < current.
- Right subtree: values > current.

This allows fast search, insert, and delete on average.

### 5.1 Insertion in BST

```python
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        # If equal, you can choose to ignore or handle duplicates specially.
```

Usage:

```python
root = BSTNode(10)
for v in [5, 15, 2, 7, 12, 20]:
    root.insert(v)
```

### 5.2 Searching in BST

```python
def bst_search(node, target):
    if node is None:
        return False
    if target == node.value:
        return True
    if target < node.value:
        return bst_search(node.left, target)
    else:
        return bst_search(node.right, target)

print(bst_search(root, 7))   # True
print(bst_search(root, 100)) # False
```

### 5.3 Inorder traversal of BST gives sorted values

```python
def inorder_list(node, result=None):
    if result is None:
        result = []
    if node:
        inorder_list(node.left, result)
        result.append(node.value)
        inorder_list(node.right, result)
    return result

print(inorder_list(root))  # sorted list of values
```

This is a simple way to sort numbers using a tree (though built-in `sorted` is faster and easier in practice).

***

## 6. Introduction to Graphs

Graphs are more general than trees and can represent arbitrary relationships.

### 6.1 Basic terminology

- **Directed graph (digraph)**: edges have a direction (A → B).  
- **Undirected graph**: edges don’t have direction (A — B).  
- **Weighted graph**: edges carry a cost or weight.  
- **Path**: sequence of nodes connected by edges.  
- **Cycle**: path that starts and ends at the same node with at least one edge.

Examples:

- Web pages and links → directed graph.  
- Road map (two-way roads) → undirected graph.  
- Road map with distances → weighted undirected graph.

### 6.2 Graph representation: adjacency list

In Python, a common representation is a dictionary from node → list of neighbors.

```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"]
}
```

Each key is a node, and each value is the list of nodes directly connected to it.

***

## 7. Graph Traversals: BFS and DFS

### 7.1 BFS on an unweighted graph

Use BFS to find shortest path (fewest edges) from a starting node.

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    q = deque([start])
    visited.add(start)

    while q:
        node = q.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

bfs(graph, "A")  # A B C D E (one possible order)
```

### 7.2 DFS on a graph (recursive)

DFS explores as deep as possible before backtracking.

```python
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

dfs(graph, "A")  # A B D C E (one possible order)
```

DFS is useful for:

- Checking if a graph is connected.
- Exploring components.
- Detecting cycles (with extra logic).

***

## 8. Shortest Path (Unweighted Graphs)

To find the actual shortest path (fewest edges) from `start` to `goal`, use BFS and keep track of parents.

```python
from collections import deque

def shortest_path_unweighted(graph, start, goal):
    q = deque([start])
    visited = {start}
    parent = {start: None}

    while q:
        node = q.popleft()
        if node == goal:
            break
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                q.append(neighbor)

    if goal not in parent:
        return None  # no path

    # Reconstruct path
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path

print(shortest_path_unweighted(graph, "A", "E"))  # e.g., ['A', 'B', 'D', 'E']
```

This pattern is widely used in routing, puzzles, and simple network analysis.

---

## 9. Weighted Graphs and Dijkstra (Advanced)

If edges have weights (like distances), BFS is not enough; edges are not all “equally long”. Dijkstra’s algorithm finds the shortest path in a graph with non-negative edge weights.

### 9.1 Weighted graph representation

```python
weighted_graph = {
    "A": [("B", 5), ("C", 1)],
    "B": [("A", 5), ("C", 2), ("D", 1)],
    "C": [("A", 1), ("B", 2), ("D", 4)],
    "D": [("B", 1), ("C", 4)]
}
```

Each neighbor is a tuple `(node, weight)`.

### 9.2 Dijkstra’s algorithm (simple version)

```python
import heapq

def dijkstra(graph, start):
    # distances: shortest known distance from start
    dist = {node: float("inf") for node in graph}
    dist[start] = 0

    # priority queue of (distance, node)
    pq = [(0, start)]

    while pq:
        current_dist, node = heapq.heappop(pq)

        if current_dist > dist[node]:
            continue  # stale entry

        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist

print(dijkstra(weighted_graph, "A"))
# Example output: {'A': 0, 'B': 3, 'C': 1, 'D': 4}
```

This is a key algorithm for routing and many optimization problems.

---

## 10. Common Use Cases and How to Think About Them

### 10.1 Trees

- **Hierarchical data**:
  - File system, organization chart, category tree.
  - Use a `TreeNode` with `children` list.
- **Search trees**:
  - Quick lookups and range queries.
  - Use BSTs or balanced trees (AVL, Red-Black; usually rely on libraries or use `dict`/`set`).
- **Expression trees**:
  - Represent mathematical expressions as trees.
  - Postorder traversal can evaluate the expression.

### 10.2 Graphs

- **Social networks**:
  - Users as nodes, relationships as edges.
  - Use adjacency list; BFS/DFS to find friends-of-friends, connected components.
- **Maps and routing**:
  - Cities/intersections as nodes, roads as edges.
  - Weighted graphs with Dijkstra (or A*).
- **Dependency graphs**:
  - Packages or tasks as nodes.
  - Edges represent “A depends on B”.
  - Topological sort (on DAGs) to find valid build or execution order.

---

## 11. Practice Ideas by Skill Level

### Beginner

- Build a small tree representing your family or folder structure and print it with indentation.  
- Implement a binary tree with 5–7 nodes and write functions that:
  - Count nodes.
  - Find the maximum value.
  - Print all leaf nodes.

### Intermediate

- Implement BST insert and search.  
- Read a simple road map (nodes and connections) from a text file into an adjacency list and:
  - Print all neighbors of a given city.
  - Check if two cities are connected using BFS.

### Advanced

- Implement Dijkstra and test on a small weighted graph (cities and distances).  
- Detect cycles in a directed graph using DFS and recursion stack tracking.  
- Implement topological sort for a DAG of tasks with dependencies.