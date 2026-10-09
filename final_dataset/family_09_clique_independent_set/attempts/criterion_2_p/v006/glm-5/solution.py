import sys
from collections import deque

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr]); ptr += 1
    m = int(input[ptr]); ptr += 1
    k = int(input[ptr]); ptr += 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input[ptr]); ptr += 1
        v = int(input[ptr]); ptr += 1
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)
    sets = [[], []]
    possible = True

    for i in range(1, n + 1):
        if color[i] == 0:
            q = deque([i])
            color[i] = 1
            comp_sets = [[], []]
            comp_sets[0].append(i)
            
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        comp_sets[color[v] - 1].append(v)
                        q.append(v)
                    elif color[v] == color[u]:
                        possible = False
            
            if len(comp_sets[0]) < len(comp_sets[1]):
                sets[0].extend(comp_sets[0])
                sets[1].extend(comp_sets[1])
            else:
                sets[0].extend(comp_sets[1])
                sets[1].extend(comp_sets[0])

    if not possible:
        print("NO")
        return

    if len(sets[0]) >= k:
        print("YES")
        print(' '.join(map(str, sets[0][:k])))
    elif len(sets[1]) >= k:
        print("YES")
        print(' '.join(map(str, sets[1][:k])))
    else:
        print("NO")

if __name__ == '__main__':
    solve()