import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    nL = int(data[idx]); idx += 1
    nR = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    edges = []
    degL = [0] * (nL + 1)
    degR = [0] * (nR + 1)

    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        edges.append((u, v))
        degL[u] += 1
        degR[v] += 1

    K = 0
    for i in range(1, nL + 1):
        if degL[i] > K:
            K = degL[i]
    for i in range(1, nR + 1):
        if degR[i] > K:
            K = degR[i]

    # Build adjacency lists with edge indices
    adjL = [[] for _ in range(nL + 1)]
    adjR = [[] for _ in range(nR + 1)]
    for i, (u, v) in enumerate(edges):
        adjL[u].append((v, i))
        adjR[v].append((u, i))

    color = [0] * m
    visited = [False] * m

    # For each vertex, maintain a set of used colors
    usedL = [set() for _ in range(nL + 1)]
    usedR = [set() for _ in range(nR + 1)]

    # We'll use a stack-based DFS to avoid recursion limits
    for start in range(m):
        if visited[start]:
            continue
        stack = [start]
        while stack:
            e = stack[-1]
            if visited[e]:
                stack.pop()
                continue
            visited[e] = True
            u, v = edges[e]
            # Find smallest available color not in usedL[u] or usedR[v]
            # Since degree <= K, we can just iterate from 1
            c = 1
            while c in usedL[u] or c in usedR[v]:
                c += 1
            color[e] = c
            usedL[u].add(c)
            usedR[v].add(c)
            # Push unvisited neighbors
            for (vv, ei) in adjL[u]:
                if not visited[ei]:
                    stack.append(ei)
            for (uu, ei) in adjR[v]:
                if not visited[i] if False else (not visited[ei]):
                    stack.append(ei)
            # Note: we might push duplicates, but visited check handles it

    out = []
    out.append("YES")
    out.append(" ".join(str(c) for c in color))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()