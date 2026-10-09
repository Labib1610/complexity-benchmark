import sys
import threading

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    p1 = []
    p2 = []
    
    idx = 2
    for i in range(j):
        p1.append(int(data[idx]))
        p2.append(int(data[idx+1]))
        idx += 2
    
    # Check JOB certificates
    for i in range(j):
        # For JOB i: u_i >= p1[i], v_i - u_i >= p1[i] + p2[i], v_i <= 2*T - p2[i]
        # From first and second: v_i >= u_i + p1[i] + p2[i] >= p1[i] + p1[i] + p2[i] = 2*p1[i] + p2[i]
        # But also v_i <= 2*T - p2[i]
        # So we need 2*p1[i] + p2[i] <= 2*T - p2[i]
        # Which simplifies to 2*p1[i] + 2*p2[i] <= 2*T => p1[i] + p2[i] <= T
        if p1[i] + p2[i] > T:
            print(f"JOB {i+1}")
            return
    
    # Check LOAD certificates
    
    # For LOAD 1: u_i >= p1[i], |u_i - u_k| >= p1[i] + p1[k], u_i <= 2*T - p1[i]
    # This is equivalent to placing points on a line with minimum distances and within [p1[i], 2*T - p1[i]]
    # Let's sort by p1 values to make checking easier
    # We can think of this as placing points in intervals [p1[i], 2*T - p1[i]] with separation p1[i] + p1[k]
    
    # A necessary condition for LOAD 1 is that the total "space" needed exceeds the available space
    # But let's use a simpler approach: if sum of all p1[i] * 2 > T, then likely unsatisfiable
    # Actually, let's compute the minimum span required
    
    # Sort indices by p1 values to check if placement is possible
    indices = list(range(j))
    indices.sort(key=lambda x: p1[x])
    
    # Try to place points greedily starting from leftmost position
    # Position of u_0 should be at least p1[indices[0]]
    # Then each subsequent point needs to be at least p1[indices[i]] + p1[indices[i-1]] away from previous
    
    min_positions = [0] * j
    min_positions[0] = p1[indices[0]]
    
    feasible_1 = True
    for i in range(1, j):
        prev_idx = indices[i-1]
        curr_idx = indices[i]
        min_pos = min_positions[i-1] + p1[prev_idx] + p1[curr_idx]
        min_positions[i] = max(min_pos, p1[curr_idx])
        
        # Check if this position exceeds the upper bound
        if min_positions[i] > 2*T - p1[curr_idx]:
            feasible_1 = False
            break
    
    if not feasible_1:
        print("LOAD 1")
        return
        
    # Now check LOAD 2 similarly but with v variables
    # v_i >= p2[i], |v_i - v_k| >= p2[i] + p2[k], v_i <= 2*T - p2[i]
    
    # Sort indices by p2 values
    indices.sort(key=lambda x: p2[x])
    
    min_positions = [0] * j
    min_positions[0] = p2[indices[0]]
    
    feasible_2 = True
    for i in range(1, j):
        prev_idx = indices[i-1]
        curr_idx = indices[i]
        min_pos = min_positions[i-1] + p2[prev_idx] + p2[curr_idx]
        min_positions[i] = max(min_pos, p2[curr_idx])
        
        # Check if this position exceeds the upper bound
        if min_positions[i] > 2*T - p2[curr_idx]:
            feasible_2 = False
            break
            
    if not feasible_2:
        print("LOAD 2")
        return
        
    # If we reach here, there might be an error in our logic since problem guarantees unsatisfiability
    # Let's recheck with a more precise method for LOAD
    
    # For LOAD 1: we want to see if we can fit j points in their respective ranges with separations
    # The minimum total span needed is sum of all p1[i] + sum of all (p1[i] + p1[k]) for consecutive placements
    
    # Simpler check: if we order by p1, and try tightest packing...
    def is_load_impossible(p_vals):
        # Sort by p values
        sorted_indices = sorted(range(len(p_vals)), key=lambda x: p_vals[x])
        pos = [0] * len(p_vals)
        
        # Place first point at its minimum position
        pos[sorted_indices[0]] = p_vals[sorted_indices[0]]
        
        for i in range(1, len(p_vals)):
            idx_curr = sorted_indices[i]
            idx_prev = sorted_indices[i-1]
            
            # Minimum position based on separation from previous point
            min_sep_pos = pos[idx_prev] + p_vals[idx_prev] + p_vals[idx_curr]
            # Minimum position based on its own constraint
            min_own_pos = p_vals[idx_curr]
            
            pos[idx_curr] = max(min_sep_pos, min_own_pos)
            
            # Check against upper bound
            if pos[idx_curr] > 2*T - p_vals[idx_curr]:
                return True
                
        return False
    
    if is_load_impossible(p1):
        print("LOAD 1")
        return
        
    if is_load_impossible(p2):
        print("LOAD 2")
        return

# Run the main function
if __name__ == '__main__':
    threading.Thread(target=main).start()