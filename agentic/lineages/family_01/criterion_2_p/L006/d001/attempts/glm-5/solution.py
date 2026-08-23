import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
        
        # BFS to check bipartiteness and assign colors
        # We want lexicographically smallest, so we try to assign 1 to the start node.
        # If it leads to a conflict, we try assigning 2.
        # Actually, for a connected component, assigning 1 to the lowest numbered node
        # is always optimal for lexicographical order, provided it's bipartite.
        # If it's not bipartite, assigning 2 won't help either.
        
        # Let's do a standard BFS and check for bipartiteness.
        # If we find a conflict, the whole graph is not bipartite.
        
        color[start] = 1
        q = deque([start])
        ok = True
        component_nodes = [start]
        
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - color[u]
                    q.append(v)
                    component_nodes.append(v)
                elif color[v] == color[u]:
                    ok = False
                    # We can break early, but we need to consume the queue or just return NO
                    # Let's just set a flag and break out of all loops.
                    break
            if not ok:
                break
        
        if not ok:
            print("NO")
            return
        
        # Now, we need to check if assigning 1 to `start` was optimal.
        # Actually, for lexicographically smallest, we want the smallest numbered node
        # in the component to be 1. Since we iterate `start` from 1 to n, and `start`
        # is the smallest uncolored node, it is the smallest in its component.
        # So assigning 1 to it is optimal.
        
        # However, there's a catch: what if the component is bipartite, but assigning 1
        # to `start` forces a higher numbered node to be 1, whereas assigning 2 to `start`
        # would allow that higher numbered node to be 1?
        # Wait, no. Lexicographically smallest means we want f[1] as small as possible,
        # then f[2], etc. Since `start` is the smallest in the component, we want f[start]=1.
        # The colors of other nodes are then determined by the bipartition.
        # There's no choice: once f[start] is fixed, all others in the component are fixed.
        # And we want f[start]=1 because start is the smallest index in the component.
        # So the assignment is uniquely determined for each component (up to swapping),
        # and we pick the one where the smallest index is 1.
        
        # But wait, is it possible that by assigning 1 to `start`, some other node `x` (x > start)
        # gets 1, but if we assigned 2 to `start`, `x` would get 2, and some other node `y` (y > x)
        # would get 1? That doesn't matter because lexicographical order prioritizes smaller indices.
        # Since `start` is the smallest, f[start]=1 is better than f[start]=2, regardless of later nodes.
        
        # So the current assignment is optimal.
        pass
    
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

solve()