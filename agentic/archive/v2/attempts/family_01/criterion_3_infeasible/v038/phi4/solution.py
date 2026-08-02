from sys import stdin

def minimal_incompatibility_certificate():
    input = stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = {}
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        if u > v:
            u, v = v, u
        if u not in edges:
            edges[u] = set()
        edges[u].add(v)
        index += 2
    
    # Find the lexicographically smallest triplet (a, b, c)
    for a in range(1, n + 1):
        if a in edges:
            for b in sorted(edges[a]):
                if b > a and b in edges:
                    for c in sorted(edges[b]):
                        if c > b and c in edges[a]:
                            print(a, b, c)
                            return

minimal_incompatibility_certificate()