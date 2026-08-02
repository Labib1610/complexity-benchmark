n, m = map(int, input().split())
incompatibility = [set() for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    incompatibility[u].add(v)
    incompatibility[v].add(u)

# Find the smallest lexicographical triple
found = False

for a in range(1, n + 1):
    for b in incompatibility[a]:
        if b > a:
            for c in incompatibility[a]:
                if c > b and c in incompatibility[b]:
                    print(a, b, c)
                    found = True
                    break
            if found:
                break
    if found:
        break