import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * n
    set1 = []
    set2 = []
    
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            set1.append(i)
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        if color[v] == 0:
                            set1.append(v)
                        else:
                            set2.append(v)
                        q.append(v)
    
    # Isolated vertices are those with degree 0
    isolated = [i for i in range(n) if not adj[i]]
    
    # Try to pick from larger set
    if len(set1) >= k:
        print("YES")
        print(" ".join(str(x+1) for x in set1[:k]))
        return
    if len(set2) >= k:
        print("YES")
        print(" ".join(str(x+1) for x in set2[:k]))
        return
    
    # Need to combine
    # Take all from larger set, then add isolated vertices
    if len(set1) >= len(set2):
        large = set1
        small = set2
    else:
        large = set2
        small = set1
    
    # We can take all from large, and then add isolated vertices
    # But isolated vertices are already in one of the sets (they were colored)
    # Actually isolated vertices have no edges, so they can be added freely.
    # They are already in either set1 or set2.
    # So we can just take all from large, then add from small that are isolated.
    # But isolated vertices are in small or large already. We can just take from small if they are isolated.
    
    # Let's collect isolated from small
    isolated_in_small = [v for v in small if not adj[v]]
    
    if len(large) + len(isolated_in_small) >= k:
        take = large + isolated_in_small
        print("YES")
        print(" ".join(str(x+1) for x in take[:k]))
        return
    
    print("NO")

if __name__ == "__main__":
    solve()