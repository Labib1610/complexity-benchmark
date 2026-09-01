import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n, m = data[0], data[1]

parent = list(range(n))
size = [1] * n
parity = [0] * n  # parity[x] = color[x] XOR color[parent[x]]

def find(x):
    r = x
    total = 0
    while parent[r] != r:
        total ^= parity[r]
        r = parent[r]

    cur = x
    prefix = 0
    while parent[cur] != cur:
        nxt = parent[cur]
        edge = parity[cur]
        parent[cur] = r
        parity[cur] = total ^ prefix
        prefix ^= edge
        cur = nxt

    return r, total

possible = True
idx = 2

for _ in range(m):
    u = data[idx] - 1
    v = data[idx + 1] - 1
    idx += 2

    ru, pu = find(u)
    rv, pv = find(v)

    if ru == rv:
        if (pu ^ pv) != 1:
            possible = False
            break
    else:
        root_parity = pu ^ pv ^ 1
        if size[ru] < size[rv]:
            parent[ru] = rv
            parity[ru] = root_parity
            size[rv] += size[ru]
        else:
            parent[rv] = ru
            parity[rv] = root_parity
            size[ru] += size[rv]

if not possible:
    print("NO")
else:
    orientation = [-1] * n
    answer = [0] * n

    for i in range(n):
        root, p = find(i)
        if orientation[root] == -1:
            orientation[root] = p
        answer[i] = (p ^ orientation[root]) + 1

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, answer)))
    sys.stdout.write("\n")