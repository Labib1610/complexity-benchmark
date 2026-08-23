import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[ptr])
        ptr += 1
        v = int(input_data[ptr])
        ptr += 1
        adj[u].append(v)
        adj[v].append(u)
    
    # -1: unassigned, 1: plane 1, 2: plane 2
    assignment = [-1] * (n + 1)
    
    for start in range(1, n + 1):
        if assignment[start] != -1:
            continue
        # BFS from start, assign to plane 1 for lexicographically smallest
        assignment[start] = 1
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if assignment[v] == -1:
                    assignment[v] = 3 - assignment[u]  # 1 -> 2, 2 -> 1
                    queue.append(v)
                elif assignment[v] == assignment[u]:
                    print("NO")
                    return
    
    print("YES")
    print(" ".join(map(str, assignment[1:])))

solve()