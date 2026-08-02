import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    assign = [0] * n
    color_masks = [0, 0, 0]  # colors 1,2,3

    def forward_check():
        for j in range(n):
            if assign[j] == 0:
                forbidden = 0
                if adj[j] & color_masks[0]:
                    forbidden |= 1
                if adj[j] & color_masks[1]:
                    forbidden |= 2
                if adj[j] & color_masks[2]:
                    forbidden |= 4
                if forbidden == 7:  # all colors forbidden
                    return False
        return True

    def dfs(idx):
        if idx == n:
            return True
        for c in range(3):  # colors 1..3
            if (adj[idx] & color_masks[c]) == 0:
                assign[idx] = c + 1
                color_masks[c] |= 1 << idx
                if forward_check():
                    if dfs(idx + 1):
                        return True
                color_masks[c] ^= 1 << idx
                assign[idx] = 0
        return False

    if dfs(0):
        out = ["YES", " ".join(map(str, assign))]
    else:
        out = ["NO"]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()