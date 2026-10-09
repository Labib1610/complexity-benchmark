import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    edge_indices = defaultdict(list)
    
    for i in range(m):
        u = int(data[2 + 2*i])
        v = int(data[2 + 2*i + 1])
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
        edge_indices[(u,v)].append(i)
        edge_indices[(v,u)].append(i)
    
    # We want the global interference to be 5^m
    # Each multiplier M_{u,v} = (s_u | s_v) + 2
    # s_u, s_v in {1,2}
    # Possible values:
    # s_u=1, s_v=1: 1|1 = 1, M=3
    # s_u=1, s_v=2: 1|2 = 3, M=5
    # s_u=2, s_v=1: 2|1 = 3, M=5
    # s_u=2, s_v=2: 2|2 = 2, M=4
    # So M can be 3, 4, or 5.
    # We want product of all M to be 5^m.
    # This means ALL M must be 5. Because:
    # If any M is 3 or 4, the product will have factors of 3 or 4, and cannot be 5^m.
    # So for every edge (u,v), we must have (s_u | s_v) + 2 = 5 => s_u | s_v = 3
    # This happens when (s_u, s_v) is (1,2) or (2,1)
    
    # So this is a 2-coloring problem where each edge must connect different colors.
    # This is equivalent to checking if the graph is bipartite.
    
    color = [-1] * (n + 1)
    result = [0] * (n + 1)
    
    for start in range(1, n + 1):
        if color[start] == -1:
            # BFS to check bipartiteness and assign lexicographically smallest coloring
            queue = deque()
            queue.append(start)
            # To get lexicographically smallest, we try to assign 1 first
            color[start] = 1
            result[start] = 1
            
            while queue:
                u = queue.popleft()
                current_color = color[u]
                next_color = 2 if current_color == 1 else 1
                
                for v, idx in adj[u]:
                    if color[v] == -1:
                        color[v] = next_color
                        result[v] = next_color
                        queue.append(v)
                    elif color[v] == current_color:
                        # Not bipartite
                        print("NO")
                        return
    
    # If we reach here, the graph is bipartite and we have a valid coloring
    # The result array gives us the assignment
    print("YES")
    print(" ".join(str(result[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()