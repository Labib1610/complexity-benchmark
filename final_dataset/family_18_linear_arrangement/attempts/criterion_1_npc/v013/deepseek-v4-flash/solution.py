import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m, B = map(int, input().split())
    edges = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].append(v)
        edges[v].append(u)
    
    # Try multiple starting points: highest degree first, then others
    order = sorted(range(n), key=lambda x: -len(edges[x]))
    
    for start in order:
        # BFS from start
        dist = [-1]*n
        dist[start] = 0
        q = deque([start])
        bfs_order = []
        while q:
            u = q.popleft()
            bfs_order.append(u)
            for v in edges[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        # Assign slots: center = start gets middle slot
        # We'll assign slots from center outward by BFS order
        # Actually, we want to place closer nodes near center.
        # Sort by distance, then assign slots from center outward.
        nodes_by_dist = sorted(range(n), key=lambda x: dist[x])
        # Place them: first node (start) gets slot n//2+1 (1-indexed)
        # Then place others alternating left/right
        slot = [0]*n
        left = n//2
        right = n//2 + 1
        # start at center
        slot[start] = n//2 + 1
        # For others, fill from closest to farthest
        placed = {start}
        for node in nodes_by_dist:
            if node in placed:
                continue
            # place on left if possible, else right
            if left >= 1:
                slot[node] = left
                left -= 1
            else:
                slot[node] = right
                right += 1
            placed.add(node)
        
        # compute cost
        cost = 0
        for u in range(n):
            for v in edges[u]:
                if u < v:
                    cost += abs(slot[u] - slot[v])
        if cost <= B:
            print("YES")
            print(" ".join(str(x) for x in slot))
            return
    
    print("NO")

if __name__ == "__main__":
    solve()