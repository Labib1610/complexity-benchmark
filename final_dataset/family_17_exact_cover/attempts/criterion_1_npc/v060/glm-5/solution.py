import sys

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    q = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    n = 3 * q
    triples = []
    for _ in range(t):
        a = int(input_data[idx]) - 1
        b = int(input_data[idx+1]) - 1
        c = int(input_data[idx+2]) - 1
        idx += 3
        triples.append((a, b, c))
    
    # degree check
    deg = [0] * n
    for (a, b, c) in triples:
        deg[a] += 1; deg[b] += 1; deg[c] += 1
    if any(d == 0 for d in deg):
        print("NO")
        return
    
    # connected components via union-find
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for (a, b, c) in triples:
        ra, rb, rc = find(a), find(b), find(c)
        # union all
        parent[rb] = ra
        parent[find(rc)] = ra  # careful: find(rc) after setting parent[rb]=ra
    ...