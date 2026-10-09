import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr]); ptr +=1
    m = int(input[ptr]); ptr +=1
    k = int(input[ptr]); ptr +=1

    degrees = [0] * (n + 1)
    edges = []
    for _ in range(m):
        u = int(input[ptr]); ptr +=1
        v = int(input[ptr]); ptr +=1
        edges.append((u, v))
        degrees[u] += 1
        degrees[v] += 1

    # Sort edges by sum of degrees, then u, then v
    sorted_edges = sorted(edges, key=lambda x: (degrees[x[0]] + degrees[x[1]], x[0], x[1]))

    used = [False] * (n + 1)
    res = []
    for u, v in sorted_edges:
        if not used[u] and not used[v]:
            res.append((u, v))
            used[u] = True
            used[v] = True
            if len(res) == k + 1:
                break

    for u, v in res:
        print(u, v)

if __name__ == "__main__":
    main()