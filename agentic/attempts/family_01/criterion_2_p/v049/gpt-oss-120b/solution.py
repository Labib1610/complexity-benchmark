import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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

    final = [0] * (n + 1)          # 0 = unassigned, 1 or 2 = answer
    temp = [-1] * (n + 1)         # temporary 0/1 during BFS

    for start in range(1, n + 1):
        if final[start]:
            continue
        # BFS of this component
        q = deque([start])
        temp[start] = 0
        comp = [start]
        bip = True
        while q and bip:
            u = q.popleft()
            for v in adj[u]:
                if temp[v] == -1:
                    temp[v] = 1 - temp[u]
                    q.append(v)
                    comp.append(v)
                elif temp[v] == temp[u]:
                    bip = False
                    break
        if not bip:
            print("NO")
            return
        # decide final colours: give 1 to the side containing 'start'
        side_start = temp[start]
        for v in comp:
            if temp[v] == side_start:
                final[v] = 1
            else:
                final[v] = 2
        # reset temp for next component
        for v in comp:
            temp[v] = -1

    print("YES")
    out = ' '.join(str(final[i]) for i in range(1, n + 1))
    sys.stdout.write(out)

if __name__ == "__main__":
    solve()