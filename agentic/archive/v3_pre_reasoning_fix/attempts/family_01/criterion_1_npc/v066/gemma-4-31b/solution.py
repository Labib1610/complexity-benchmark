```python
import sys

def solve():
    # Increase recursion depth for deep backtracking if necessary
    sys.setrecursionlimit(2000)
    
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    # s stores the assigned frequency for each unit (1 to n)
    s = [0] * (n + 1)

    def is_valid(u, color):
        for v in adj[u]:
            if