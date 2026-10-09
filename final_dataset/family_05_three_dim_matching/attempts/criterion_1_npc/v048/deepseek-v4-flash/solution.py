import sys
sys.setrecursionlimit(1000000)

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    k = int(input_data[0])
    t = int(input_data[1])
    triples = []
    idx = 2
    by_chassis = [[] for _ in range(k)]
    for _ in range(t):
        c = int(input_data[idx]) - 1
        e = int(input_data[idx+1]) - 1
        g = int(input_data[idx+2]) - 1
        idx += 3
        triples.append((c,e,g))
        by_chassis[c].append((e,g))
    
    # Prepare bit masks per chassis: develop list of (core_mask, payload_mask)
    chassis_options = []
    for c in range(k):
        options = []
        for e,g in by_chassis[c]:
            options.append((1 << e, 1 << g))
        chassis_options.append(options)
    
    full_mask = (1 << k) - 1
    solution = []
    
    def dfs(chassis_mask, core_mask, payload_mask):
        if chassis_mask == 0:
            return core_mask == 0 and payload_mask == 0
        # pick first unused chassis
        # get lowest set bit
        c = (chassis_mask & -chassis_mask).bit_length() - 1
        rem_chassis = chassis_mask & ~(1 << c)
        for cmask, pmask in chassis_options[c]:
            if core_mask & cmask == 0 and payload_mask & pmask == 0:
                solution.append((c, cmask.bit_length()-1, pmask.bit_length()-1))
                if dfs(rem_chassis, core_mask | cmask, payload_mask | pmask):
                    return True
                solution.pop()
        return False
    
    if dfs(full_mask, 0, 0):
        print("YES")
        for c,e,g in solution:
            print(c+1, e+1, g+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()