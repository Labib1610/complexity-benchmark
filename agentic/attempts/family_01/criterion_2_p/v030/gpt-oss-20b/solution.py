import sys

def main():
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

    color = [-1] * n
    result = [0] * n
    for start in range(n):
        if color[start] != -1:
            continue
        stack = [start]
        color[start] = 0
        comp = [start]
        bip = True
        while stack:
            u = stack.pop()
            cu = color[u]
            for v in adj[u]:
                cv = color[v]
                if cv == -1:
                    color[v] = cu ^ 1
                    stack.append(v)
                    comp.append(v)
                elif cv == cu:
                    bip = False
                    break
            if not bip:
                break
        if not bip:
            sys.stdout.write("NO")
            return
        min_node = min(comp)
        min_col = color[min_node]
        for node in comp:
            if color[node] == min_col:
                result[node] = 1
            else:
                result[node] = 2

    out_lines = ["YES", " ".join(map(str, result))]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()