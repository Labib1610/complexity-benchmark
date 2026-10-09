import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    edges = []
    index = 3
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        edges.append((u, v))
        index += 2
    
    if m == 0:
        # No edges, any k nodes will do
        if k <= n:
            print("YES")
            print(' '.join(map(str, range(1, k+1))))
        else:
            print("NO")
        return
    
    # Build adjacency list
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # Graph is bipartite, find the two partitions
    color = {}
    nodes = list(adj.keys()) if adj else []
    if not nodes and n > 0:
        nodes = [1]
    
    visited = set()
    partition = {0: [], 1: []}
    
    # We'll do BFS to 2-color the graph
    all_nodes = set()
    for u, v in edges:
        all_nodes.add(u)
        all_nodes.add(v)
    
    unvisited = set(range(1, n+1))
    while unvisited:
        start = next(iter(unvisited))
        queue = deque([start])
        color[start] = 0
        partition[0].append(start)
        visited.add(start)
        unvisited.remove(start)
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            opposite_color = 1 - current_color
            
            for neighbor in adj[node]:
                if neighbor not in color:
                    color[neighbor] = opposite_color
                    partition[opposite_color].append(neighbor)
                    visited.add(neighbor)
                    unvisited.discard(neighbor)
                    queue.append(neighbor)
                elif color[neighbor] == current_color:
                    # This should not happen as per problem statement
                    print("NO")
                    return
        
        if unvisited:
            continue
        else:
            break
    
    # If some nodes have no edges, they can be added to either partition
    all_present = set(color.keys())
    missing = set(range(1, n+1)) - all_present
    # Add missing nodes to partition 0 arbitrarily
    partition[0].extend(missing)
    
    # Now we have two independent sets (partitions)
    # We want to pick k nodes with no edges between them
    # So we pick from the larger partition if possible
    
    part0 = partition[0]
    part1 = partition[1]
    
    if len(part0) >= k:
        print("YES")
        print(' '.join(map(str, part0[:k])))
    elif len(part1) >= k:
        print("YES")
        print(' '.join(map(str, part1[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    main()