import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    
    color = [-1] * n
    components = []
    
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            comp = []
            ok = True
            while q:
                u = q.popleft()
                comp.append(u)
                for v in g[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)
                    elif color[v] == color[u]:
                        ok = False
            if not ok:
                print("NO")
                return
            components.append(comp)
    
    # Now we have components and a base coloring (color 0 or 1)
    # We need to possibly flip some components to get smallest lexicographic sequence
    
    assignment = [-1] * n
    for comp in components:
        # Two ways: keep colors as-is, or flip them
        # We'll build both and choose smaller lexicographically considering only this component
        comp_set = set(comp)
        # Build sequences for this component based on color
        seq1 = [None] * n
        for u in comp:
            seq1[u] = 1 if color[u] == 0 else 2
        seq2 = [None] * n
        for u in comp:
            seq2[u] = 2 if color[u] == 0 else 1
        
        # Compare assignments for this comp, choose smaller lexicographically
        # Pick whichever has a 1 earlier within this component
        idx = min(comp)
        if seq1[idx] <= seq2[idx]:
            for u in comp:
                assignment[u] = seq1[u]
        else:
            for u in comp:
                assignment[u] = seq2[u]
    
    # Now check the whole assignment for lexicographic minimality globally
    # We might need a second pass: because choosing per component might not be globally best
    # Actually it's fine: each component independent, lexicographic order is determined by index order
    # So we choose for each component the orientation that gives a '1' at the smallest index in that component
    # But two components can interleave indices; first index where they differ decides globally.
    # Since components are independent, orientation choice can affect index ordering across components.
    # Need to refine: we must choose orientation per component to minimize whole sequence lexicographically.
    
    # Do it component-wise but in order of smallest index in the component, decide orientation to put 1 earlier if possible.
    # Actually, the correct way: for each node from 0..n-1, if assignment not yet fixed, attempt to set 1 if possible.
    
    # So let's run BFS/DFS again but assign greedily to minimize lexicographic order.
    
    color = [-1] * n
    final = [0] * n
    
    for i in range(n):
        if color[i] == -1:
            # BFS this component
            color[i] = 0
            q = deque([i])
            comp = []
            while q:
                u = q.popleft()
                comp.append(u)
                for v in g[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)
            # Now try orientation that gives node i (smallest index in this comp) color 1 if possible
            # color[i]=0 originally, so setting color[i]=1 means flip all
            # We want lexicographically smallest for whole sequence
            # First see if we can set final[i]=1 without conflict
            # Since this is first occurrence of this component, the decision is global
            # Try both orientations and pick smaller final array over this comp
            comp_set = set(comp)
            seqA = [None]*n
            seqB = [None]*n
            for u in comp:
                seqA[u] = 1 if color[u] == 0 else 2
                seqB[u] = 1 if color[u] == 1 else 2
            # Compare seqA and seqB at earliest differing index in whole array
            best = seqA
            for idx in range(n):
                if seqA[idx] is not None and seqB[idx] is not None:
                    if seqA[idx] != seqB[idx]:
                        if seqA[idx] > seqB[idx]:
                            best = seqB
                        break
            for u in comp:
                final[u] = best[u]
    
    print("YES")
    print(" ".join(str(x) for x in final))

if __name__ == "__main__":
    solve()