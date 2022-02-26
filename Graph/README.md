# Graph key Topics
## Disjoint Set
key methods 
- `QuickFind`
- `QuickUnion`
- `UnionByRank`
- `Path Compression`

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
        while self.root[x] != x: 
            x = self.root[x]
        return x
        
    def union_quickfind(self, x, y): 
        # connect the two nodes x and y
        # for QuickFind, we need to use dfs to find and union each parent node of x and y
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y: 
            for i in range(n): 
                if self.root[i] == root_y: 
                    self.root[i] = root_x
    
    def union_quickunion(self, x, y): 
        # connect the two nodes x and y
        # for QuickUnion, we only need to re-assign the 2 nodes root value once to reflect the relationship
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x != root_y: 
            self.root[root_y] = root_x
    
    def connected(self, x, y): 
        return self.find(x) == self.find(y)
```
</details>

In above example, to union node 5 and node 6, and find node 6, would have worst case time complexity of O(N), since it's 
just a line. To optimize the time complexity, `UnionByRank` could be used.

The idea of `UnionByRank` is to merge the smaller graph/tree into the larger graph/tree, to avoid creating a graph/tree
with depth of `depth1 + depth2`. See demonstration, 
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
- [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/)
- 