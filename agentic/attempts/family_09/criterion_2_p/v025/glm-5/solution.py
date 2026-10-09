import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    comp = []
    
    for i in range(1, n + 1):
        if color[i] == 0:
            queue = [i]
            color[i] = 1
            comp_a = []
            comp_b = []
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                if color[u] == 1:
                    comp_a.append(u)
                else:
                    comp_b.append(u)
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
            comp.append((comp_a, comp_b))
    
    # DP: dp[i] = max size of independent set using first i components
    # We need to track if size k is achievable
    # dp[i] = max(dp[i-1] + |A_i|, dp[i-1] + |B_i|)
    # But we need to know if exactly k is achievable
    
    num_comp = len(comp)
    # dp[i][j] = True if we can achieve size j using first i components
    # j can be at most n, but we only care up to k
    # To optimize, we track the max achievable size and use bitset or simple boolean array
    
    # Since n <= 100000, we can use a bitset approach
    # dp[j] = True if size j is achievable
    # Initialize dp[0] = True
    dp = [False] * (k + 1)
    dp[0] = True
    choice = [[-1] * (k + 1) for _ in range(num_comp + 1)]  # choice[i][j] = 0 (use A), 1 (use B), -1 (not reachable)
    
    for i in range(1, num_comp + 1):
        a, b = comp[i - 1]
        size_a = len(a)
        size_b = len(b)
        new_dp = [False] * (k + 1)
        for j in range(k + 1):
            if dp[j]:
                if j + size_a <= k:
                    new_dp[j + size_a] = True
                    choice[i][j + size_a] = 0
                if j + size_b <= k:
                    new_dp[j + size_b] = True
                    choice[i][j + size_b] = 1
        dp = new_dp
    
    if not dp[k]:
        print("NO")
        return
    
    print("YES")
    # Backtrack to find the selection
    result = []
    curr_k = k
    for i in range(num_comp, 0, -1):
        c = choice[i][curr_k]
        a, b = comp[i - 1]
        if c == 0:
            result.extend(a)
            curr_k -= len(a)
        else:
            result.extend(b)
            curr_k -= len(b)
    
    print(' '.join(map(str, result)))

solve()