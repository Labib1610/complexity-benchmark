import sys

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    # Try to find an independent set of size k
    # Use backtracking with pruning
    def backtrack(start, chosen, mask):
        if len(chosen) == k:
            return chosen[:]
        if start >= n:
            return None
        # Prune: if remaining nodes + chosen < k, impossible
        if n - start + len(chosen) < k:
            return None
        # Try including start
        if not (mask & (1 << start)):
            chosen.append(start)
            res = backtrack(start + 1, chosen, mask | adj[start] | (1 << start))
            if res:
                return res
            chosen.pop()
        # Try excluding start
        return backtrack(start + 1, chosen, mask)
    
    res = backtrack(0, [], 0)
    if res is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(str(x + 1) for x in res))

if __name__ == "__main__":
    solve()