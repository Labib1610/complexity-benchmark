import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        adj[v].append(u)

    # We want the lexicographically smallest valid assignment.
    # We assign positions to dials 0 to n-1 sequentially.
    # For each dial i, we try positions 1, 2, 3 in increasing order.
    # A position p is valid for dial i if no neighbor j < i has position p.
    # Since we assign in order, neighbors j > i are not yet assigned, so they don't constrain i yet.
    # This greedy approach works because:
    # 1. If we can assign a valid position to dial i, we do so.
    # 2. If no position is valid for dial i, it means all 3 positions are forbidden.
    #    A position is forbidden if some neighbor j < i has that position.
    #    Since there are only 3 positions, if all are forbidden, dial i must have at least 3 neighbors j < i.
    #    Let these neighbors be $j_1, j_2, j_3$ with positions 1, 2, 3 respectively.
    #    These neighbors form a clique among themselves (due to the problem's structure:
    #    if $j_1, j_2$ are neighbors of $i$ and have different positions, they must be adjacent,
    #    otherwise we could recolor one of them to match the other, reducing the number of distinct colors around $i$).
    #    Actually, the logic is simpler: if we cannot assign a color to $i$, it implies the existence of a $K_4$.
    #    The neighbors $j < i$ that block colors must use distinct colors.
    #    If 3 colors are blocked, there are 3 neighbors $j_1, j_2, j_3$ with colors 1, 2, 3.
    #    Since $j_1$ and $j_2$ have different colors, they must be adjacent (otherwise $j_1$ could have taken $j_2$'s color).
    #    Similarly for $j_2, j_3$ and $j_1, j_3$.
    #    Thus $i, j_1, j_2, j_3$ form a $K_4$, which makes the graph non-3-colorable.
    #    In this case, we correctly output NO.
    # 3. If a valid assignment exists, the greedy choice (smallest valid position) preserves the existence
    #    of a solution and yields the lexicographically smallest one.

    res = [0] * n
    possible = True

    for i in range(n):
        # Determine which colors are used by assigned neighbors
        used = [False] * 4 # Indices 1, 2, 3
        for neighbor in adj[i]:
            if neighbor < i:
                used[res[neighbor]] = True
        
        # Find the smallest available color
        chosen_color = 0
        for color in range(1, 4):
            if not used[color]:
                chosen_color = color
                break
        
        if chosen_color == 0:
            possible = False
            break
        
        res[i] = chosen_color

    if not possible:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, res)) + "\n")

if __name__ == '__main__':
    solve()