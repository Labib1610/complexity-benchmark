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
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        adj[u].append((v, len(edges) - 1))
        adj[v].append((u, len(edges) - 1))
        index += 2
    
    # 0 means unset, 1 and 2 are the two states
    state = [0] * (n + 1)
    queue = deque()
    
    # We will try to assign values starting from node 1 to ensure lex smallest
    # But we need to handle disconnected components properly
    
    # Let's do BFS/DFS for each component
    visited = [False] * (n + 1)
    
    for start_node in range(1, n + 1):
        if visited[start_node]:
            continue
            
        # For each connected component, we can start with state 1 for the first node
        state[start_node] = 1
        queue.append(start_node)
        visited[start_node] = True
        
        while queue:
            u = queue.popleft()
            current_state = state[u]
            
            # The neighbor must be either current_state * 2 or current_state / 2
            # Since states are 1 or 2:
            # If current_state == 1, neighbor must be 2
            # If current_state == 2, neighbor must be 1
            required_neighbor_state = 2 if current_state == 1 else 1
            
            for v, edge_idx in adj[u]:
                if not visited[v]:
                    state[v] = required_neighbor_state
                    visited[v] = True
                    queue.append(v)
                else:
                    # Check consistency
                    if state[v] != required_neighbor_state:
                        print("NO")
                        return
    
    # Final check: verify all edges satisfy the condition
    for u, v in edges:
        su = state[u]
        sv = state[v]
        if not (su == 2 * sv or sv == 2 * su):
            print("NO")
            return
            
    print("YES")
    print(" ".join(map(str, state[1:])))

if __name__ == "__main__":
    main()