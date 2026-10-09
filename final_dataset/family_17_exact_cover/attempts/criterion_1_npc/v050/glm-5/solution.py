import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3 ** q
    
    # Build adjacency list: for each pair (u, v), store the third person w
    # such that (u, v, w) is a valid triple
    adj = {}
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        # Store all permutations of pairs
        pairs = [(a, b, c), (a, c, b), (b, c, a)]
        for x, y, z in pairs:
            if x not in adj:
                adj[x] = {}
            adj[x][y] = z
    
    result = []
    used = [False] * (n + 1)
    
    def dfs(remaining):
        if remaining == 0:
            return True
        
        # Find the smallest unused person
        for i in range(1, n + 1):
            if not used[i]:
                first = i
                break
        
        used[first] = True
        
        # Try all valid pairs with first
        if first in adj:
            for second in adj[first]:
                if not used[second]:
                    third = adj[first][second]
                    if not used[third]:
                        used[second] = True
                        used[third] = True
                        result.append((first, second, third))
                        if dfs(remaining - 3):
                            return True
                        result.pop()
                        used[second] = False
                        used[third] = False
        
        used[first] = False
        return False
    
    if dfs(n):
        print("YES")
        for triple in result:
            print(triple[0], triple[1], triple[2])
    else:
        print("NO")

solve()