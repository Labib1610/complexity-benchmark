import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = data[idx]
        v = data[idx + 1]
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)  # 0 or 1
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        comp = []
        dq = deque([start])
        color[start] = 0
        comp.append(start)
        conflict = False
        while dq:
            u = dq.popleft()
            cu = color[u]
            for v in adj[u]:
                cv = color[v]
                if cv == -1:
                    color[v] = cu ^ 1
                    dq.append(v)
                    comp.append(v)
                elif cv == cu:
                    conflict = True
                    break
            if conflict:
                break
        if conflict:
            sys.stdout.write("NO")
            return
        # ensure minimal lexicographic: smallest index gets color 0
        min_idx = min(comp)
        if color[min_idx] == 1:
            for v in comp:
                color[v] ^= 1

    result = [str(color[i] + 1) for i in range(1, n + 1)]
    sys.stdout.write("YES\n" + " ".join(result))

if __name__ == "__main__":
    solve()