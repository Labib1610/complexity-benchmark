import sys

def main():
    sys.setrecursionlimit(1000000)
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    # Find connected components
    visited = [False] * (n + 1)
    components = []

    def dfs_comp(v, comp):
        visited[v] = True
        comp.append(v)
        for u in adj[v]:
            if not visited[u]:
                dfs_comp(u, comp)

    for v in range(1, n + 1):
        if not visited[v]:
            comp = []
            dfs_comp(v, comp)
            comp.sort()
            components.append(comp)

    # Sort components by smallest vertex to ensure lexicographic minimality
    components.sort(key=lambda x: x[0] if x else float('inf'))

    ans = [0] * (n + 1)
    avail = [0b111] * (n + 1)

    def solve_component(vertices):
        L = len(vertices)

        def dfs(idx):
            if idx == L:
                return True
            v = vertices[idx]
            for c in (1, 2, 3):
                bit = 1 << (c - 1)
                if not (avail[v] & bit):
                    continue
                conflict = False
                changes = []
                for u in adj[v]:
                    if ans[u] != 0:
                        if ans[u] == c:
                            conflict = True
                            break
                    else:
                        if avail[u] & bit:
                            avail[u] ^= bit
                            changes.append(u)
                if conflict:
                    for u in changes:
                        avail[u] ^= bit
                    continue
                ans[v] = c
                if dfs(idx + 1):
                    return True
                ans[v] = 0
                for u in changes:
                    avail[u] ^= bit
            return False

        return dfs(0)

    possible = True
    for comp in components:
        if not solve_component(comp):
            possible = False
            break

    if not possible:
        print("NO")
    else:
        print("YES")
        print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()