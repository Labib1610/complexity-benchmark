from itertools import product

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    edges.append((u, v))
coloring = [-1] * n

def valid(colors):
    for u, v in edges:
        if colors[u] == colors[v]:
            return False
    return True

for c1, c2, c3 in product(range(3), repeat=3):
    coloring[0], coloring[1], coloring[2] = c1, c2, c3
    for i in range(3, n):
        for j in range(3):
            if coloring[i] != -1:
                break
            if all(coloring[u] != j for u in (x for x in range(i) if (i, x) in edges or (x, i) in edges)):
                coloring[i] = j
    else:
        if valid(coloring):
            print('YES')
            print(*(1 + c for c in coloring))
            exit()
print('NO')