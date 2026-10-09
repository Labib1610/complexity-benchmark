import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    idx = 2
    adj = [[] for _ in range(2 * n)]
    for _ in range(m):
        a = int(data[idx]); b = int(data[idx+1]); idx += 2
        u = (abs(a) - 1) * 2 + (1 if a > 0 else 0)
        v = (abs(b) - 1) * 2 + (1 if b > 0 else 0)
        adj[u ^ 1].append(v)
        adj[v ^ 1].append(u)
    stack = []
    on_stack = [False] * (2 * n)
    index = [-1] * (2 * n)
    low = [0] * (2 * n)
    comp = [-1] * (2 * n)
    timer = [0]
    comp_id = [0]
    size = 2 * n
    for s in range(size):
        if index[s] == -1:
            stack.append(~s)
            stack.append(s)
            while stack:
                v = stack.pop()
                if v >= 0:
                    if index[v] != -1:
                        continue
                    index[v] = timer[0]
                    low[v] = timer[0]
                    timer[0] += 1
                    on_stack[v] = True
                    stack.append(~v)
                    for w in adj[v]:
                        if index[w] == -1:
                            stack.append(w)
                        elif on_stack[w]:
                            if index[w] < low[v]:
                                low[v] = index[w]
                else:
                    v = ~v
                    if stack:
                        parent = stack[-1]
                        if parent >= 0:
                            if low[v] < low[parent]:
                                low[parent] = low[v]
                    if low[v] == index[v]:
                        while True:
                            w = stack.pop()
                            on_stack[w] = False
                            comp[w] = comp_id[0]
                            if w == v:
                                break
                        comp_id[0] += 1
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
    print("YES")
    out = []
    for i in range(n):
        out.append('1' if comp[2*i] < comp[2*i+1] else '0')
    print(' '.join(out))

solve()