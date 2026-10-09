import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    j = int(input_data[0])
    T = int(input_data[1])
    
    p1 = []
    p2 = []
    idx = 2
    for _ in range(j):
        p1.append(int(input_data[idx]))
        p2.append(int(input_data[idx+1]))
        idx += 2
        
    # Check for JOB i
    for i in range(j):
        min_c1 = p1[i] / 2.0
        max_c1 = T - p1[i] / 2.0
        
        min_c2 = p2[i] / 2.0
        max_c2 = T - p2[i] / 2.0
        
        # Constraint 3: c2_i - c1_i >= (p1_i + p2_i) / 2
        # c2_i >= c1_i + (p1_i + p2_i) / 2
        # To minimize c2_i, we set c1_i to its minimum value min_c1
        min_c2_from_c1 = min_c1 + (p1[i] + p2[i]) / 2.0
        
        if min_c2_from_c1 > max_c2:
            print(f"JOB {i+1}")
            return
            
    # Check for LOAD 1
    # Sort primary slider lengths in descending order
    p1_sorted = sorted(p1, reverse=True)
    
    # The minimum span required for the centers is the sum of half-lengths
    # of adjacent intervals in the optimal packing.
    min_span = 0.0
    for k in range(j - 1):
        min_span += (p1_sorted[k] + p1_sorted[k+1]) / 2.0
        
    max_span = T - p1_sorted[-1] / 2.0 - p1_sorted[-2] / 2.0
    
    if min_span > max_span:
        print("LOAD 1")
        return
        
    # Check for LOAD 2
    # Sort secondary slider lengths in descending order
    p2_sorted = sorted(p2, reverse=True)
    
    min_span = 0.0
    for k in range(j - 1):
        min_span += (p2_sorted[k] + p2_sorted[k+1]) / 2.0
        
    max_span = T - p2_sorted[-1] / 2.0 - p2_sorted[-2] / 2.0
    
    if min_span > max_span:
        print("LOAD 2")
        return

if __name__ == '__main__':
    solve()