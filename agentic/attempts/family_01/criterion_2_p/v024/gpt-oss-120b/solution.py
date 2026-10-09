import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    g = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        g[u].append(v)
        g[v].append(u)

    color = [-1] * n          # 0/1 parity inside component
    answer = [0] * n          # final 1/2 assignment
    stack = []
    for start in range(n):
        if color[start] != -1:
            continue
        # new component
        comp_vertices = []
        color[start] = 0
        stack.append(start)
        ok = True
        while stack:
            v = stack.pop()
            comp_vertices.append(v)
            cv = color[v]
            for to in g[v]:
                if color[to] == -1:
                    color[to] = cv ^ 1
                    stack.append(to)
                elif color[to] == cv:
                    print("NO")
                    return
        # decide orientation: make smallest index vertex have final value 1
        min_v = min(comp_vertices)
        # if min_v currently has parity 0, we map 0->1,1->2; else flip
        flip = (color[min_v] == 1)
        for v in comp_vertices:
            parity = color[v]
            if flip:
                parity ^= 1
            answer[v] = parity + 1   # 0->1,1->2

    print("YES")
    print(' '.join(map(str, answer)))

if __name__ == "__main__":
    solve()