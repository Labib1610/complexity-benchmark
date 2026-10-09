import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    graph = [set() for _ in range(n+1)]
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
        graph[u].add(v)
        graph[v].add(u)
    
    # For each node, sort its neighbors
    for i in range(1, n+1):
        graph[i] = sorted(graph[i])
    
    # We want the lexicographically smallest triple (a,b,c) where a<b<c and all pairs conflict
    # Iterate through all edges (a,b) with a < b
    # For each such edge, look for a node c such that c > b and c is connected to both a and b
    
    best = None
    
    for a in range(1, n+1):
        neighbors_a = graph[a]
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            if b <= a:
                continue
            neighbors_b = graph[b]
            # Use two pointers to find common neighbors of a and b that are > b
            j = 0
            k = 0
            while j < len(neighbors_a) and k < len(neighbors_b):
                c_a = neighbors_a[j]
                c_b = neighbors_b[k]
                if c_a == c_b:
                    c = c_a
                    if c > b:
                        # Found a valid triple (a, b, c)
                        print(a, b, c)
                        return
                    elif c < b:
                        j += 1
                        k += 1
                    else:  # c == b
                        j += 1
                        k += 1
                elif c_a < c_b:
                    j += 1
                else:
                    k += 1

if __name__ == "__main__":
    main()