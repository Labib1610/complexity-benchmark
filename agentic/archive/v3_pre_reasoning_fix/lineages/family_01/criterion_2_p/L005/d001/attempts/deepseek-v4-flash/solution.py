import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    graph = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        graph[u].append(v)
        graph[v].append(u)

    color = [0] * n  # 0 uncolored, 1 or 2

    for start in range(n):
        if color[start]:
            continue
        color[start] = 1
        q = [start]
        head = 0
        while head < len(q):
            u = q[head]; head += 1
            need = 1 if color[u] == 2 else 2
            for v in graph[u]:
                if color[v] == 0:
                    color[v] = need
                    q.append(v)
                elif color[v] == color[u]:
                    sys.stdout.write("NO\n")
                    return
    sys.stdout.write("YES\n" + " ".join(map(str, color)) + "\n")

if __name__ == "__main__": main()

Need note if graph self-loop causes color[v] already assigned maybe in iteration from neighbor? We check conflict.

One subtlety: In BFS, when visiting u and considering neighbor v, if color[v]==0, set to need. If later when processing some other node, there is an edge to u with conflict, works. If graph has self-loop, the self edge is checked only when processing u. By then color[u]=1, color[v]=1, conflict; NO. Good.

Potential bug: We process vertices in for i range(n). Suppose graph disconnected, start i maybe not colored but has earlier vertex with smaller index in same component? Since all prev processed; if i not colored, no prev in component, so i is min. assign 1. Good.

Let's maybe include comments? Not necessary.Code: