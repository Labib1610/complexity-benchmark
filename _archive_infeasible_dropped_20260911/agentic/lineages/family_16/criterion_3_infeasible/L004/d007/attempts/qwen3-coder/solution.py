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
        # For a single job, we need x, y, z such that:
        # y - x = p1
        # z - y = p2
        # So z - x = p1 + p2
        # And we need 1 <= x < y < z <= T + 1
        # This means we need z - x <= T (since x >= 1 and z <= T + 1)
        # So p1 + p2 <= T
        if p1 + p2 > T:
            print(f"JOB {i + 1}")
            return
    
    # Check for collection-specific contradiction
    # For collection 1: we have j sets, each of size p1_i
    # They must be disjoint and fit in [1, T]
    # The minimum space needed is sum of p1's
    # But since they are disjoint intervals, we actually need 
    # sum(p1) positions, but the maximum number of positions is T
    # So if sum(p1) > T, then LOAD 1
    
    # Similarly for collection 2 with p2
    
    sum_p1 = sum(p1_list)
    sum_p2 = sum(p2_list)
    
    if sum_p1 > T:
        print("LOAD 1")
        return
        
    if sum_p2 > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()