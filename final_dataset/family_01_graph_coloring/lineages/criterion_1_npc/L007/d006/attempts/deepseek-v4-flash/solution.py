import sys
sys.setrecursionlimit(1000000)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * n
    # avail[i] bitmask of available colors (bits 0,1,2)
    avail = [7] * n
    
    def backtrack(count):
        if count == n:
            return True
        # find uncolored vertex with min available colors
        best = -1
        best_mask = 0
        best_bits = 10
        for i in range(n):
            if color[i] == -1:
                bits = bin(avail[i]).count('1')
                if bits == 0:
                    return False
                if bits < best_bits:
                    best_bits = bits
                    best = i
                    best_mask = avail[i]
                    if bits == 1:
                        break
        # try colors
        for c in range(3):
            if (best_mask >> c) & 1:
                # assign
                color[best] = c
                # save old avail for neighbors
                old = []
                for nb in adj[best]:
                    if color[nb] == -1:
                        old.append((nb, avail[nb]))
                        avail[nb] &= ~(1 << c)
                if backtrack(count + 1):
                    return True
                # backtrack
                for nb, old_mask in old:
                    avail[nb] = old_mask
                color[best] = -1
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(str(c+1) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    solve()