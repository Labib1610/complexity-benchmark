import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)          # 0 = unvisited, 1 or 2 = final answer
    parity = [0] * (n + 1)         # temporary 0/1 within component
    for start in range(1, n + 1):
        if color[start]:
            continue
        # BFS this component
        q = deque([start])
        parity[start] = 0
        comp = [start]
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if parity[v] == 0 and color[v] == 0 and v not in comp:
                    # not visited in this component yet
                    parity[v] = parity[u] ^ 1
                    q.append(v)
                    comp.append(v)
                elif parity[v] == 0 and color[v] == 0:
                    # first time reaching v, set parity
                    parity[v] = parity[u] ^ 1
                    q.append(v)
                    comp.append(v)
                else:
                    # already assigned parity (or final color), check consistency
                    if parity[v] != parity[u] ^ 1:
                        ok = False
                        break
            if not ok:
                break
        if not ok:
            print("NO")
            return
        # Determine mapping to final colors to make smallest lexicographic
        # start is the smallest index in this component (by iteration order)
        if parity[start] == 0:
            map0, map1 = 1, 2
        else:
            map0, map1 = 2, 1
        for v in comp:
            color[v] = map0 if parity[v] == 0 else map1

    # All components processed successfully
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()