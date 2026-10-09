k, t = map(int, input().split())
seen = [False] * (k + 1)

for _ in range(t):
    x, y, z = map(int, input().split())
    seen[x] = True

for i in range(1, k + 1):
    if not seen[i]:
        print(i)
        break