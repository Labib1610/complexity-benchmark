import sys

def main():
    input = sys.stdin.read
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
    
    edges.sort()
    
    adjacency_list = {i: set() for i in range(1, n+1)}
    for u, v in edges:
        adjacency_list[u].add(v)
        adjacency_list[v].add(u)
    
    for u, v in edges:
        if v - u == 1:
            continue
        for w in adjacency_list[u]:
            if w > v and w in adjacency_list[v]:
                print(u, v, w)
                return

if __name__ == "__main__":
    main()