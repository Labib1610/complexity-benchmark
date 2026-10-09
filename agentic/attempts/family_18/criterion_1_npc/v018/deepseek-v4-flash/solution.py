import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    edges = []
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u,v))
        adj[u].append(v)
        adj[v].append(u)
    
    if m == 0:
        print("YES")
        print(" ".join(str(i+1) for i in range(n)))
        return
    
    # Check if n is small enough for exact search
    if n > 14:
        # Heuristic: arrange by degree descending around center
        degree = [len(adj[i]) for i in range(n)]
        order = sorted(range(n), key=lambda x: -degree[x])
        # Place highest degree in middle
        pos = [0]*n
        left = (n-1)//2
        right = left+1
        # We'll use simple BFS from highest degree node
        from collections import deque
        placed = [False]*n
        pos_list = [0]*n
        start = order[0]
        placed[start] = True
        pos_list[start] = left
        left -= 1
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not placed[v]:
                    if left >= 0:
                        pos_list[v] = left
                        left -= 1
                    else:
                        pos_list[v] = right
                        right += 1
                    placed[v] = True
                    q.append(v)
        # place any remaining
        for i in range(n):
            if not placed[i]:
                if left >= 0:
                    pos_list[i] = left
                    left -= 1
                else:
                    pos_list[i] = right
                    right += 1
        total = sum(abs(pos_list[u]-pos_list[v]) for u,v in edges)
        if total <= B:
            print("YES")
            print(" ".join(str(p+1) for p in pos_list))
        else:
            print("NO")
        return

    # Exact search using backtracking
    best_pos = None
    found = False
    used = [False]*(n+1)
    pos = [0]*n
    # precompute edge list as pairs
    
    def lower_bound(k):
        # minimal possible additional cost given k assigned
        # For each edge, if both endpoints assigned, cost fixed.
        # If one assigned, we can put other as close as possible.
        # For unassigned both, min cost 0.
        lb = 0
        for (u,v) in edges:
            if u < k and v < k:
                lb += abs(pos[u] - pos[v])
            elif u < k:
                # place v at position 1 or n, whichever closer
                lb += min(abs(pos[u] - 1), abs(pos[u] - n))
            elif v < k:
                lb += min(abs(pos[v] - 1), abs(pos[v] - n))
        return lb
    
    def dfs(idx, cost):
        nonlocal found, best_pos
        if found:
            return
        if cost > B:
            return
        if idx == n:
            if cost <= B:
                found = True
                best_pos = pos[:]
            return
        # pruning: lower bound based on fixed + possible min for remaining
        lb = cost
        # For edges with exactly one endpoint placed, add min possible
        for (u,v) in edges:
            if u < idx and v >= idx:
                lb += min(abs(pos[u]-1), abs(pos[u]-n))
            elif v < idx and u >= idx:
                lb += min(abs(pos[v]-1), abs(pos[v]-n))
        if lb > B:
            return
        # try positions
        for p in range(1, n+1):
            if not used[p]:
                used[p] = True
                pos[idx] = p
                add = 0
                for (u,v) in edges:
                    if u == idx and v < idx:
                        add += abs(p - pos[v])
                    elif v == idx and u < idx:
                        add += abs(p - pos[u])
                dfs(idx+1, cost + add)
                used[p] = False
                if found:
                    return
    
    dfs(0, 0)
    
    if found:
        print("YES")
        print(" ".join(str(x) for x in best_pos))
    else:
        print("NO")

if __name__ == "__main__":
    solve()