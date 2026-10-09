import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    q = int(input_data[0])
    t = int(input_data[1])
    triples = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        triples.append((a, b, c))
    
    n = 3 * q
    # adjacency list: for each crystal, list of triples containing it
    adj = [[] for _ in range(n + 1)]
    for i, (a, b, c) in enumerate(triples):
        adj[a].append(i)
        adj[b].append(i)
        adj[c].append(i)
    
    used = [False] * (n + 1)
    chosen = []
    
    # Precompute for each triple the set of its vertices
    triple_set = [set(tri) for tri in triples]
    
    # Backtracking
    def backtrack(start):
        if len(chosen) == q:
            return True
        # find first unused crystal
        v = start
        while v <= n and used[v]:
            v += 1
        if v > n:
            return False
        # try all triples containing v
        for ti in adj[v]:
            a, b, c = triples[ti]
            if used[a] or used[b] or used[c]:
                continue
            # choose this triple
            used[a] = used[b] = used[c] = True
            chosen.append((a, b, c))
            if backtrack(v + 1):
                return True
            # backtrack
            chosen.pop()
            used[a] = used[b] = used[c] = False
        return False
    
    if backtrack(1):
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()