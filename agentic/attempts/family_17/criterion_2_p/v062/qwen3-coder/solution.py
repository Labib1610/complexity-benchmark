import sys
from collections import defaultdict, deque

def solve():
    import sys
    import threading
    
    def main():
        import sys
        from collections import defaultdict, deque
        
        sys.setrecursionlimit(1 << 25)
        
        try:
            line = sys.stdin.readline()
            if not line:
                return
            q, t = map(int, line.split())
        except:
            return
            
        if t == 0:
            if q == 0:
                print("YES")
            else:
                print("NO")
            return
            
        # Build a graph: left nodes are 1..q, right nodes are (q+1)..2q
        # Each blueprint is an edge between a left node and a right node
        adj = defaultdict(list)
        edges = []
        
        for _ in range(t):
            a, b = map(int, sys.stdin.readline().split())
            adj[a].append((b, len(edges)))
            adj[b].append((a, len(edges)))
            edges.append((a, b))
            
        # We want to find a perfect matching in this bipartite graph
        # Left side: 1 to q
        # Right side: q+1 to 2*q
        
        match_left = {}   # match_left[l] = r
        match_right = {}  # match_right[r] = l
        
        def dfs(u, visited):
            for v, idx in adj[u]:
                if v in visited:
                    continue
                visited.add(v)
                if v not in match_right or dfs(match_right[v], visited):
                    match_left[u] = v
                    match_right[v] = u
                    return True
            return False
        
        # Try to find maximum matching
        matched = 0
        for u in range(1, q + 1):
            if u not in match_left:
                visited = set()
                if dfs(u, visited):
                    matched += 1
                    
        if matched == q:
            print("YES")
            for u in range(1, q + 1):
                print(u, match_left[u])
        else:
            print("NO")
    
    threading.Thread(target=main).start()

solve()