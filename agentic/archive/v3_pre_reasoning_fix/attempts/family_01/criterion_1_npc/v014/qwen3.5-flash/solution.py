import sys

# Increase recursion depth to handle deep recursion in backtracking if necessary
sys.setrecursionlimit(5000)

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list for the graph
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break

    # Array to store the final colors (shifts)
    colors = [0] * (n + 1)
    
    # To identify connected components
    visited = [False] * (n + 1)
    components = []
    
    # Find connected components
    for i in range(1, n + 1):
        if not visited[i]:
            comp_nodes = []
            stack = [i]
            visited[i] = True
            while stack:
                u = stack.pop()
                comp_nodes.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            components.append(comp_nodes)
    
    # Function to check if a component is bipartite and get the partition
    # Returns (is_bipartite, partition_map)
    # partition_map maps node -> 0 or 1
    def get_bipartite_info(comp_nodes):
        if not comp_nodes:
            return True, {}
        
        start = comp_nodes[0]
        part_map = {start: 0}
        queue = [start]
        idx = 0
        while idx < len(queue):
            u = queue[idx]
            idx += 1
            p = part_map[u]
            for v in adj[u]:
                if v in part_map:
                    if part_map[v] == p:
                        return False, None
                else:
                    part_map[v] = 1 - p
                    queue.append(v)
        return True, part_map

    # Backtracking function to find the lexicographically smallest 3-coloring
    # comp_nodes is assumed to be sorted
    def backtrack(idx):
        if idx == len(comp_nodes):
            return True
        
        u = comp_nodes[idx]
        for c in 1, 2, 3:
            # Check if color c is valid for u
            valid = True
            for v in adj[u]:
                if colors[v] == c:
                    valid = False
                    break
            if valid:
                colors[u] = c
                if backtrack(idx + 1):
                    return True
                colors[u] = 0
        return False

    # Process each component
    for comp in components:
        # Sort component nodes to ensure we process in lexicographical order of indices
        comp.sort()
        
        is_bip, part_map = get_bipartite_info(comp)
        
        if is_bip:
            # If bipartite, we only need to check the two 2-colorings using colors 1 and 2.
            # Any 3-coloring would be lexicographically larger or equal to one of these 2-colorings
            # (or equivalent to one with 3 replaced by 1/2).
            # Actually, we just need to compare the two 2-colorings.
            # Option 1: U -> 1, V -> 2
            # Option 2: U -> 2, V -> 1
            
            # Construct Option 1
            # We need to compare the sequences restricted to comp
            # comp is sorted.
            
            # Option 1 colors
            c1 = [0] * (n + 1)
            for u in comp:
                if part_map[u] == 0:
                    c1[u] = 1
                else:
                    c1[u] = 2
            
            # Option 2 colors
            c2 = [0] * (n + 1)
            for u in comp:
                if part_map[u] == 0:
                    c2[u] = 2
                else:
                    c2[u] = 1
            
            # Compare c1 and c2 based on the subsequence of comp nodes
            # Since comp is sorted, we compare element-wise
            chosen = None
            for u in comp:
                if c1[u] < c2[u]:
                    chosen = c1
                    break
                elif c2[u] < c1[u]:
                    chosen = c2
                    break
            else:
                # If they are identical (should not happen unless 1==2), pick one
                chosen = c1
            
            # Update global colors
            for u in comp:
                colors[u] = chosen[u]
        else:
            # If not bipartite, run backtracking to find the lexicographically smallest 3-coloring
            # Since we process nodes in increasing order of ID and try colors 1, 2, 3 in order,
            # the first solution found is the lexicographically smallest.
            if not backtrack(0):
                print("NO")
                return
            # If backtrack returns True, colors are set correctly in the global array
    
    # If we successfully assigned colors to all components
    print("YES")
    print(" ".join(map(str, colors[1:])))

if __name__ == '__main__':
    solve()