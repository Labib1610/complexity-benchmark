import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    color = [-1] * n
    possible = True

    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            stack = [i]
            while stack:
                u = stack.pop()
                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        stack.append(v)
                    elif color[v] == color[u]:
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break

    if not possible:
        print("NO")
        return

    # Now we have a valid bipartition, but we need lexicographically smallest assignment
    # We can try to assign 1 to as many early nodes as possible
    # We'll do a BFS/DFS with priority to assign 1 if possible
    assign = [0] * n
    visited = [False] * n

    for start in range(n):
        if visited[start]:
            continue
        # Try to assign start to 1
        assign[start] = 1
        visited[start] = True
        stack = [start]
        ok = True
        while stack:
            u = stack.pop()
            for v in graph[u]:
                if not visited[v]:
                    assign[v] = 3 - assign[u]  # opposite
                    visited[v] = True
                    stack.append(v)
                elif assign[v] == assign[u]:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            # revert this component and assign start to 2 instead
            # reset visited for this component
            comp = [start]
            visited[start] = False
            stack = [start]
            while stack:
                u = stack.pop()
                for v in graph[u]:
                    if visited[v]:
                        visited[v] = False
                        comp.append(v)
                        stack.append(v)
            assign[start] = 2
            visited[start] = True
            stack = [start]
            while stack:
                u = stack.pop()
                for v in graph[u]:
                    if not visited[v]:
                        assign[v] = 3 - assign[u]
                        visited[v] = True
                        stack.append(v)

    print("YES")
    print(" ".join(str(x) for x in assign))

if __name__ == "__main__":
    solve()