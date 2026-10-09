import sys
sys.setrecursionlimit(300000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    pos = [0] * n
    order = []
    
    # DFS to get in-order (preorder) positions
    stack = [(0, -1, 0)]  # node, parent, state (0=enter, 1=exit)
    counter = 0
    while stack:
        u, p, state = stack.pop()
        if state == 0:
            pos[u] = counter
            counter += 1
            order.append(u)
            stack.append((u, p, 1))
            for v in adj[u]:
                if v != p:
                    stack.append((v, u, 0))
        # exit state: nothing needed
    
    # Compute total stretch
    total = 0
    for u in range(n):
        for v in adj[u]:
            if u < v:
                total += abs(pos[u] - pos[v])
    
    if total <= B:
        print("YES")
        print(" ".join(str(pos[i] + 1) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()