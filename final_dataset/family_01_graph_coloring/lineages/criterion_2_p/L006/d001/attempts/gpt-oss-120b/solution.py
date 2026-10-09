import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
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

    color = [-1] * n          # 0/1 bipartite color
    comp = [-1] * n           # component id
    comp_cnt = 0
    from collections import deque

    for i in range(n):
        if color[i] != -1:
            continue
        # BFS this component
        q = deque([i])
        color[i] = 0
        comp[i] = comp_cnt
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    comp[v] = comp_cnt
                    q.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
        comp_cnt += 1

    # orientation for each component: flip = 0 means color 0 -> state 1
    # flip = 1 means color 0 -> state 2
    flip = [0] * comp_cnt
    decided = [False] * comp_cnt

    res = [0] * n
    for i in range(n):
        cid = comp[i]
        if not decided[cid]:
            # we want state 1 at position i
            # if current color[i] == 0, set flip=0; else flip=1
            flip[cid] = color[i]  # because state 1 corresponds to (color xor flip)==0
            decided[cid] = True
        state = 1 if (color[i] ^ flip[cid]) == 0 else 2
        res[i] = state

    print("YES")
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    solve()