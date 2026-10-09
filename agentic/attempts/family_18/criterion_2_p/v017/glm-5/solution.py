import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        print("NO")
        return
    
    it = iter(data)
    try:
        n = int(next(it))
        m = int(next(it))
        B = int(next(it))
    except StopIteration:
        print("NO")
        return
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    # Find root (node with degree != 1, except for n=1 case)
    root = 1
    deg = [len(adj[i]) for i in range(n + 1)]
    for i in range(1, n + 1):
        if deg[i] != 1:
            root = i
            break
    
    if n == 1:
        print("YES")
        print(1)
        return
    
    # BFS to build tree structure and parent pointers
    parent = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]
    order = []
    q = [root]
    parent[root] = root
    order.append(root)
    
    idx = 0
    while idx < len(q):
        u = q[idx]
        idx += 1
        for v in adj[u]:
            if parent[v] == 0:
                parent[v] = u
                children[u].append(v)
                q.append(v)
                order.append(v)
    
    # DP on tree
    # dp[u] = set of sizes of subtrees in the "lower" group (closer to leaves)
    inf = n + 1
    dp = [set() for _ in range(n + 1)]
    
    # Process in reverse order (leaves to root)
    for u in reversed(order):
        dp[u].add(0)
        for v in children[u]:
            new_set = set()
            for s1 in dp[u]:
                for s2 in dp[v]:
                    new_set.add(s1 + s2 + 1)
            dp[u] = new_set
    
    # Find valid split at root
    found = -1
    for s in dp[root]:
        cost = s * (n - s)
        if cost <= B:
            found = s
            break
    
    if found == -1:
        print("NO")
        return
    
    # Assign positions
    pos = [0] * (n + 1)
    group = [0] * (n + 1)  # 0 = upper (small pos), 1 = lower (large pos)
    
    # BFS from root to assign groups
    # Root itself should be in upper group (group 0)
    group[root] = 0
    
    # We need to select exactly 'found' nodes for lower group
    # Greedy: process children, for each child decide group
    # If parent is 0, child can be 0 or 1. If parent is 1, child must be 1.
    
    remaining = found
    q_assign = [root]
    idx = 0
    while idx < len(q_assign):
        u = q_assign[idx]
        idx += 1
        
        if group[u] == 0:
            # This node is upper group
            # Its children can potentially be lower group
            # We need to decide which subtrees go to lower group
            for v in children[u]:
                child_contribution = -1
                best_k = -1
                # Check if we can take this child's subtree for lower group
                for k in dp[v]:
                    needed = k + 1
                    if needed <= remaining:
                        if child_contribution == -1 or k > child_contribution:
                            child_contribution = k
                            best_k = k
                
                if child_contribution != -1:
                    group[v] = 1
                    remaining -= best_k + 1
                else:
                    group[v] = 0
                q_assign.append(v)
        else:
            # Parent is lower group, all children must be lower group
            for v in children[u]:
                group[v] = 1
                q_append.append(v)
    
    # Collect nodes by group
    upper = []
    lower = []
    for u in range(1, n + 1):
        if group[u] == 0:
            upper.append(u)
        else:
            lower.append(u)
    
    # Assign positions
    # Upper group gets positions 1, 2, ... len(upper)
    # Lower group gets positions n, n-1, ... n - len(lower) + 1
    for i, u in enumerate(upper):
        pos[u] = i + 1
    
    for i, u in enumerate(lower):
        pos[u] = n - i
    
    print("YES")
    print(' '.join(map(str, pos[1:])))

if __name__ == "__main__":
    solve()