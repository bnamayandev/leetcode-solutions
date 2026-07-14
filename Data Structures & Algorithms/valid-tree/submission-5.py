class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
            
        adj = defaultdict(list)

        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        visited = set()

        def dfs(num: int, prev: int):
            if num in visited:
                return False
            
            visited.add(num)
            for edge in adj[num]:
                if edge == prev:
                    continue
                if not dfs(edge, num):
                    return False

            return True
        
        
        dfs(0, None)
        print(visited)
        return len(visited) == n