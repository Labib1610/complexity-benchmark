def solve():
    import sys
    data = sys.stdin.read().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(data[idx]) - 1  # 0-indexed
        idx += 1
        v = int(data[idx]) - 1
        idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    assignment = [-1] * n
    
    def is_valid(shard, drive):
        for neighbor in adj[shard]:
            if assignment[neighbor] == drive:
                return False
        return True
    
    def backtrack(shard_idx):
        if shard_idx == n:
            return True
        
        for drive in range(1, 4):  # drives 1, 2, 3
            if is_valid(shard_idx, drive):
                assignment[shard_idx] = drive
                if backtrack(shard_idx + 1):
                    return True
                assignment[shard_idx] = -1
        
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

solve()