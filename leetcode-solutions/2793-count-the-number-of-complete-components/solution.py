class Solution(object):
    def countCompleteComponents(self, n, edges):
        parent = list(range(n))
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        
        for a, b in edges:
            union(a, b)
        
        vertex_count = {}
        edge_count = {}
        
        for i in range(n):
            root = find(i)
            vertex_count[root] = vertex_count.get(root, 0) + 1
        
        for a, b in edges:
            root = find(a)
            edge_count[root] = edge_count.get(root, 0) + 1
        
        result = 0
        for root in vertex_count:
            k = vertex_count[root]
            e = edge_count.get(root, 0)
            if e == k * (k - 1) // 2:
                result += 1
        
        return result
