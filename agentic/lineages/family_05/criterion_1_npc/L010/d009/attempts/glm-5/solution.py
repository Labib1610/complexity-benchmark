import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    relays = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        relays.append((a, b, c))
    
    # We need to select k relays such that:
    # - Primary channels form a permutation of 1..k
    # - Secondary channels form a permutation of 1..k
    # - Tertiary channels form a permutation of 1..k
    
    # Group relays by their primary channel
    by_primary = [[] for _ in range(k + 1)]
    for idx, (a, b, c) in enumerate(relays):
        by_primary[a].append((b, c, idx))
    
    # Check if we have at least one relay for each primary channel 1..k
    for i in range(1, k + 1):
        if not by_primary[i]:
            print("NO")
            return
    
    # Now we need to select exactly one relay from each primary group
    # such that secondary channels form a permutation and tertiary channels form a permutation
    
    # This is equivalent to finding a perfect matching in a bipartite graph
    # Left side: primary channels 1..k
    # Right side: secondary channels 1..k
    # Edge exists if there's a relay with that primary and secondary
    # But we also need tertiary to be a permutation
    
    # We can model this as finding a permutation pi (secondary assignment) and sigma (tertiary assignment)
    # such that for each primary i, there exists a relay (i, pi[i], sigma[i])
    
    # Since k <= 22, we can use meet-in-the-middle or DP with bitmask
    
    # Split primary channels into two halves
    half = k // 2
    left_size = half
    right_size = k - half
    
    left_primaries = list(range(1, left_size + 1))
    right_primaries = list(range(left_size + 1, k + 1))
    
    # For left half: enumerate all valid (secondary_mask, tertiary_mask) pairs
    # and store the relay choices
    
    left_results = {}  # (sec_mask, ter_mask) -> list of relay indices
    
    def enumerate_left(pos, sec_mask, ter_mask, choices):
        if pos == left_size:
            key = (sec_mask, ter_mask)
            if key not in left_results:
                left_results[key] = choices[:]
            return True
        
        pri = left_primaries[pos]
        for b, c, idx in by_primary[pri]:
            if (sec_mask >> (b - 1)) & 1:
                continue
            if (ter_mask >> (c - 1)) & 1:
                continue
            choices.append(idx)
            enumerate_left(pos + 1, sec_mask | (1 << (b - 1)), ter_mask | (1 << (c - 1)), choices)
            choices.pop()
    
    enumerate_left(0, 0, 0, [])
    
    if not left_results:
        print("NO")
        return
    
    # For right half: enumerate and check against left_results
    right_primaries_list = right_primaries
    
    def enumerate_right(pos, sec_mask, ter_mask, choices):
        if pos == right_size:
            # Check if there's a matching left half
            needed_sec_mask = ((1 << k) - 1) ^ sec_mask
            needed_ter_mask = ((1 << k) - 1) ^ ter_mask
            key = (needed_sec_mask, needed_ter_mask)
            if key in left_results:
                # Found a solution
                left_choices = left_results[key]
                all_choices = left_choices + choices[:]
                print("YES")
                for idx in all_choices:
                    a, b, c = relays[idx]
                    print(a, b, c)
                return True
            return False
        
        pri = right_primaries_list[pos]
        for b, c, idx in by_primary[pri]:
            if (sec_mask >> (b - 1)) & 1:
                continue
            if (ter_mask >> (c - 1)) & 1:
                continue
            choices.append(idx)
            if enumerate_right(pos + 1, sec_mask | (1 << (b - 1)), ter_mask | (1 << (c - 1)), choices):
                return True
            choices.pop()
        return False
    
    if not enumerate_right(0, 0, 0, []):
        print("NO")

solve()