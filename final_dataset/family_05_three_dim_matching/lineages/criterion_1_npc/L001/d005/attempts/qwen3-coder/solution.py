from itertools import combinations

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    resonators = []
    idx = 2
    for _ in range(t):
        f = int(data[idx])
        p = int(data[idx+1])
        a = int(data[idx+2])
        resonators.append((f, p, a))
        idx += 3
    
    # We need to find a subset of exactly k resonators such that
    # the union of all frequency, phase, and amplitude values has size 3*k
    # Since each value is between 1 and k, the max size for each set is k
    # So we need each of U_f, U_p, U_a to have size k, meaning we need to see
    # all values 1..k in each parameter
    
    # Try all combinations of k resonators from the t available
    from itertools import combinations
    
    target_freq = set(range(1, k+1))
    
    for combo in combinations(resonators, k):
        freqs = set()
        phases = set()
        amps = set()
        
        for f, p, a in combo:
            freqs.add(f)
            phases.add(p)
            amps.add(a)
        
        if len(freqs) == k and len(phases) == k and len(amps) == k:
            print("YES")
            for res in combo:
                print(res[0], res[1], res[2])
            return
    
    print("NO")

solve()