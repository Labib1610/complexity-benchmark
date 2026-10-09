from collections import defaultdict, deque

def find_maximum_matching(graph, controller_count):
    # Hopcroft-Karp algorithm implementation for maximum bipartite matching
    
    # Initialize
    pair_u = [0] * (controller_count + 1)  # 1-indexed, 0 means unmatched
    pair_v = [0] * (controller_count + 1)  # 1-indexed, 0 means unmatched
    dist = [0] * (controller_count + 1)
    
    def bfs():
        queue = deque()
        for u in range(1, controller_count + 1):
            if pair_u[u] == 0:  # If u is free
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        dist[0] = float('inf')  # 0 is the NIL node
        
        while queue:
            u = queue.popleft()
            if dist[u] < dist[0]:  # If u is not NIL
                for v in graph[u]:
                    if dist[pair_v[v]] == float('inf'):  # If pair of v is not yet reached
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])
        return dist[0] != float('inf')
    
    def dfs(u):
        if u != 0:
            for v in graph[u]:
                if dist[pair_v[v]] == dist[u] + 1:
                    if dfs(pair_v[v]):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = float('inf')
            return False
        return True
    
    matching = 0
    while bfs():
        for u in range(1, controller_count + 1):
            if pair_u[u] == 0:  # If u is free
                if dfs(u):
                    matching += 1
                    
    return matching, pair_u

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    graph = defaultdict(list)
    index = 2
    
    for _ in range(t):
        a = int(data[index])
        b = int(data[index + 1])
        # Convert platform id from range [q+1, 2q] to [1, q]
        platform_id = b - q
        graph[a].append(platform_id)
        index += 2
    
    # Find maximum matching
    matching_size, pair_u = find_maximum_matching(graph, q)
    
    # Check if perfect matching exists
    if matching_size == q:
        print("YES")
        for controller in range(1, q + 1):
            platform = pair_u[controller]
            # Convert platform id back to original range [q+1, 2q]
            print(controller, platform + q)
    else:
        print("NO")

if __name__ == "__main__":
    main()