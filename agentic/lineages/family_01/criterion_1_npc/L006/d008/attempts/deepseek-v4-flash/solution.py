import sys

sys.setrecursionlimit(10000)

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # forbidden pairs: (2,2) and (3,3)
    # state 1 is compatible with all
    
    assignment = [0] * n  # 0 = unassigned
    
    # Precompute degree for ordering
    degree = [len(adj[i]) for i in range(n)]
    
    def is_valid(node, val):
        for nb in adj[node]:
            if assignment[nb] != 0:
                if assignment[nb] == val and val in (2,3):
                    return False
        return True
    
    # MRV: pick unassigned with fewest possible values
    def select_unassigned():
        best = -1
        best_count = 4
        for i in range(n):
            if assignment[i] == 0:
                cnt = 0
                for v in (1,2,3):
                    if is_valid(i, v):
                        cnt += 1
                if cnt < best_count:
                    best_count = cnt
                    best = i
                    if cnt == 0:
                        break
        return best
    
    def backtrack():
        node = select_unassigned()
        if node == -1:
            return True
        # try values in order 1,2,3
        for val in (1,2,3):
            if is_valid(node, val):
                assignment[node] = val
                if backtrack():
                    return True
                assignment[node] = 0
        return False
    
    if backtrack():
        print("YES")
        print(" ".join(str(x) for x in assignment))
    else:
        print("NO")

if __name__ == "__main__":
    solve()