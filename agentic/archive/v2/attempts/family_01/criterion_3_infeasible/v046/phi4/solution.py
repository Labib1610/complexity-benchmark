import sys
input = sys.stdin.read

def find_earliest_failure(n, m, edges):
    interference = [set() for _ in range(n + 1)]
    
    for u, v in edges:
        interference[u].add(v)
        interference[v].add(u)

    # Find the smallest lexicographical triple (a, b, c) such that a < b < c
    for a in range(1, n + 1):
        for b in interference[a]:
            if b > a:
                for c in interference[a]:
                    if c > b and c in interference[b]:
                        return a, b, c

def main():
    data = input().split()
    
    index = 0
    n = int(data[index])
    m = int(data[index + 1])
    index += 2
    
    edges = []
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        index += 2

    result = find_earliest_failure(n, m, edges)
    print(result[0], result[1], result[2])

if __name__ == "__main__":
    main()