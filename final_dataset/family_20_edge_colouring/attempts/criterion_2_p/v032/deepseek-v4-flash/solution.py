import sys
from collections import deque

input = sys.stdin.readline

def solve():
    nL, nR, m = map(int, input().split())
    edges = []
    adjL = [[] for _ in range(nL + 1)]
    adjR = [[] for _ in range(nR + 1)]
    
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        adjL[u].append((v, i))
        adjR[v].append((u, i))
    
    # Compute Δ
    delta = 0
    for u in range(1, nL + 1):
        delta = max(delta, len(adjL[u]))
    for v in range(1, nR + 1):
        delta = max(delta, len(adjR[v]))
    
    color = [0] * m
    # colorL[u][c] = edge index colored c at left node u
    # colorR[v][c] = edge index colored c at right node v
    colorL = [dict() for _ in range(nL + 1)]
    colorR = [dict() for _ in range(nR + 1)]
    
    for idx, (u, v) in enumerate(edges):
        # find smallest free color at u and v
        usedL = set(colorL[u].keys())
        usedR = set(colorR[v].keys())
        c = 1
        while c in usedL or c in usedR:
            c += 1
        # assign color c
        color[idx] = c
        colorL[u][c] = idx
        colorR[v][c] = idx
        
        # resolve conflicts via alternating path
        while True:
            # conflict at left?
            if c in colorL[u] and colorL[u][c] != idx:
                # find edge conflicting at left
                e2 = colorL[u][c]
                u2, v2 = edges[e2]
                # recolor e2 to a free color at v2
                usedR2 = set(colorR[v2].keys())
                c2 = 1
                while c2 in usedR2 or c2 == c:
                    c2 += 1
                # remove old color from v2
                del colorR[v2][c]
                color[e2] = c2
                colorR[v2][c2] = e2
                # now e2 has color c2, conflict may be at left u2
                # update colorL for u2
                if c in colorL[u2]:
                    del colorL[u2][c]
                colorL[u2][c2] = e2
                # continue with e2 at left u2
                idx = e2
                u = u2
                c = c2
                continue
            # conflict at right?
            if c in colorR[v] and colorR[v][c] != idx:
                e2 = colorR[v][c]
                u2, v2 = edges[e2]
                # recolor e2 to a free color at u2
                usedL2 = set(colorL[u2].keys())
                c2 = 1
                while c2 in usedL2 or c2 == c:
                    c2 += 1
                del colorL[u2][c]
                color[e2] = c2
                colorL[u2][c2] = e2
                if c in colorR[v2]:
                    del colorR[v2][c]
                colorR[v2][c2] = e2
                idx = e2
                v = v2
                c = c2
                continue
            break
    
    print("YES")
    print(" ".join(map(str, color)))

if __name__ == "__main__":
    solve()