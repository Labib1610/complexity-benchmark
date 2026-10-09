def solve():
    n, m, k = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    if m == 0:
        print("YES")
        print()
        return

    def is_watched(guards, edge):
        u, v = edge
        return u in guards or v in guards

    def check(guards):
        for edge in edges:
            if not is_watched(guards, edge):
                return False
        return True

    for i in range(1 << n):
        guards = []
        count = 0
        for j in range(n):
            if (i >> j) & 1:
                guards.append(j + 1)
                count += 1

        if count <= k and check(guards):
            print("YES")
            print(*guards)
            return

    print("NO")

solve()