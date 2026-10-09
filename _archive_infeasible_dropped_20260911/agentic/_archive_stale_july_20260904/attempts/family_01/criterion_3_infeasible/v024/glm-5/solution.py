import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u][v] = True
        adj[v][u] = True
    
    # For each node, store its neighbors (incompatible modules)
    neighbors = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if adj[i][j]:
                neighbors[i].append(j)
                neighbors[j].append(i)
    
    # Sort neighbors for each node to help with lexicographic ordering
    for i in range(1, n + 1):
        neighbors[i].sort()
    
    # For each pair (a, b) where a < b and they are incompatible
    # Check if there exists c > b such that both (a, c) and (b, c) are incompatible
    for a in range(1, n - 1):
        for b in neighbors[a]:
            if b <= a:
                continue
            # Check for c in neighbors of both a and b, with c > b
            # Use two-pointer technique on sorted neighbor lists
            nb_a = neighbors[a]
            nb_b = neighbors[b]
            i, j = 0, 0
            len_a, len_b = len(nb_a), len(nb_b)
            while i < len_a and j < len_b:
                ca = nb_a[i]
                cb = nb_b[j]
                if ca <= b:
                    i += 1
                    continue
                if cb <= b:
                    j += 1
                    continue
                if ca == cb:
                    print(a, b, ca)
                    return
                elif ca < cb:
                    i += 1
                else:
                    j += 1

if __name__ == "__main__":
    solve()