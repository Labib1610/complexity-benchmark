import sys
input = sys.stdin.read

def main():
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        if u > v:
            u, v = v, u
        edges.append((u, v))
        index += 2
    
    conflict_graph = {i: set() for i in range(1, n+1)}
    
    for u, v in edges:
        conflict_graph[u].add(v)
        conflict_graph[v].add(u)
    
    for a in range(1, n + 1):
        for b in sorted(conflict_graph[a]):
            if b > a:
                for c in sorted(conflict_graph[b]):
                    if c > b and c in conflict_graph[a]:
                        print(a, b, c)
                        return

if __name__ == "__main__":
    main()