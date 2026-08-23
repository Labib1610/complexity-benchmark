import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    # remove duplicate edges
    adj = [list(set(nei)) for nei in adj]

    # Fast path: if the graph is bipartite, the lexicographically smallest
    # valid assignment is just its lexicographically smallest 2-coloring.
    color = [0] * n
    is_bip = True
    for v in range(n):
        if color[v] == 0:
            color[v] = 1
            dq = deque([v])
            while dq and is_bip:
                x = dq.popleft()
                for u in adj[x]:
                    if color[u] == 0:
                        color[u] = 3 - color[x]
                        dq.append(u)
                    elif color[u] == color[x]:
                        is_bip = False
                        break
            if not is_bip:
                break
    if is_bip:
        sys.stdout.write('YES\n' + ' '.join(map(str, color)) + '\n')
        return

    # General case: backtracking search with unit propagation.
    FULL = 7  # bits for colors 1,2,3
    assign = [0] * n
    dom = [FULL] * n
    sys.setrecursionlimit(10000)

    def propagate(v):
        cbit = dom[v]
        stack = [v]
        while stack:
            x = stack.pop()
            cx = dom[x]
            for u in adj[x]:
                if dom[u] & cx:
                    dom[u] &= ~cx
                    if dom[u] == 0:
                        return False
                    if dom[u] & (dom[u] - 1) == 0:
                        stack.append(u)
        return True

    def dfs(i):
        while i < n and assign[i]:
            i += 1
        if i == n:
            return True
        mask = dom[i]
        for c in (1, 2, 3):
            cbit = 1 << (c - 1)
            if not (mask & cbit):
                continue
            old_assign = assign[:]
            old_dom = dom[:]
            assign[i] = c
            dom[i] = cbit
            if propagate(i) and dfs(i + 1):
                return True
            assign[:] = old_assign
            dom[:] = old_dom
        return False

    if dfs(0):
        sys.stdout.write('YES\n' + ' '.join(map(str, assign)) + '\n')
    else:
        sys.stdout.write('NO\n')

if __name__ == '__main__':
    solve()