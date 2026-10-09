import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    index = 2
    edges = []
    adj = defaultdict(list)
    
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        index += 2
        # Check if the mixture satisfies the additional constraints
        if a + b <= 3*q and abs(b - a) >= 1:
            edges.append((a, b))
            adj[a].append(b)
    
    # Try to find a matching that matches all acids (1 to q) with alkalis (q+1 to 2q)
    # This is a bipartite matching problem
    # We can use a standard algorithm like Hopcroft-Karp or a simpler DFS-based approach
    
    match_alkali = {}  # alkali -> acid
    match_acid = {}    # acid -> alkali
    
    def dfs(u, visited):
        for v in adj[u]:
            if v in visited:
                continue
            visited.add(v)
            if v not in match_alkali or dfs(match_alkali[v], visited):
                match_alkali[v] = u
                match_acid[u] = v
                return True
        return False
    
    matched = 0
    for acid in range(1, q+1):
        if dfs(acid, set()):
            matched += 1
    
    if matched == q:
        print("YES")
        for acid in range(1, q+1):
            print(acid, match_acid[acid])
    else:
        print("NO")

if __name__ == "__main__":
    main()