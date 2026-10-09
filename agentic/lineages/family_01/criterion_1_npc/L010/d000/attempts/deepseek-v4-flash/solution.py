n, m = map(int, input().split())
conflicts = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    conflicts[u].append(v)
    conflicts[v].append(u)

assignment = [0] * n

def backtrack(idx):
    if idx == n:
        return True
    for color in range(1, 4):
        ok = True
        for neighbor in conflicts[idx]:
            if assignment[neighbor] == color:
                ok = False
                break
        if ok:
            assignment[idx] = color
            if backtrack(idx + 1):
                return True
            assignment[idx] = 0
    return False

if backtrack(0):
    print("YES")
    print(" ".join(map(str, assignment)))
else:
    print("NO")