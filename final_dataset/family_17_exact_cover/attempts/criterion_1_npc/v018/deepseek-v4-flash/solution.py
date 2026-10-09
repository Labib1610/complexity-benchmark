import sys
sys.setrecursionlimit(10000000)

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    trios = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        trios.append((a, b, c))
    
    n = 3 * q
    used = [False] * n
    adj = [[] for _ in range(n)]
    for idx, (a, b, c) in enumerate(trios):
        adj[a].append(idx)
        adj[b].append(idx)
        adj[c].append(idx)
    
    # Sort trios by some heuristic: maybe by sum of degrees
    # Precompute degree
    degree = [0] * n
    for a, b, c in trios:
        degree[a] += 1
        degree[b] += 1
        degree[c] += 1
    
    # Order trios by total degree (smaller first) for better pruning
    trios_sorted = sorted(range(t), key=lambda i: degree[trios[i][0]] + degree[trios[i][1]] + degree[trios[i][2]])
    
    # We'll try to match operators one by one
    # Find first unused operator
    def find_unused():
        for i in range(n):
            if not used[i]:
                return i
        return -1
    
    chosen = []
    
    def backtrack():
        if len(chosen) == q:
            return True
        # Find first unused operator
        v = find_unused()
        if v == -1:
            return False
        # Try all trios containing v
        for idx in adj[v]:
            a, b, c = trios[idx]
            if used[a] or used[b] or used[c]:
                continue
            # choose
            used[a] = used[b] = used[c] = True
            chosen.append((a+1, b+1, c+1))
            if backtrack():
                return True
            # undo
            chosen.pop()
            used[a] = used[b] = used[c] = False
        return False
    
    if backtrack():
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()