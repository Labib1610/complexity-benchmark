from collections import deque
import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * (n+1)
    
    for i in range(1, n+1):
        if color[i] != -1:
            continue
        # BFS to get component nodes
        # Try two colorings
        comp_nodes = []
        q = deque([i])
        color[i] = 1
        comp_nodes.append(i)
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 3 - color[u]
                    comp_nodes.append(v)
                    q.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
        # Now we have a valid coloring for this component starting with 1.
        # Try starting with 2: we can flip all colors in this component.
        # But we must check if flipping causes conflict? Flipping all colors in a bipartite component is always valid.
        # So both are valid. Choose lexicographically smaller.
        # Since we process in increasing index order, we can compare.
        # We'll store the component nodes sorted (they are already in BFS order, but we need sorted by index)
        comp_nodes.sort()
        # Option A: current color (start with 1)
        # Option B: flip
        # Compare sequences for these nodes
        # We'll build both sequences
        seqA = [color[node] for node in comp_nodes]
        seqB = [3 - color[node] for node in comp_nodes]
        if seqB < seqA:
            # flip
            for node in comp_nodes:
                color[node] = 3 - color[node]
    
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n+1)))

if __name__ == "__main__":
    solve()