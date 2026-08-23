import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [[] for _ in range(n)]
    p = 2
    for _ in range(m):
        u = int(data[p]) - 1
        v = int(data[p + 1]) - 1
        p += 2
        adj[u].append(v)
        adj[v].append(u)

    ans = [0] * n
    possible = True
    stack = []

    for i in range(n):
        if ans[i]:
            continue
        ans[i] = 1
        stack.append(i)
        while stack:
            u = stack.pop()
            need = 3 - ans[u]
            for v in adj[u]:
                av = ans[v]
                if av == 0:
                    ans[v] = need
                    stack.append(v)
                elif av != need:
                    possible = False
                    stack.clear()
                    break
        if not possible:
            break

    out = sys.stdout.buffer
    if not possible:
        out.write(b"NO\n")
    else:
        out.write(b"YES\n")
        out.write(b" ".join(str(x).encode() for x in ans))
        out.write(b"\n")

if __name__ == "__main__":
    solve()