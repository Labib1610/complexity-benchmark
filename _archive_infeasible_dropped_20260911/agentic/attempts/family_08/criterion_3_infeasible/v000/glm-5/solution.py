import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    k = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for i in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].append((v, i))
        adj[v].append((u, i))
        edges.append((u, v))
    
    match = [0] * (n + 1)  # match[v] = edge index + 1, 0 means unmatched
    edge_used = [False] * m
    visited = [0] * (n + 1)
    timestamp = 0
    
    def augment(u):
        nonlocal timestamp
        visited[u] = timestamp
        for v, eid in adj[u]:
            if edge_used[eid]:
                continue
            if match[v] == 0:
                match[u] = eid + 1
                match[v] = eid + 1
                edge_used[eid] = True
                return True
            # v is matched, try to augment from v's partner
            w = edges[match[v] - 1][0] if edges[match[v] - 1][1] == v else edges[match[v] - 1][1]
            if visited[w] != timestamp and augment(w):
                match[u] = eid + 1
                match[v] = eid + 1
                edge_used[eid] = True
                return True
        return False
    
    result = []
    for i in range(m):
        u, v = edges[i]
        if match[u] == 0 and match[v] == 0:
            match[u] = i + 1
            match[v] = i + 1
            edge_used[i] = True
            result.append(i)
            if len(result) >= k + 1:
                break
        elif match[u] == 0:
            timestamp += 1
            if augment(v):
                result.append(i)
                if len(result) >= k + 1:
                    break
            # If augment fails, edge i is just skipped
        elif match[v] == 0:
            timestamp += 1
            if augment(u):
                result.append(i)
                if len(result) >= k + 1:
                    break
        # else both matched, skip for simplicity
    
    for eid in result[:k+1]:
        print(f"{edges[eid][0]} {edges[eid][1]}")

solve()