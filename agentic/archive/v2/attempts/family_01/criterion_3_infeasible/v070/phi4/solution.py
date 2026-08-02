import sys

def find_mutually_interlocking_triplet():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    m = int(data[index + 1])
    index += 2
    
    # Create adjacency list for the graph
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index + 1]) - 1
        graph[u].append(v)
        graph[v].append(u)
        index += 2
    
    # Sort neighbors to ensure lexicographical order
    for neighbors in graph:
        neighbors.sort()
    
    # Find the smallest triplet (a, b, c) with a < b < c and all pairs interlocking
    for a in range(n):
        for b in graph[a]:
            if b > a:
                for c in graph[b]:
                    if c > b and a in graph[c]:
                        print(a + 1, b + 1, c + 1)
                        return

if __name__ == "__main__":
    find_mutually_interlocking_triplet()