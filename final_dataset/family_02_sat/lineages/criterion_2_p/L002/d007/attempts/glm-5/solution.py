import sys
sys.setrecursionlimit(300000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        c1 = int(next(it))
        c2 = int(next(it))
        u = abs(c1)
        v = abs(c2)
        adj[u].append((v, c1, c2))
        adj[v].append((u, c1, c2))
    
    state = [-1] * (n + 1)
    possible = True
    
    for i in range(1, n + 1):
        if state[i] == -1:
            stack = [(i, 0)]
            while stack and possible:
                u, s = stack.pop()
                if state[u] != -1:
                    if state[u] != s:
                        possible = False
                    continue
                state[u] = s
                for v, c1, c2 in adj[u]:
                    tau_u = c1 * (2 * s - 1)
                    if tau_u < 0:
                        # Need tau_v >= 0 to avoid fracture
                        # tau_v = c2 * (2 * s_v - 1) >= 0
                        if c2 > 0:
                            s_v = 1
                        else:
                            s_v = 0
                        if state[v] == -1:
                            stack.append((v, s_v))
                        elif state[v] != s_v:
                            possible = False
                            break
                    # If tau_u >= 0, no constraint on v from this edge
                if not possible:
                    break
        if not possible:
            break
    
    if not possible:
        print("NO")
    else:
        print("YES")
        result = []
        for i in range(1, n + 1):
            if state[i] == -1:
                state[i] = 0
            result.append(str(state[i]))
        print(' '.join(result))

solve()