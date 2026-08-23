import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    N = next(it)
    M = next(it)
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u = next(it)
        v = next(it)
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (N + 1)  # 0 or 1
    ans = [0] * (N + 1)     # final 1 or 2

    for start in range(1, N + 1):
        if color[start] != -1:
            continue
        stack = [start]
        color[start] = 0
        comp_nodes = [start]
        min_node = start
        bipartite = True
        while stack:
            u = stack.pop()
            cu = color[u]
            for v in adj[u]:
                cv = color[v]
                if cv == -1:
                    color[v] = cu ^ 1
                    stack.append(v)
                    comp_nodes.append(v)
                    if v < min_node:
                        min_node = v
                elif cv == cu:
                    bipartite = False
                    break
            if not bipartite:
                break
        if not bipartite:
            sys.stdout.write("NO")
            return
        # map colors so that min_node gets 1
        if color[min_node] == 0:
            for node in comp_nodes:
                ans[node] = color[node] + 1
        else:
            for node in comp_nodes:
                ans[node] = 2 - color[node]

    out_lines = ["YES", " ".join(map(str, ans[1:]))]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()