import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    
    groupings = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        groupings.append((a, b, c))
    
    n = 3 * q
    used = [False] * (n + 1)
    
    # Group by first element for faster lookup
    by_first = [[] for _ in range(n + 1)]
    for g in groupings:
        by_first[g[0]].append(g)
    
    result = []
    
    def backtrack():
        # Find smallest unused crate
        start = 1
        while start <= n and used[start]:
            start += 1
        if start > n:
            return True  # all used
        
        for g in by_first[start]:
            a, b, c = g
            if not used[a] and not used[b] and not used[c]:
                used[a] = used[b] = used[c] = True
                result.append(g)
                if backtrack():
                    return True
                result.pop()
                used[a] = used[b] = used[c] = False
        return False
    
    if backtrack():
        print("YES")
        for a, b, c in result:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()