import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # For each endpoint e, we have a list of allowed IPs.
    # The shard d is fixed per endpoint, so we just need to pick one IP per endpoint
    # such that all chosen IPs are distinct.
    
    adj = [[] for _ in range(k + 1)]
    shard_of = [0] * (k + 1)
    
    for _ in range(t):
        e = int(next(it))
        d = int(next(it))
        i = int(next(it))
        adj[e].append(i)
        shard_of[e] = d
    
    # Bipartite matching: left side endpoints 1..k, right side IPs 1..k
    matchL = [0] * (k + 1)  # matchL[e] = i
    matchR = [0] * (k + 1)  # matchR[i] = e
    visited = [0] * (k + 1)
    token = 0
    
    def augment(u):
        nonlocal token
        for v in adj[u]:
            if visited[v] == token:
                continue
            visited[v] = token
            if matchR[v] == 0 or augment(matchR[v]):
                matchL[u] = v
                matchR[v] = u
                return True
        return False
    
    result = 0
    for e in range(1, k + 1):
        token += 1
        if augment(e):
            result += 1
        else:
            print("NO")
            return
    
    if result != k:
        print("NO")
        return
    
    print("YES")
    out_lines = []
    for e in range(1, k + 1):
        out_lines.append(f"{e} {shard_of[e]} {matchL[e]}")
    sys.stdout.write("\n".join(out_lines) + "\n")

solve()