import sys
from collections import deque

input = sys.stdin.readline

def solve():
    A, B, L = map(int, input().split())
    edges = []
    degA = [0] * (A + 1)
    degB = [0] * (B + 1)
    
    for _ in range(L):
        u, v = map(int, input().split())
        edges.append((u, v))
        degA[u] += 1
        degB[v] += 1
    
    K = max(max(degA), max(degB))
    
    # adjacency list for both sides
    adjA = [[] for _ in range(A + 1)]
    adjB = [[] for _ in range(B + 1)]
    
    for idx, (u, v) in enumerate(edges):
        adjA[u].append((v, idx))
        adjB[v].append((u, idx))
    
    color = [0] * L
    
    # colorA[u][c] = which edge from u has color c
    colorA = [[-1] * (K + 1) for _ in range(A + 1)]
    colorB = [[-1] * (K + 1) for _ in range(B + 1)]
    
    for u in range(1, A + 1):
        for v, idx in adjA[u]:
            if color[idx] != 0:
                continue
            # find free color for u
            c = 1
            while colorA[u][c] != -1:
                c += 1
            # assign
            color[idx] = c
            colorA[u][c] = idx
            colorB[v][c] = idx
            
            # resolve conflicts
            v2 = v
            c2 = c
            while True:
                # find edge from v2 with color c2 that is not idx
                conflict_idx = colorB[v2][c2]
                if conflict_idx == -1 or conflict_idx == idx:
                    break
                # find new color for conflict edge
                u2, v3 = edges[conflict_idx]
                # find free color for u2
                c3 = 1
                while colorA[u2][c3] != -1:
                    c3 += 1
                # recolor conflict edge
                color[conflict_idx] = c3
                colorA[u2][c3] = conflict_idx
                colorB[v3][c3] = conflict_idx
                # remove old color from u2
                colorA[u2][c2] = -1
                colorB[v3][c2] = -1
                # move to next conflict
                v2 = v3
                c2 = c3
    
    print("YES")
    print(" ".join(map(str, color)))

if __name__ == "__main__":
    solve()