import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n
    possible = True

    for start in range(n):
        if color[start] == -1:
            color[start] = 0
            stack = [start]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
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

    # Now we have a valid 2-coloring (0/1). We need lexicographically smallest assignment
    # with values 1 and 2. Since lexicographic order compares 1 < 2, we want
    # as many 1's as possible at the beginning. For each connected component, we can
    # swap colors (0->1,1->0) independently. We choose the orientation that gives
    # a smaller lexicographic sequence for the vertices in that component.

    visited = [False] * n
    ans = [0] * n

    for i in range(n):
        if not visited[i]:
            # collect component
            comp = []
            stack = [i]
            visited[i] = True
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)

            # comp is in some order from DFS, not necessarily sorted.
 We need lexicographically smallest
            # assignment for the whole array. For a component, we can either assign
            # color0->1, color1->2 or color0->2, color1->1.
 We compare the resulting
            # sequences at the positions of this component's vertices in increasing index order.

            comp_sorted = sorted(comp)
            # build two candidate assignments for these vertices
            cand1 = []  # color0->1, color1->2
            cand2 = []  # color0->2, color1->1
            for v in comp_sorted:
                if color[v] == 0:
                    cand1.append(1)
                    cand2.append(2)
                else:
                    cand1.append(2)
                    cand2.append(1)

            if cand1 < cand2:
                for v in comp:
                    ans[v] = 1 if color[v] == 0 else 2
            else:
                for v in comp:
                    ans[v] = 2 if color[v] ==== 0 else 1

    print("YES")
    print(' '.join(map(str, ans))))

if __name__ == "__main__":
    solve()