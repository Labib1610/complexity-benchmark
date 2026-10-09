import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    p1_list = []
    p2_list = []
    
    index = 2
    for _ in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        p1_list.append(p1)
        p2_list.append(p2)
        index += 2
    
    # Check for job-specific contradiction
    for i in range(j):
        p1 = p1_list[i]
        p2 = p2_list[i]
        # For job i, we need p1 + p2 consecutive integers <= T
        # But actually, we need p1 integers < some value and p2 integers > some value
        # So we need at least p1 + p2 integers in total, but they must fit in {1,...,T}
        # The minimum number of integers needed for job i is p1 + p2
        # If p1 + p2 > T, then impossible
        if p1 + p2 > T:
            print(f"JOB {i+1}")
            return
    
    # Check for collection-specific contradiction
    sum_p1 = sum(p1_list)
    sum_p2 = sum(p2_list)
    
    # For collection 1: sum of all p1 must be <= T
    if sum_p1 > T:
        print("LOAD 1")
        return
        
    # For collection 2: sum of all p2 must be <= T
    if sum_p2 > T:
        print("LOAD 2")
        return
    
    # If we reach here, there should be a contradiction, but let's double-check
    # Actually, the problem guarantees there is a contradiction, so one of the above should have triggered
    # But just in case, we'll default to checking if sum_p1 > T or sum_p2 > T again
    
    # Re-checking logic more carefully:
    # Job-specific: For job k, we need p1_k elements in S1,k and p2_k elements in S2,k
    # With Rule 3, all elements of S1,k < all elements of S2,k
    # This means we need at least p1_k + p2_k positions in {1,...,T}
    # So if p1_k + p2_k > T, then JOB k is impossible
    
    # Collection-specific: 
    # For collection 1, all S1,k must be disjoint and fit in {1,...,T}
    # So sum of all p1_k must be <= T
    # Same for collection 2 with p2_k
    
    # Let's re-run the checks properly
    
    # First check job-specific
    for i in range(j):
        if p1_list[i] + p2_list[i] > T:
            print(f"JOB {i+1}")
            return
            
    # Then check collection-specific
    if sum_p1 > T:
        print("LOAD 1")
        return
    if sum_p2 > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()