import sys
import threading

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    p = []
    idx = 2
    for i in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        p.append((p1, p2))
        idx += 2
    
    # Check for Local Contradiction (JOB)
    for i in range(j):
        p1, p2 = p[i]
        if p1 + p2 > T:
            print(f"JOB {i+1}")
            return
    
    # Check for Global Contradiction (LOAD)
    # For c=1: check if sum of p1's > T for any pair that needs to be ordered
    # Actually, need to check if there's a cycle or impossible ordering
    
    # Let's think differently:
    # For LOAD 1: we have V_{i,1} = U_{i,1} * 2^{p_{i,1}}, U_{i,1} >= 1
    # Constraints (6): (V_{i,1} - U_{k,1})(V_{k,1} - U_{i,1}) <= 0
    # This means between any two intervals [U_{i,1}, V_{i,1}] and [U_{k,1}, V_{k,1}], one is not greater than the other.
    # In other words, the intervals [U_i, V_i] form a laminar family (nested or disjoint).
    # But since U_i >= 1 and V_i = U_i * 2^{p_i} > U_i, all intervals are proper.
    # So they must be nested: there exists an ordering such that U_1 < V_1 <= U_2 < V_2 <= ... <= U_j < V_j
    # Then V_j >= V_{j-1} * 2^{p_j} >= V_{j-2} * 2^{p_{j-1} + p_j} >= ... >= V_1 * 2^{p_2 + ... + p_j}
    # And V_1 = U_1 * 2^{p_1} >= 2^{p_1}
    # So V_j >= 2^{p_1 + p_2 + ... + p_j}
    # But also V_j <= 2^T
    # So if p_1 + ... + p_j > T, then LOAD 1 is contradictory.
    
    # Similarly for c=2.
    
    # But wait, the constraint is on V_{i,1} * V_{i,2} <= 2^T for JOB,
    # and separately V_{i,c} <= 2^T for LOAD.
    
    # Actually, re-reading example 2 note:
    # It shows that even with same p1=50, the chaining leads to 2^{200} > 2^{150}.
    # So it's about ordering and chaining bounds.
    
    # Let's implement checking for LOAD 1 and LOAD 2 based on chaining logic.
    
    # For LOAD 1:
    # Variables U_{i,1}, V_{i,1} with V_{i,1} = U_{i,1} * 2^{p_{i,1}}, U_{i,1} >= 1
    # Ordering constraints: for all i!=k, (V_{i,1} - U_{k,1})(V_{k,1} - U_{i,1}) <= 0
    # Bounding: V_{i,1} <= 2^T
    
    # These ordering constraints mean intervals [U_{i,1}, V_{i,1}] are laminar.
    # Since V_{i,1} > U_{i,1}, they are proper intervals, so must be nested.
    # WLOG order them: U_1 < V_1 <= U_2 < V_2 <= ... <= U_j < V_j
    # Then V_j >= V_{j-1} * 2^{p_j} >= ... >= V_1 * 2^{p_2 + ... + p_j} >= 2^{p_1 + p_2 + ... + p_j}
    # Need V_j <= 2^T, so if p_1 + ... + p_j > T, contradiction.
    # But we can permute indices, so sort p_{i,1} in increasing order to get worst case chaining.
    # Actually, to maximize the final V, we should sort in decreasing order of p.
    # Because V_n >= V_{n-1} * p_{n} >= V_{n-2} * p_{n-1} * p_n ...
    # To maximize, put largest p first.
    
    # So for LOAD 1: sort p_{i,1} descending, sum them, if > T, then LOAD 1
    # For LOAD 2: sort p_{i,2} descending, sum them, if > T, then LOAD 2
    
    p1_list = [p[i][0] for i in range(j)]
    p2_list = [p[i][1] for i in range(j)]
    
    p1_sorted = sorted(p1_list, reverse=True)
    p2_sorted = sorted(p2_list, reverse=True)
    
    sum_p1 = sum(p1_sorted)
    sum_p2 = sum(p2_sorted)
    
    if sum_p1 > T:
        print("LOAD 1")
        return
    elif sum_p2 > T:
        print("LOAD 2")
        return

# Run the main function
if __name__ == '__main__':
    threading.Thread(target=main).start()