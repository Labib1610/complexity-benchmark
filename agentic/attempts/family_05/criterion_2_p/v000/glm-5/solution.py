import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # For each specialist x, collect the set of allowed time slots z.
    # Since machine y is fixed per specialist, we just need to assign each specialist
    # a distinct time slot from its allowed set.
    allowed_slots = [set() for _ in range(k + 1)]
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        allowed_slots[x].add(z)
    
    # Hopcroft-Karp style bipartite matching: left = specialists 1..k, right = slots 1..k
    match_left = [0] * (k + 1)   # match_left[x] = z assigned to specialist x
    match_right = [0] * (k + 1)  # match_right[z] = x assigned to slot z
    dist = [0] * (k + 1)
    INF = float('inf')
    NIL = 0
    
    def bfs():
        queue = deque()
        for x in range(1, k + 1):
            if match_left[x] == NIL:
                dist[x] = 0
                queue.append(x)
            else:
                dist[x] = INF
        dist[NIL] = INF
        while queue:
            x = queue.popleft()
            if dist[x] < dist[NIL]:
                for z in allowed_slots[x]:
                    y = match_right[z]
                    if dist[y] == INF:
                        dist[y] = dist[x] + 1
                        queue.append(y)
        return dist[NIL] != INF
    
    def dfs(x):
        if x != NIL:
            for z in allowed_slots[x]:
                y = match_right[z]
                if dist[y] == dist[x] + 1 and dfs(y):
                    match_left[x] = z
                    match_right[z] = x
                    return True
            dist[x] = INF
            return False
        return True
    
    matching = 0
    while bfs():
        for x in range(1, k + 1):
            if match_left[x] == NIL:
                if dfs(x):
                    matching += 1
    
    if matching < k:
        print("NO")
        return
    
    print("YES")
    out_lines = []
    for x in range(1, k + 1):
        z = match_left[x]
        # The machine y for specialist x: since each specialist has exactly one fixed machine
        # and all distinct, y == x by the problem's promise (specialist i -> machine i).
        # But to be safe, we can output y = x as per the fixed pairing.
        out_lines.append(f"{x} {x} {z}")
    sys.stdout.write("\n".join(out_lines) + "\n")

solve()