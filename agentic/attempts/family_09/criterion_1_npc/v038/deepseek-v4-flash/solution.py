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
    # We'll use backtracking with bitmasks
    def backtrack(start, chosen, mask):
        if len(chosen) == k:
            return chosen[:]
        # Prune: not enough remaining vertices
        if n - start < k - len(chosen):
            return None
        for i in range(start, n):
            if mask & (1 << i):
                continue
            # Check if i conflicts with chosen
            conflict = False
            for v in chosen:
                if adj[i] & (1 << v):
                    conflict = True
                    break
            if conflict:
                continue
            chosen.append(i)
            res = backtrack(i + 1, chosen, mask | (1 << i))
            if res:
                return res
            chosen.pop()
        return None
    
    res = backtrack(0, [], 0)
    if res is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(str(x + 1) for x in res))

if __name__ == "__main__":
    solve()