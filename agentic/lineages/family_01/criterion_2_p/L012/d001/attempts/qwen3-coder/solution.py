import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    adj = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # For each connected component, we need to check if it's bipartite
    # and find a valid assignment.
    # The constraint is that for each edge (u,v): s[u] * s[v] = 2
    # Since s[u], s[v] ∈ {1,2}, the valid pairs are (1,2) and (2,1).
    # This means that adjacent nodes must have different values.
    # So the graph must be bipartite.
    
    color = {}
    result = [None] * (n + 1)
    
    for i in range(1, n + 1):
        if i not in color:
            # BFS to check bipartiteness and assign values
            queue = deque()
            queue.append(i)
            color[i] = 0
            # For bipartite graphs, one side gets 1, other gets 2
            # To get lexicographically smallest, we want node 1 to be 1 if possible
            # So we'll assign 1 to color 0 and 2 to color 1
            
            # But we need to be careful about the lexicographical order.
            # We want the configuration to be lexicographically smallest.
            # That means we want earlier nodes to be as small as possible.
            
            # Let's do BFS and try to assign 1 to color 0 and 2 to color 1
            # unless it violates constraints.
            
            # Actually, since the only valid assignments are (1,2) and (2,1),
            # we can model this as a 2-coloring problem where:
            # color 0 -> value 1
            # color 1 -> value 2
            # or 
            # color 0 -> value 2
            # color 1 -> value 1
            # We need to choose the option that gives lexicographically smallest result.
            
            # For the component containing node min_node_in_component,
            # we should try both options and pick the one that makes that node 1 if possible.
            
            component_nodes = []
            temp_queue = deque([i])
            visited_temp = set()
            visited_temp.add(i)
            component_nodes.append(i)
            
            while temp_queue:
                u = temp_queue.popleft()
                for v in adj[u]:
                    if v not in visited_temp:
                        visited_temp.add(v)
                        component_nodes.append(v)
                        temp_queue.append(v)
            
            min_node = min(component_nodes)
            
            # Try coloring starting with min_node as color 0
            local_color = {}
            local_color[min_node] = 0
            queue_local = deque([min_node])
            valid = True
            
            while queue_local and valid:
                u = queue_local.popleft()
                for v in adj[u]:
                    if v in local_color:
                        if local_color[v] == local_color[u]:
                            valid = False
                            break
                    else:
                        local_color[v] = 1 - local_color[u]
                        queue_local.append(v)
            
            if not valid:
                print("NO")
                return
            
            # Now decide whether to map color 0 -> 1 or 2
            # We want min_node to be as small as possible, so we want it to be 1
            # min_node has color 0, so we map color 0 -> 1, color 1 -> 2
            for node in component_nodes:
                c = local_color[node]
                if c == 0:
                    result[node] = 1
                else:
                    result[node] = 2
    
    print("YES")
    print(" ".join(map(str, result[1:])))

if __name__ == "__main__":
    main()