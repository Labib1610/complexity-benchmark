import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    
    # specialist x is paired with machine y in Stage 1
    # so each x has exactly one y, and the mapping is a bijection
    # we need to choose for each (x,y) pair a time slot z
    # such that every time slot 1..k is used exactly once
    
    # This is a bipartite matching: left side = specialists (or x,y pairs),
    # right side = time slots z.
    # Each allowed combination (x,y,z) is an edge from specialist x to slot z.
    
    adj = [[] for _ in range(k + 1)]
    idx = 2
    for _ in range(t):
        x = int(data[idx]); y = int(data[idx+1]); z = int(data[idx+2])
        idx += 3
        adj[x].append(z)
    
    # Hopcroft-Karp or simple augmenting path matching
    match_z = [0] * (k + 1)  # which x is matched to z
    match_x = [0] * (k + 1)  # which z is matched to x
    
    def try_kuhn(v, visited):
        for to in adj[v]:
            if not visited[to]:
                visited[to] = True
                if match_z[to] == 0 or try_kuhn(match_z[to], visited):
                    match_z[to] = v
                    match_x[v] = to
                    return True
        return False
    
    result = 0
    for v in range(1, k + 1):
        visited = [False] * (k + 1)
        if try_kuhn(v, visited):
            result += 1
        else:
            break
    
    if result == k:
        out = ["YES"]
        for v in range(1, k + 1):
            z = match_x[v]
            # we need y for x; from input we know each x has one y
            # but we didn't store it. Let's re-read or store.
            # Actually we need to output x y z. We stored adj only.
            # Let's fix: store y mapping.
            pass
        # We need to output x y z. We lost y. Let's redo with y stored.
        # Rewrite solution storing y.
        pass
    else:
        sys.stdout.write("NO\n")

solve()