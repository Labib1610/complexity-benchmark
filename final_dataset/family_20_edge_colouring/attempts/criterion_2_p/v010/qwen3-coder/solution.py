import sys
from collections import defaultdict
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    nP, nS, m = map(int, sys.stdin.readline().split())
    
    links = []
    primary_deg = [0] * (nP + 1)
    secondary_deg = [0] * (nS + 1)
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        links.append((u, v))
        primary_deg[u] += 1
        secondary_deg[v] += 1
    
    # Find peak concentration
    peak = max(max(primary_deg), max(secondary_deg))
    
    # For each node, maintain a set of used phases
    primary_used = [set() for _ in range(nP + 1)]
    secondary_used = [set() for _ in range(nS + 1)]
    
    result = []
    
    # Process each link in order
    for u, v in links:
        # Find a phase that is not used by either u or v
        phase = 1
        while phase in primary_used[u] or phase in secondary_used[v]:
            phase += 1
        result.append(str(phase))
        primary_used[u].add(phase)
        secondary_used[v].add(phase)
    
    print("YES")
    print(' '.join(result))

threading.Thread(target=main).start()