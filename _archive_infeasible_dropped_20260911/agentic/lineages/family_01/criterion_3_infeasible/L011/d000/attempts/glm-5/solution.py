import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]); v = int(input_data[idx+1])
        idx += 2
        if u < v:
            adj[u].add(v)
        else:
            adj[v].add(u)
    
    for a in range(1, n + 1):
        neighbors = adj[a]
        if len(neighbors) < 2:
            continue
        sorted_neighbors = sorted(neighbors)
        for i in range(len(sorted_neighbors)):
            b = sorted_neighbors[i]
            for j in range(i + 1, len(sorted_neighbors)):
                c = sorted_neighbors[j]
                if c in adj[b]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()