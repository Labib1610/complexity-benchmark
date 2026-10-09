import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    color = [0] * n  # 0 = unassigned, 1..3 = colors

    # Precompute possible colors for each vertex as bitmask (bits 0..2 for colors 1..3)
    # We'll use 0b111 initially
    possible = [0b111] * n

    # MRV: pick unassigned vertex with fewest possible colors
    def select_vertex():
        best = -1
        best_count = 5
        for i in range(n):
            if color[i] == 0:
                cnt = bin(possible[i]).count('1')
                if cnt < best_count:
                    best_count = cnt
                    best = i
                    if cnt == 1:
                        break
        return best

    def dfs():
        v = select_vertex()
        if v == -1:
            return True
        # Try each color
        mask = possible[v]
        while mask:
            c_bit = mask & -mask
            c = (c_bit.bit_length())  # 1,2,3
            mask ^= c_bit
            # assign
            color[v] = c
            # save possible states for neighbors
            saved = []
            ok = True
            # update neighbors
            nb = adj[v]
            for u in range(n):
                if (nb >> u) & 1:
                    if color[u] == 0:
                        if possible[u] & (1 << (c-1)):
                            possible[u] &= ~(1 << (c-1))
                            saved.append(u)
                            if possible[u] == 0:
                                ok = False
                                break
                        else:
                            # already not possible, fine
                            pass
                    elif color[u] == c:
                        ok = False
                        break
            if ok and dfs():
                return True
            # revert
            for u in saved:
                possible[u] |= (1 << (c-1))
            color[v] = 0
        return False

    if dfs():
        print("YES")
        print(' '.join(str(color[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()