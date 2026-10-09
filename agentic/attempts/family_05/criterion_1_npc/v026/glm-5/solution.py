import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    idx = 2
    triples = []
    for _ in range(t):
        x = int(data[idx]) - 1
        y = int(data[idx+1]) - 1
        z = int(data[idx+2]) - 1
        idx += 3
        triples.append((x, y, z))
    
    # For each x, list of (y, z)
    by_x = [[] for _ in range(k)]
    for x, y, z in triples:
        by_x[x].append((y, z))
    
    # If any x has no triples, impossible
    for x in range(k):
        if not by_x[x]:
            print("NO")
            return
    
    # DP over x from k-1 down to 0
    # State: bitmask of used y (k bits) and used z (k bits)
    # Since k <= 22, total states up to 2^44 which is too large.
    # But we can use meet-in-the-middle: split x into two halves.
    
    half = k // 2
    first_half = half  # x in [0, half)
    second_half_start = half
    second_half_end = k
    
    # Process first half: x in [0, half)
    # dp maps (ymask, zmask) -> list of (y, z) choices for x=0..half-1
    # We store as dict: (ymask, zmask) -> tuple of (y,z) for each x in first half
    # To save memory, store as dict of (ymask, zmask) -> choices tuple
    
    dp_first = {}
    dp_first[(0, 0)] = ()
    
    for x in range(first_half):
        new_dp = {}
        for (ymask, zmask), choices in dp_first.items():
            for (y, z) in by_x[x]:
                if (ymask >> y) & 1:
                    continue
                if (zmask >> z) & 1:
                    continue
                ny = ymask | (1 << y)
                nz = zmask | (1 << z)
                key = (ny, nz)
                if key not in new_dp:
                    new_dp[key] = choices + ((y, z),)
        dp_first = new_dp
        if not dp_first:
            print("NO")
            return
    
    # Process second half: x in [half, k)
    # dp maps (ymask, zmask) -> list of (y, z) choices for x=half..k-1
    dp_second = {}
    dp_second[(0, 0)] = ()
    
    for x in range(second_half_start, second_half_end):
        new_dp = {}
        for (ymask, zmask), choices in dp_second.items():
            for (y, z) in by_x[x]:
                if (ymask >> y) & 1:
                    continue
                if (zmask >> z) & 1:
                    continue
                ny = ymask | (1 << y)
                nz = zmask | (1 << z)
                key = (ny, nz)
                if key not in new_dp:
                    new_dp[key] = choices + ((y, z),)
        dp_second = new_dp
        if not dp_second:
            print("NO")
            return
    
    # Now find matching: first half uses (ymask1, zmask1), second half uses (ymask2, zmask2)
    # such that ymask1 | ymask2 == full_y and zmask1 | zmask2 == full_z
    # and ymask1 & ymask2 == 0 and zmask1 & zmask2 == 0
    full_mask = (1 << k) - 1
    
    # Build dict for second half: key (ymask, zmask) -> choices
    # For each first half state, compute complement and look up
    found = False
    result_first = None
    result_second = None
    
    for (ymask1, zmask1), choices1 in dp_first.items():
        ymask2_needed = full_mask ^ ymask1
        zmask2_needed = full_mask ^ zmask1
        key2 = (ymask2_needed, zmask2_needed)
        if key2 in dp_second:
            found = True
            result_first = choices1
            result_second = dp_second[key2]
            break
    
    if not found:
        print("NO")
        return
    
    print("YES")
    # Output in order: x=0..half-1 with result_first, then x=half..k-1 with result_second
    for i, (y, z) in enumerate(result_first):
        print(f"{i+1} {y+1} {z+1}")
    for i, (y, z) in enumerate(result_second):
        x = second_half_start + i
        print(f"{x+1} {y+1} {z+1}")

solve()