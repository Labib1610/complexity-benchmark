import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    
    triplets = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        triplets.append((a, b, c))
    
    n = 3 * q
    
    # Group triplets by their first element
    triplets_by_first = [[] for _ in range(n + 1)]
    for trip in triplets:
        triplets_by_first[trip[0]].append(trip)
    
    # dp[i] = True if pages 1..i-1 can be covered, False otherwise
    # parent[i] = the triplet used to cover the last segment ending at i
    dp = [False] * (n + 1)
    parent = [None] * (n + 1)
    dp[0] = True
    
    for i in range(n + 1):
        if not dp[i]:
            continue
        for trip in triplets_by_first[i + 1]:
            a, b, c = trip
            if c <= n and not dp[c]:
                dp[c] = True
                parent[c] = trip
    
    if not dp[n]:
        print("NO")
        return
    
    print("YES")
    # Reconstruct the solution
    result = []
    pos = n
    while pos > 0:
        trip = parent[pos]
        result.append(trip)
        pos = trip[0] - 1
    
    for trip in reversed(result):
        print(trip[0], trip[1], trip[2])

solve()