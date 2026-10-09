import sys
sys.setrecursionlimit(10000000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    triples = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        triples.append((a,b,c))
    
    n = 3*q
    # adjacency list: for each vertex, list of triple indices
    in_triples = [[] for _ in range(n)]
    for idx, (a,b,c) in enumerate(triples):
        in_triples[a].append(idx)
        in_triples[b].append(idx)
        in_triples[c].append(idx)
    
    used = [False]*n
    chosen = []
    
    # MRV: pick unused vertex with fewest candidate triples
    def pick_vertex():
        best = -1
        best_count = 10**9
        for v in range(n):
            if not used[v]:
                cnt = 0
                for tidx in in_triples[v]:
                    a,b,c = triples[tidx]
                    if not used[a] and not used[b] and not used[c]:
                        cnt += 1
                if cnt < best_count:
                    best_count = cnt
                    best = v
                    if cnt == 0:
                        break
        return best
    
    def dfs(depth):
        if depth == q:
            return True
        v = pick_vertex()
        if v == -1:
            return False
        # try triples containing v
        for tidx in in_triples[v]:
            a,b,c = triples[tidx]
            if used[a] or used[b] or used[c]:
                continue
            # place
            used[a] = used[b] = used[c] = True
            chosen.append((a+1,b+1,c+1))
            if dfs(depth+1):
                return True
            chosen.pop()
            used[a] = used[b] = used[c] = False
        return False
    
    if dfs(0):
        print("YES")
        for a,b,c in chosen:
            print(a,b,c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()