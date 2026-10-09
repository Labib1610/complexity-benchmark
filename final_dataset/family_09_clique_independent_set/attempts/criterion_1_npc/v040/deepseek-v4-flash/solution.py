import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    n, m, k = map(int, input_data[:3])
    edges = [[] for _ in range(n)]
    for i in range(m):
        u, v = map(int, input_data[3 + 2*i:5 + 2*i])
        edges[u-1].append(v-1)
        edges[v-1].append(u-1)

    adj_mask = [0] * n
    for i in range(n):
        mask = 0
        for v in edges[i]:
            mask |= (1 << v)
        adj_mask[i] = mask

    # backtracking
    chosen = []
    possible = False

    def backtrack(start, selected_mask):
        nonlocal possible
        if len(chosen) == k:
            possible = True
            return True
        if start >= n:
            return False
        # Bound: if even picking all remaining won't reach k
        if len(chosen) + (n - start) < k:
            return False

        # skip current
        if backtrack(start + 1, selected_mask):
            return True

        # take current if not adjacent to selected
        if (selected_mask & adj_mask[start]) == 0:
            chosen.append(start + 1)
            if backtrack(start + 1, selected_mask | (1 << start)):
                return True
            chosen.pop()
        return False

    if backtrack(0, 0):
        print("YES")
        print(" ".join(map(str, chosen)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()