import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    p1 = []
    p2 = []
    
    index = 2
    for _ in range(j):
        p1_val = int(data[index])
        p2_val = int(data[index+1])
        p1.append(p1_val)
        p2.append(p2_val)
        index += 2
    
    # Check for JOB i
    for i in range(j):
        # S_i >= 0
        # S_i + p1[i] <= U_i  => U_i >= S_i + p1[i]
        # U_i + p2[i] <= T   => U_i <= T - p2[i]
        # So we need: S_i + p1[i] <= T - p2[i] => S_i <= T - p1[i] - p2[i]
        # But also S_i >= 0
        # So if T - p1[i] - p2[i] < 0, then no S_i can satisfy both
        if T - p1[i] - p2[i] < 0:
            print(f"JOB {i+1}")
            return
    
    # Check for LOAD 1
    # We want to place intervals [S_i, S_i + p1[i]) disjointly in [0, T]
    # The minimum space needed is sum of p1[i]
    sum_p1 = sum(p1)
    # Since intervals are open-ended on the right, we can pack them tightly
    # The total length needed is sum_p1, but since they are open on the right,
    # we actually need sum_p1 in a space of T. 
    # Actually, let's think more carefully:
    # To place j intervals of lengths p1[0], ..., p1[j-1] disjointly starting from S_i >= 0
    # and all within [0, T), we need:
    # Total space required = sum(p1) 
    # Available space = T
    # If sum(p1) > T, it's impossible.
    if sum_p1 > T:
        print("LOAD 1")
        return
        
    # Check for LOAD 2
    # We want to place intervals [U_i, U_i + p2[i]) disjointly in [0, T]
    # Same logic applies.
    sum_p2 = sum(p2)
    if sum_p2 > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()