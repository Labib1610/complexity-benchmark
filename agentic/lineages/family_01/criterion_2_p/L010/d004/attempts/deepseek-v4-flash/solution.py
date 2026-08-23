import sys
from collections import deque

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
    
    color = [-1] * n
    final = [0] * n
    
    for start in range(n):
        if color[start] != -1:
            continue
        # BFS to collect component
        q = deque([start])
        color[start] = 0
        comp = []
        ok = True
        while q:
            u = q.popleft()
            comp.append(u)
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                elif color[v] == color[u]:
                    ok = False
        if not ok:
            print("NO")
            return
        
        # Now we have a component with colors 0/1.
        # We need to decide whether to keep as is (0->1, 1->2) or swap (0->2, 1->1)
        # to get lexicographically smaller for this component.
        # Build two candidate assignments for this component.
        cand1 = [0] * n  # keep: color 0 -> 1, color 1 -> 2
        cand2 = [0] * n  # swap: color 0 -> 2, color 1 -> 1
        for u in comp:
            if color[u] == 0:
                cand1[u] = 1
                cand2[u] = 2
            else:
                cand1[u] = 2
                cand2[u] = 1
        
        # Compare lexicographically for this component only
        # We compare the sequence of assignments for nodes in comp, sorted by index.
        comp_sorted = sorted(comp)
        better = None
        for cand in (cand1, cand2):
            if better is None:
                better = cand
            else:
                # compare
                for idx in comp_sorted:
                    if cand[idx] < better[idx]:
                        better = cand
                        break
                    elif cand[idx] > better[idx]:
                        break
        # Assign better to ans
        for u in comp:
            ans[u] = better[u]
    
    print("YES")
    print(' '.join(str(x) for x in ans))

if __name__ == "__main__":
    solve()