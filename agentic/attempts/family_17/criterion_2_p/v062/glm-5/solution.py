import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0])
    t = int(data[1])
    
    # adj[a] = list of b-values (b = q+1 .. 2q), stored as 0-indexed right nodes
    adj = [[] for _ in range(q)]
    
    idx = 2
    for _ in range(t):
        a = int(data[idx]) - 1
        b = int(data[idx+1]) - 1 - q
        adj[a].append(b)
        idx += 2
    
    # Kuhn's algorithm for maximum matching
    matchR = [-1] * q  # matchR[b] = a matched to right node b
    visited = [False] * q
    visited_token = 0
    visited_stamp = [0] * q
    
    def try_kuhn(a):
        for b in adj[a]:
            if visited_stamp[b] != visited_token:
                visited_stamp[b] = visited_token
                if matchR[b] == -1 or try_kuhn(matchR[b]):
                    matchR[b] = a
                    return True
        return False
    
    for a in range(q):
        visited_token += 1
        if not try_kuhn(a):
            print("NO")
            return
    
    print("YES")
    out = []
    for b in range(q):
        a = matchR[b]
        out.append(f"{a+1} {b+1+q}")
    sys.stdout.write("\n".join(out))

solve()