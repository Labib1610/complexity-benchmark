import sys

# Increase recursion depth to handle up to N=40 comfortably
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

    adj = [[] for _ in range(n)]
    is_edge = [[False] * n for _ in range(n)]
    
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        adj[v].append(u)
        is_edge[u][v] = True
        is_edge[v][u] = True

    # Check for K4 (Complete graph of 4 vertices)
    # If K4 exists, the graph is not 3-colorable.
    has_k4 = False
    for i in range(n):
        for j in range(i + 1, n):
            if not is_edge[i][j]:
                continue
            
            # Find common neighbors of i and j with index > j
            common = []
            for k in range(j + 1, n):
                if is_edge[i][k] and is_edge[j][k]:
                    common.append(k)
            
            # If there are at least 2 common neighbors, check if they are connected
            if len(common) >= 2:
                for idx1 in range(len(common)):
                    for idx2 in range(idx1 + 1, len(common)):
                        u_c = common[idx1]
                        v_c = common[idx2]
                        if is_edge[u_c][v_c]:
                            has_k4 = True
                            break
                    if has_k4:
                        break
            if has_k4:
                break
        if has_k4:
            break
            
    if has_k4:
        print("NO")
        return

    final_sol = None
    assignment = [0] * n
    
    # available[i] is a bitmask of available colors for node i
    # 1 -> bit 0, 2 -> bit 1, 3 -> bit 2
    # Initially all colors are available (111 binary = 7)
    
    def backtrack(idx, available):
        nonlocal final_sol
        
        if idx == n:
            final_sol = list(assignment)
            return True
        
        # Try colors 1, 2, 3 in order to ensure lexicographically smallest solution
        for c in range(1, 4):
            # Check if color c is available for node idx
            if not ((available[idx] >> (c - 1)) & 1):
                continue
            
            # Create a copy of available colors for the next state
            new_available = list(available)
            # Mark idx as assigned (no colors available)
            new_available[idx] = 0
            
            # Track nodes assigned in this step to clear them on backtrack
            assigned_in_this_step = [idx]
            possible = True
            
            # Queue for unit propagation (forced assignments)
            q = []
            
            # Propagate the choice of c to neighbors
            for v in adj[idx]:
                # Only consider unassigned neighbors (v > idx)
                # Note: neighbors v < idx are already assigned and checked via available[idx]
                if v <= idx:
                    continue
                
                # If v has color c available, remove it
                if (new_available[v] >> (c - 1)) & 1:
                    new_available[v] &= ~(1 << (c - 1))
                    if new_available[v] == 0:
                        possible = False
                        break
                    # If only 1 color remains, v is forced to that color
                    if new_available[v] & (new_available[v] - 1) == 0:
                        q.append(v)
            
            # Process forced assignments
            if possible:
                q_ptr = 0
                while q_ptr < len(q):
                    u = q[q_ptr]
                    q_ptr += 1
                    
                    mask = new_available[u]
                    if mask == 0:
                        possible = False
                        break
                    
                    # Determine the forced color
                    c_u = 0
                    if mask & 1: c_u = 1
                    elif mask & 2: c_u = 2
                    elif mask & 4: c_u = 3
                    
                    assigned_in_this_step.append(u)
                    
                    # Propagate c_u to neighbors
                    for v in adj[u]:
                        if v <= idx:
                            continue
                        if (new_available[v] >> (c_u - 1)) & 1:
                            new_available[v] &= ~(1 << (c_u - 1))
                            if new_available[v] == 0:
                                possible = False
                                break
                            if new_available[v] & (new_available[v] - 1) == 0:
                                q.append(v)
                    if not possible:
                        break
            
            if possible:
                # Assign colors to assignment array
                assignment[idx] = c
                for u in assigned_in_this_step:
                    if u > idx:
                        # Retrieve the forced color from new_available
                        mask = new_available[u]
                        if mask & 1: assignment[u] = 1
                        elif mask & 2: assignment[u] = 2
                        elif mask & 4: assignment[u] = 3
                
                # Recurse
                if backtrack(idx + 1, new_available):
                    return True
                
                # Backtrack: clear forced assignments for nodes > idx
                # assignment[idx] will be overwritten in next iteration
                for u in assigned_in_this_step:
                    if u > idx:
                        assignment[u] = 0
            
        return False

    # Start backtracking
    if backtrack(0, [7] * n):
        print("YES")
        print(*(final_sol))
    else:
        print("NO")

if __name__ == '__main__':
    solve()