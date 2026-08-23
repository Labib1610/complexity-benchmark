We can model this as a graph coloring problem with 3 colors, where we want the lexicographically smallest valid coloring.

Since \( n \leq 40 \), we can use backtracking with pruning.  
We assign colors to nodes in order from 1 to n, trying color 1 first, then 2, then 3, and check conflicts with already colored neighbors.

```python
import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * n
    
    def backtrack(idx):
        if idx == n:
            return True
        for c in range(1, 4):
            ok = True
            for nb in adj[idx]:
                if colors[nb] == c:
                    ok = False
                    break
            if ok:
                colors[idx] = c
                if backtrack(idx + 1):
                    return True
                colors[idx] = 0
        return False
    
    colors = [0] * n
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, colors)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()