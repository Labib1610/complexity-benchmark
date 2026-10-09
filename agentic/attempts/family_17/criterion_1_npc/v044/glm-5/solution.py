import sys
input = sys.stdin.readline

def solve():
    q, t = map(int, input().split())
    protocols = []
    # Map from (a, b) -> c
    ab_to_c = {}
    
    for _ in range(t):
        a, b, c = map(int, input().split())
        protocols.append((a, b, c))
        ab_to_c[(a, b)] = c
    
    # dp[i] stores the list of protocols used to cover IDs 1..3*i
    # None means not reachable, empty list means i=0
    dp = [None] * (q + 1)
    dp[0] = []
    
    for i in range(q):
        if dp[i] is None:
            continue
        
        # We need to cover the next 3 IDs: 3*i + 1, 3*i + 2, 3*i + 3
        base = 3 * i
        a1 = base + 1
        b1 = base + 2
        c1 = base + 3
        
        # Option 1: Use one protocol (a1, b1, c1)
        if (a1, b1) in ab_to_c:
            if ab_to_c[(a1, b1)] == c1:
                dp[i+1] = dp[i] + [(a1, b1, c1)]
        
        # Option 2: Use two protocols
        # We need to pair a1 with some x > b1, and b1 with some y > c1
        # The IDs to cover are a1, b1, c1, c1+1, c1+2, c1+3
        # Let the two protocols be (a1, x, c2) and (b1, y, c3)
        # The set of IDs must be {a1, b1, c1, c1+1, c1+2, c1+3}
        # So {x, c2, y, c3} = {b1, c1, c1+1, c1+2, c1+3}
        # Since x > b1 and y > c1, the only valid assignment is:
        # x = c1+1, c2 = c1+3, y = c1+2, c3 = c1+3 (Wait, c2 and c3 must be distinct)
        # Let's re-derive:
        # IDs available for x, c2, y, c3: b1, c1, c1+1, c1+2, c1+3
        # Constraints: a1 < x < c2, b1 < y < c3
        # x must be > a1 = b1-1. Since x is from the set, x can be b1, c1, c1+1, c1+2, c1+3.
        # But x > b1, so x >= c1.
        # y must be > b1. y is from the set. y can be c1, c1+1, c1+2, c1+3.
        # But y > c1 (since y > b1 and c1 > b1, and y must be distinct from x).
        # Actually, let's look at the structure.
        # The 6 IDs are a1, b1, c1, c1+1, c1+2, c1+3.
        # a1 is the smallest. It must be paired with two larger IDs.
        # b1 is the second smallest. It must be paired with two larger IDs.
        # The largest ID is c1+3. It must be paired with two smaller IDs.
        # The second largest is c1+2. It must be paired with two smaller IDs.
        # 
        # Protocol 1: (a1, ?, ?)
        # Protocol 2: (b1, ?, ?)
        # 
        # The largest ID c1+3 must be in one of them.
        # Case A: c1+3 is in Protocol 1. Then Protocol 1 is (a1, x, c1+3).
        # Then Protocol 2 must cover the remaining: b1, c1, c1+1, c1+2.
        # Protocol 2 is (b1, y, z). IDs {y, z} = {c1, c1+1, c1+2}.
        # Since y < z, and y > b1, y can be c1 or c1+1.
        # If y = c1, z = c1+2. Protocol 2: (b1, c1, c1+2).
        # Then x must be the remaining ID c1+1.
        # Protocol 1: (a1, c1+1, c1+3).
        # Check constraints: a1 < c1+1 < c1+3. Correct.
        # 
        # Case B: c1+3 is in Protocol 2. Then Protocol 2 is (b1, y, c1+3).
        # Remaining IDs for Protocol 1: c1, c1+1, c1+2.
        # Protocol 1 is (a1, x, z). IDs {x, z} = {c1, c1+1, c1+2}.
        # Since x < z, x can be c1 or c1+1.
        # If x = c1, z = c1+2. Protocol 1: (a1, c1, c1+2).
        # Then y must be the remaining ID c1+1.
        # Protocol 2: (b1, c1+1, c1+3).
        # Check constraints: b1 < c1+1 < c1+3. Correct.
        # 
        # So the two possible configurations are:
        # 1. (a1, c1+1, c1+3) and (b1, c1, c1+2)
        # 2. (a1, c1, c1+2) and (b1, c1+1, c1+3)
        
        if i + 2 <= q:
            # Configuration 1
            p1 = (a1, c1 + 1, c1 + 3)
            p2 = (b1, c1, c1 + 2)
            if p1[:2] in ab_to_c and p2[:2] in ab_to_c:
                if ab_to_c[p1[:2]] == p1[2] and ab_to_c[p2[:2]] == p2[2]:
                    dp[i+2] = dp[i] + [p1, p2]
            
            if dp[i+2] is None:
                # Configuration 2
                p1 = (a1, c1, c1 + 2)
                p2 = (b1, c1 + 1, c1 + 3)
                if p1[:2] in ab_to_c and p2[:2] in ab_to_c:
                    if ab_to_c[p1[:2]] == p1[2] and ab_to_c[p2[:2]] == p2[2]:
                        dp[i+2] = dp[i] + [p1, p2]

    if dp[q] is not None:
        print("YES")
        for p in dp[q]:
            print(p[0], p[1], p[2])
    else:
        print("NO")

if __name__ == '__main__':
    solve()