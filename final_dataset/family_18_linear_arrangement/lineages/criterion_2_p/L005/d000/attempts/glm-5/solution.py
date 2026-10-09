import sys
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    B = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    if B < n - 1:
        print("NO")
        return
    
    # DFS layout: assign positions so total stretch = n-1
    pos = [0] * (n + 1)
    visited = [False] * (n + 1)
    counter = [1]
    
    stack = [(1, 0)]  # (node, state) where state 0 = first visit
    while stack:
        node, state = stack.pop()
        if state == 0:
            visited[node] = True
            pos[node] = counter[0]
            counter[0] += 1
            # Push children in reverse order so they process left to right
            children = [c for c in adj[node] if not visited[c]]
            for c in reversed(children):
                stack.append((c, 0))
    
    print("YES")
    print(' '.join(str(pos[i]) for i in range(1, n + 1)))

solve()