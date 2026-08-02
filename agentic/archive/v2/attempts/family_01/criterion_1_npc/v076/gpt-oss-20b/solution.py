import sys

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
            neighbors[v].append(u)

    available = [0b111] * n  # bits 0,1,2 correspond to colors 1,2,3
    colorAssign = [-1] * n

    sys.setrecursionlimit(10000)

    def dfs(pos):
        if pos == n:
            return True
        node = pos
        for color in range(3):
            bit = 1 << color
            if not (available[node] & bit):
                continue
            colorAssign[node] = color
            changed = []
            conflict = False
            for nb in neighbors[node]:
                if colorAssign[nb] == -1 and (available[nb] & bit):
                    available[nb] ^= bit
                    changed.append(nb)
                    if available[nb] == 0:
                        conflict = True
                        break
            if not conflict and dfs(pos + 1):
                return True
            # restore
            for nb in changed:
                available[nb] |= bit
            colorAssign[node] = -1
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(c + 1) for c in colorAssign))
    else:
        print("NO")

if __name__ == "__main__":
    main()