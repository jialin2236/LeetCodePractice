# Graph key Topics
## Key Topics
- Disjoint Set (UnionFind)
  - Usage: build graph from given list of edges, quick display number of subgraphs and
- Minimum Spanning Tree (MST)
- DFS
- BFS
- Dijkstra Algorithm 

## Disjoint Set
key methods

|    |  constructor  | `find`  | `union` |
| ---   | ---        | ---     | ---     |
| `QuickFind` | O(N)  | O(1)   | O(N)    |
| `QuickUnion` | O(N) | O(N) worst | O(N) |
| `UnionByRank` | O(N) | O(logN)   | O(logN) |
| Path Compression | O(N) | O(logN), O(N) worse | O(logN) |


Overall, `QuickFind` achieves O(1) time in finding the root of a node, by placing the find root process
during the union of 2 nodes, and modify `self.root` using dfs like method during union. `QuickUnion` instead finds the root when 
`self.find` function is called, and only modifies the `self.root` once during union. 

Example: 

```
# 1-2-3-4  5-6
QuickFind: 
root = [1, 1, 1, 1, 5, 5]
QuickUnion:
root = [1, 1, 2, 3, 5, 5]
```

<details>
    <summary>scripts for QuickFind, QuickUnion</summary>

```
class UnionFind: 
    def __init__(self, n: int): 
        # n - number of vertices in graph 
        self.root = [i for i in range(n)]
       
    def find_quickfind(self, x): 
        # find the root node of node x
        # find root of x is already assigned to its most parent node
        return self.root[x]
    
    def find_quickunion(self, x): 
        # find the root node of node x
        # root of x is its direct parent node
        # this is without path compression
        while self.root[x] != x: 
            x = self.root[x]
        return x
        
    def union_quickfind(self, x, y): 
        # connect the two nodes x and y
        # for QuickFind, we need to use dfs to find and union each parent node of x and y
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y: 
            for i in range(len(root)): 
                if self.root[i] == root_y: 
                    self.root[i] = root_x
    
    def union_quickunion(self, x, y): 
        # connect the two nodes x and y
        # for QuickUnion, we only need to re-assign the 2 nodes root value once to reflect the relationship
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y: 
            self.root[root_y] = root_x
    
    def connected(self, x, y): 
        return self.find(x) == self.find(y)
```
</details>

In above example, to union node 5 and node 6, and find node 6, would have worst case time complexity of O(N), since it's 
just a line. To optimize the time complexity, `UnionByRank` and **Path Compression** could be used.

The idea of `UnionByRank` is to merge the smaller graph/tree into the larger graph/tree, to avoid creating a graph/tree
with depth of `depth1 + depth2`. **Path Compression** is a technique to update the parent node of all traversed elements to 
their root node. When we search for the root node of the same element again, 
we only need to traverse two elements to find its root node, which is highly efficient. See demonstration, 
```
# 1-2-3-4 5-6
# if union(5,6)
QuickFind/QuickUnion result: 
1-2-3-4-5-6
depth of the new set = depth of set 1 + depth of set 2 = 4 + 2 = 6
UnionByRank chooses the larger tree as a base, and merge the smaller tree into it: 
1-2-3-4
 \
  5-6
depth of the new set = max(depth of set 1, depth of set 2) = 4
```

<details>
    <summary>script for UnionByRank</summary>

```
class UnionFind:
    def __init__(self, n): 
        self.root = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x): 
        # with path compression
        if x == self.root[x]: 
            return x
        self.root[x] = self.find(root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x = self.root[x]
        root_y = self.root[y]
        if root_x != root_y: 
            if self.rank[root_x] > self.rank[root_y]: 
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]: 
                self.root[root_x] = root_y
            else: 
                self.root[root_y] = root_x
                self.rank[root_x] += 1
```
</details>

Related Problems: 
- 547_num_of_provinces 
- 261_Graph_valid_tree
- 323_Num_of_Connected_Components_in_Undirected_Graph
- 399_Evaluate_division 
- 1168_optimize_water_distribution

## Minimum Spanning Tree 
Given a connected, edge-weighted and undirected graph, a MST is a subset of edges that connect all 
vertices while the total weights of these edges are minimum among all possible subsets. 

an undirected graph can have multiple spanning trees. 

- Prim's algorithm
- Kruskal's algorithm

### Prim's algorithm
algorithm iterates by building the tree one vertex at a time, from an arbitrary starting vertex, at each step adding
the cheapest possible connection from any vertex in the tree to a vertex that is not in the tree. 

Data Structure Needed: 
1. adjacency list, to represent the graph
2. set, to represent vertices that's been visited/added 
3. heap, to represent the priority of the neighboring vertices

### Kruskal's algorithm 
we iterate through all the edges ordered by their costs. For each edge, we decide whether to add it to the final MST. 
The decision is based on whether this new addition will help to connect more dots (i.e. vertices).

steps:
1. sort all the edges based on their costs, including the additional edges that are added with the virtual vertex.
2. iterate through the sorted edges. 
   1. For each edge, if both ends of the edge belong to different groups, with the help of the Union-Find data structure, 
      we then add this edge into the final MST.


## DFS - Depth First Search
A method to explore all potential path by exploring depth first. 

```
# adj_list: represent relationship between nodes
# start: starting point of the search
visited = set()
stack = deque()
stack.append(start)

while stack: 
    top = stack.pop()
    if top not in visited: 
        visited.add(top)
        for neighbor in adj_list[top]:
            stack.append(neighbor)
```

## Dijkstra Algorithm 
Dijkstra Algorithm is used to solve the "single-source shortest path" problem in a weighted directed graph with 
non-negative weights.  

The main idea is to start at `u` as the center and gradually expand outward while updating the "shortest path" to reach 
other vertices. It is a greedy approach that guarantees the final solution to be optimal. 

Complexity: 
- Time O(E+VlogV)
- Space O(V)

```
def dijkstra(graph: defaultdict, source: str, target: str) -> Dict[Tuple]:
    seen, remain = defaultdict(Tuple), defaultdict(Tuple)
    seen[source] = (0, None)
    curr, d2s = source, 0
    while target not in seen:
        prev = curr
        for nei, dist in graph[prev].items():
            if nei not in seen or seen[nei][0] < d2s + dist:
                seen[nei] = (d2s + dist, prev)

        curr = min(seen, key=seen.get)
        d2s, adj = remain[curr]
        seen[curr] = (d2s, adj)
        del remain[curr]
    return seen
```