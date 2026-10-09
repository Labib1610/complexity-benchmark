import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].add(v)
        adj[v].add(u)
    
    # Greedy approach: repeatedly pick vertex with smallest degree
    # This is a standard heuristic for finding large independent sets
    # and works well for this problem size
    
    # Create list of vertices with their degrees
    vertices = list(range(n))
    
    result = []
    available = [True] * n
    
    # Sort by degree initially
    vertices.sort(key=lambda x: len(adj[x]))
    
    for v in vertices:
        if available[v]:
            # Check if we can add v to result
            can_add = True
            for u in result:
                if v in adj[u]:
                    can_add = False
                    break
            
            if can_add:
                result.append(v)
                # Mark neighbors as unavailable
                for u in adj[v]:
                    available[u] = False
                
                if len(result) == k:
                    print("YES")
                    print(" ".join(str(x + 1) for x in result))
                return
    
    # If greedy didn't find k vertices, try a more thorough search
    # Use meet-in-the-middle approach for n <= 46
    
    # Reset and try exhaustive search with pruning
    result = []
    used = [False] * n
    
    def backtrack(idx, count):
        if count == k:
            return True
        if idx == n:
            return False
        if n - idx < k - count:
            return False
        
        # Try including vertex idx
        can_include = True
        for v in result:
            if idx in adj[v]:
                can_include = False
                break
        
        if can_include:
            result.append(idx)
            if backtrack(idx + 1, count + 1):
                return True
            result.pop()
        
        # Try excluding vertex idx
        if backtrack(idx + 1, count):
            return True
        
        return False
    
    if backtrack(0, 0):
        print("YES")
        print(" ".join(str(x + 1) for x in result))
    else:
        print("NO")

solve()