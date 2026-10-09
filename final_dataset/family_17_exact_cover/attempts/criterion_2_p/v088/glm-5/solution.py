import sys
from collections import deque
input_raw = sys.stdin.read().split()
ptr = 0

def get_int():
    global ptr
    ptr += 1
    return int(input_raw[ptr-1])

q = get_int()
t = get_int()

adj = [[] for _ in range(q + 1)]
for _ in range(t):
    u = get_int()
    v = get_int()
    adj[u].append(v)
    
# Hopcroft-Karp Algorithm for Maximum Matching
# Left set: transmitters 1..q
# Right set: receivers q+1..2q
# We map right nodes to 1..q for the arrays

match_l = [0] * (q + 1)
match_r = [0] * (q + 1)
dist = [0] * (q + 1)
NIL = 0

def bfs():
    dq = deque()
    for u in range(1, q + 1):
        if match_l[u] == NIL:
            dist[u] = 0
            dq.append(u)
        else:
            dist[u] = -1
    dist[NIL] = -1
    
    while dq:
        u = dq.popleft()
        if dist[u] < dist[NIL]:
            for v in adj[u]:
                v_mapped = v - q
                if match_r[v_mapped] != NIL and dist[match_r[v_mapped]] == -1:
                    dist[match_r[v_mapped]] = dist[u] + 1
                    dq.append(match_r[v_mapped])
                elif match_r[v_mapped] == NIL:
                    dist[NIL] = dist[u] + 1
    return dist[NIL] != -1

def dfs(u):
    if u != NIL:
        for v in adj[u]:
            v_mapped = v - q
            if match_r[v_mapped] == NIL or (dist[match_r[v_mapped]] == dist[u] + 1 and dfs(match_r[v_mapped])):
                match_l[u] = v
                match_r[v_mapped] = u
                return True
        dist[u] = -1
        return False
    return True

matching_size = 0
while bfs():
    for u in range(1, q + 1):
        if match_l[u] == NIL:
            if dfs(u):
                matching_size += 1

if matching_size != q:
    sys.stdout.write("NO\n")
else:
    sys.stdout.write("YES\n")
    for u in range(1, q + 1):
        sys.stdout.write(f"{u} {match_l[u]}\n")