import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    # adj[x] = set of time slots z that specialist x (with its machine) can use
    adj = [set() for _ in range(k + 1)]
    
    for _ in range(t):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        z = int(input_data[idx]); idx += 1
        adj[x].add(z)
    
    # Hopcroft-Karp: match specialists (1..k) to time slots (1..k)
    # pair_u[x] = matched time slot for specialist x, or 0
    # pair_z[z] = matched specialist for time slot z, or 0
    pair_u = [0] * (k + 1)
    pair_z = [0] * (k + 1)
    dist = [0] * (k + 1)
    NIL = 0
    INF = float('inf')
    
    def bfs():
        queue = deque()
        for u in range(1, k + 1):
            if pair_u[u] == NIL:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        dist[NIL] = INF
        while queue:
            u = queue.popleft()
            if dist[u] < dist[NIL]:
                for z in adj[u]:
                    v = pair_z[z]
                    if v == 0:
                        if dist[NIL] == INF:
                            dist[NIL] = dist[u] + 1
                    else:
                        if dist[v] == INF:
                            dist[v] = dist[u] + 1
                            queue.append(v)
        return dist[NIL] != INF
    
    def dfs(u):
        if u != NIL:
            for z in adj[u]:
                v = pair_z[z]
                if v == 0:
                    if dist[NIL] == dist[u] + 1:
                        if dfs(NIL):
                            pair_u[u] = z
                            pair_z[z] = u
                            return True
                else:
                    if dist[v] == dist[u] + 1:
                        if dfs(v):
                            pair_u[u] = z
                            pair_z[z] = u
                            return True
            dist[u] = INF
            return False
        return True
    
    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pair_u[u] == NIL:
                if dfs(u):
                    matching += 1
    
    if matching == k:
        # Find the machine for each specialist
        # We need to re-read to get x->y mapping, but we already have adj
        # Actually we need the machine y for each specialist x
        # Let me re-read the input
        idx2 = 2
        machine_of = [0] * (k + 1)
        for _ in range(t):
            x = int(input_data[idx2]); idx2 += 1
            y = int(input_data[idx2]); idx2 += 1
            z = int(input_data[idx2]); idx2 += 1
            machine_of[x] = y
        
        out = ["YES"]
        for x in range(1, k + 1):
            z = pair_u[x]
            y = machine_of[x]
            out.append(f"{x} {y} {z}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

solve()