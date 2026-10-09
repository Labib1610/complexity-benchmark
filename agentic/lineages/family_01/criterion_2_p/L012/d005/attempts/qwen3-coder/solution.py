import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        # No connections, all independent. Choose lex smallest: all 1s
        print("YES")
        print(' '.join(['1']*n))
        return
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    edge_map = defaultdict(list)
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        edge_map[u].append(v)
        edge_map[v].append(u)
    
    # For each component, we need to check bipartiteness
    color = [-1] * (n + 1)
    assignment = [0] * (n + 1)  # 0 means unassigned
    
    visited = [False] * (n + 1)
    
    def bfs_check(start):
        queue = deque()
        queue.append(start)
        color[start] = 0
        comp_nodes = []
        
        while queue:
            node = queue.popleft()
            if visited[node]:
                continue
            visited[node] = True
            comp_nodes.append(node)
            for nei in adj[node]:
                if color[nei] == -1:
                    color[nei] = 1 - color[node]
                    queue.append(nei)
                elif color[nei] == color[node]:
                    return False, []
        return True, comp_nodes
    
    # Process each connected component
    for i in range(1, n+1):
        if not visited[i] and adj[i]:
            is_bipartite, nodes = bfs_check(i)
            if not is_bipartite:
                print("NO")
                return
                
    # Now assign values based on bipartition
    # We want to minimize sum s_i * 3^(n-i)
    # So earlier indices should be 1 if possible
    
    # Re-initialize for actual assignment
    assignment = [0] * (n + 1)
    visited_assign = [False] * (n + 1)
    
    def assign_component(start):
        # Assign based on color: color 0 -> mode 1, color 1 -> mode 2 or vice versa
        # Try both and pick the lexicographically smaller one
        c0_nodes = []
        c1_nodes = []
        temp_visited = [False] * (n + 1)
        queue = deque()
        queue.append(start)
        temp_color = [-1] * (n + 1)
        temp_color[start] = 0
        
        while queue:
            node = queue.popleft()
            if temp_visited[node]:
                continue
            temp_visited[node] = True
            if temp_color[node] == 0:
                c0_nodes.append(node)
            else:
                c1_nodes.append(node)
            for nei in adj[node]:
                if temp_color[nei] == -1:
                    temp_color[nei] = 1 - temp_color[node]
                    queue.append(nei)
                elif temp_color[nei] == temp_color[node]:
                    # Should not happen as we already checked bipartiteness
                    pass
                    
        # Try assigning c0=1,c1=2 and c0=2,c1=1
        def get_val(assign):
            val = 0
            for idx in range(1, n+1):
                if assign[idx] == 1:
                    val += 3**(n - idx)
            return val
            
        def check_valid(c0_val, c1_val):
            # Check if this assignment satisfies the constraint
            temp_assign = [0] * (n + 1)
            for x in c0_nodes:
                temp_assign[x] = c0_val
            for x in c1_nodes:
                temp_assign[x] = c1_val
                
            for node in c0_nodes + c1_nodes:
                if temp_assign[node] == 0:
                    return False, None
                k = len(edge_map[node])
                if k == 0:
                    continue
                s_node = temp_assign[node]
                neighbor_sum = 0
                for nei in edge_map[node]:
                    if temp_assign[nei] == 0:
                        return False, None
                    neighbor_sum += temp_assign[nei]
                if neighbor_sum != k * (3 - s_node):
                    return False, None
            return True, temp_assign
            
        valid1, assign1 = check_valid(1, 2)
        valid2, assign2 = check_valid(2, 1)
        
        if not valid1 and not valid2:
            return False, []
        elif valid1 and not valid2:
            return True, assign1
        elif not valid1 and valid2:
            return True, assign2
        else:
            # Both valid, choose the one with smaller sum
            val1 = sum(assign1[i] * (3 ** (n - i)) for i in range(1, n+1))
            val2 = sum(assign2[i] * (3 ** (n - i)) for i in range(1, n+1))
            if val1 <= val2:
                return True, assign1
            else:
                return True, assign2
                
        return True, assign1  # fallback
    
    # Assign for each component
    result_assignment = [0] * (n + 1)
    component_processed = [False] * (n + 1)
    
    for i in range(1, n+1):
        if not component_processed[i] and adj[i]:
            # Do BFS to get component
            comp_nodes = []
            queue = deque()
            queue.append(i)
            temp_vis = [False] * (n + 1)
            
            while queue:
                node = queue.popleft()
                if temp_vis[node] or component_processed[node]:
                    continue
                temp_vis[node] = True
                component_processed[node] = True
                comp_nodes.append(node)
                for nei in adj[node]:
                    if not temp_vis[nei] and not component_processed[nei]:
                        queue.append(nei)
                        
            # Now process this component
            # Use the same logic as above but isolated
            temp_adj = defaultdict(list)
            for u in comp_nodes:
                for v in adj[u]:
                    if v in comp_nodes:
                        temp_adj[u].append(v)
                        
            temp_color = {node: -1 for node in comp_nodes}
            start_node = comp_nodes[0]
            temp_color[start_node] = 0
            queue = deque([start_node])
            c0_nodes = []
            c1_nodes = []
            
            while queue:
                node = queue.popleft()
                if temp_color[node] == 0:
                    c0_nodes.append(node)
                else:
                    c1_nodes.append(node)
                for nei in temp_adj[node]:
                    if temp_color[nei] == -1:
                        temp_color[nei] = 1 - temp_color[node]
                        queue.append(nei)
                    elif temp_color[nei] == temp_color[node]:
                        print("NO")
                        return
                        
            # Try both assignments
            def try_assign(a, b):
                temp_ass = {}
                for x in c0_nodes:
                    temp_ass[x] = a
                for x in c1_nodes:
                    temp_ass[x] = b
                    
                for node in comp_nodes:
                    k = len(temp_adj[node])
                    if k == 0:
                        continue
                    s_node = temp_ass[node]
                    neighbor_sum = sum(temp_ass[nei] for nei in temp_adj[node])
                    if neighbor_sum != k * (3 - s_node):
                        return False, None
                return True, temp_ass
                
            valid1, ass1 = try_assign(1, 2)
            valid2, ass2 = try_assign(2, 1)
            
            chosen_ass = None
            if not valid1 and not valid2:
                print("NO")
                return
            elif valid1 and not valid2:
                chosen_ass = ass1
            elif not valid1 and valid2:
                chosen_ass = ass2
            else:
                # Both valid, compare sums
                val1 = sum(ass1[node] * (3 ** (n - node)) for node in comp_nodes)
                val2 = sum(ass2[node] * (3 ** (n - node)) for node in comp_nodes)
                chosen_ass = ass1 if val1 <= val2 else ass2
                
            for node in comp_nodes:
                result_assignment[node] = chosen_ass[node]
                
    # For isolated nodes (no connections), assign 1
    for i in range(1, n+1):
        if result_assignment[i] == 0:
            result_assignment[i] = 1
            
    print("YES")
    print(' '.join(str(result_assignment[i]) for i in range(1, n+1)))

if __name__ == "__main__":
    main()