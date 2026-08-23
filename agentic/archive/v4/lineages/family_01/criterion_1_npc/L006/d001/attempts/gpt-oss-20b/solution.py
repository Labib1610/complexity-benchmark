import sys
sys.setrecursionlimit(10000)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    neighbors = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if v not in neighbors[u]:
            neighbors[u].append(v)
        if u not in neighbors[v]:
            neighbors[v].append(u)

    color = [0] * n
    allowed_init = [7] * n  # bits 0,1,2 for colors 1,2,3

    def dfs(idx, allowed):
        if idx == n:
            return True
        # try colors 1..3
        for c in (1, 2, 3):
            # check conflict with already colored neighbors
            conflict = False
            for nb in neighbors[idx]:
                if nb < idx and color[nb] == c:
                    conflict = True
                    break
            if conflict:
                continue
            new_allowed = allowed[:]  # copy
            # remove color c from uncolored neighbors
            mask = ~(1 << (c - 1))
            for nb in neighbors[idx]:
                if nb > idx:
                    new_allowed[nb] &= mask
                    if new_allowed[nb] == 0:
                        conflict = True
                        break
            if conflict:
                continue
            color[idx] = c
            if dfs(idx + 1, new_allowed):
                return True
            color[idx] = 0  # backtrack
        return False

    if dfs(0, allowed_init):
        print("YES")
        print(' '.join(str(color[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    main()