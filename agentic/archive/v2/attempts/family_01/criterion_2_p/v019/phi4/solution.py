import sys

def relay_channel_allocation():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    m = int(data[index + 1])
    index += 2
    
    edges = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges[u].append(v)
        edges[v].append(u)
        index += 2

    config = [0] * (n + 1)

    def is_valid(node, color):
        for neighbor in edges[node]:
            if config[neighbor] == color:
                return False
        return True

    from heapq import heappush, heappop

    # Using a min-heap to ensure lexicographical order
    heap = [(0, i) for i in range(1, n + 1)]
    
    while heap:
        color, node = heappop(heap)
        
        if config[node] != 0:
            continue
        
        if not is_valid(node, color):
            print("NO")
            return

        config[node] = color + 1
        next_color = (color + 1) % 2
        
        for neighbor in edges[node]:
            heappush(heap, (next_color, neighbor))
    
    # If we reach this point, a valid configuration is found
    print("YES")
    print(' '.join(map(str, config[1:])))

relay_channel_allocation()