import sys
import sys
sys.setrecursionlimit(10000000)

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

    # Check if graph is 3-colorable and find lexicographically smallest coloring
    # Use backtracking with pruning, n <= 40, but graph is small enough for meet-in-middle? Actually we can use DP over subsets for bipartite? No, 3-coloring is NP-hard, but n=40 is too big for general 3-coloring.
    # But constraints are small? n=40, m up to 780. 3^40 is impossible. Must use meet-in-the-middle or branch and bound.
    # However, this is a known problem: 3-coloring with lexicographically smallest. n=40 suggests meet-in-the-middle or DP over subsets with 3^(n/2) ~ 3^20 ~ 3.4e9 too big.
    # Wait, maybe the graph is complete? No, it's general.
    # Let's think: 3-coloring is NP-complete, but n=40 is small enough for backtracking with pruning? In worst case, 3^40 is impossible.
    # But maybe the intended solution is to use the fact that we only need lexicographically smallest, so we can try to assign greedily and check if the remaining graph is 3-colorable.
    # Checking 3-colorability for n=40 is still hard, but we can use backtracking with forward checking and MRV heuristic.
    # Actually, n=40 is too big for general 3-coloring. There must be a trick.
    # Wait, the problem says "exactly three independent life-support grids" and "each module must be connected to exactly one of these three grids". That's just 3-coloring.
    # But n=40 is too big for general 3-coloring. Maybe the graph is complete? No.
    # Let's re-read: "n ≤ 40" and "m ≤ n(n-1)/2". So it's a general graph.
    # 3-coloring is NP-complete, so there is no polynomial algorithm unless P=NP. But n=40 is small enough for meet-in-the-middle with 3^(n/2) ~ 3^20 ~ 3.4e9, too big.
    # Maybe we can use the fact that we only need lexicographically smallest, so we can try to assign greedily and use a SAT solver? But we can't use external libraries.
    # Wait, maybe the intended solution is to use backtracking with pruning and it will pass because the graph is sparse? But m can be up to 780, which is dense.
    # Let's think again: n=40, 3^40 is impossible. But maybe we can use the fact that the graph is 3-colorable? No, we need to check.
    # Actually, I recall that 3-coloring can be solved in O(2^n * n) using inclusion-exclusion or DP over subsets, but 2^40 is too big.
    # Wait, maybe the graph is complete? No.
    # Let's check the examples: Example 1 has n=4, m=5, which is K4 minus one edge. Example 2 is K4, which is not 3-colorable.
    # So n=40 is the maximum, but maybe the test cases are small? The problem says n ≤ 40, but maybe the intended solution is backtracking with pruning and it will pass because the graph is not too dense? But worst-case is still exponential.
    # Actually, I think the intended solution is to use the fact that we can try to assign greedily and use a 3-coloring algorithm that works well in practice, like backtracking with MRV and forward checking.
    # But to be safe, we can use the following approach: for each module from 1 to n, try to assign the smallest possible color (1,2,3) such that the remaining graph is 3-colorable. To check 3-colorability, we can use backtracking with pruning.
    # Since n=40, the backtracking might be okay if we use bitmasks and pruning.
    # Let's implement a function is_colorable() that checks if the current partial assignment can be extended to a full 3-coloring.
    # We'll use recursion with memoization on the state (vertex, mask of used colors for each vertex?) That's too big.
    # Actually, we can use the following: for each vertex, we maintain a bitmask of available colors (1-3). Initially all 111. When we assign a color to a vertex, we remove that color from its neighbors.
    # We can use backtracking with MRV (choose vertex with fewest available colors) and forward checking.
    # Since n=40, the branching factor is at most 3, and the depth is at most 40, so worst-case 3^40 is impossible, but with MRV and forward checking, it might be okay for the given constraints? Probably not in the worst case.
    # But maybe the problem is from a contest where n=40 is small enough for meet-in-the-middle? Let's think of another approach.
    # Actually, I think the intended solution is to use the fact that the graph is 3-colorable, and we need lexicographically smallest. We can use the following greedy: for i from 1 to n, try to assign color 1,2,3, and check if the remaining graph is 3-colorable. To check 3-colorability, we can use a backtracking algorithm that is efficient for n=40.
    # Let's implement a backtracking 3-coloring algorithm with MRV and forward checking. It should be fast enough for n=40 in practice.
    # We'll represent the graph as adjacency bitmasks.
    # We'll maintain an array color of length n, where color[i] = 0 means unassigned, else 1,2,3.
    # We'll also maintain for each vertex a bitmask of available colors (bits 0-2).
    # When we assign a color to a vertex, we remove that color from its neighbors.
    # If any vertex has no available colors, backtrack.
    # We'll use recursion and try to color the vertex with the fewest available colors (MRV).
    # Since we need lexicographically smallest, we'll try to assign the smallest possible color to the current vertex in the main loop.
    # But for the greedy assignment, we need to be careful: when we try to assign a color to vertex i, we need to check if there exists a valid coloring with that assignment. So we can use a recursive function that tries to color the graph with the given partial assignment.
    # Let's implement it.

    # Precompute adjacency bitmask
    adj_mask = [0] * n
    for i in range(n):
        adj_mask[i] = adj[i]

    # We'll use a recursive function to check if the graph is 3-colorable given a partial assignment.
    # We'll pass the current color array and the available colors for each vertex.
    # To make it efficient, we'll use bitmasks for available colors.
    # We'll also use memoization on the tuple of available colors? That's too big.
    # Let's just implement backtracking with MRV and forward checking.

    def is_colorable(colors, avail):
        # colors: list of int, 0 = unassigned, else 1,2,3
        # avail: list of int, bitmask of available colors (bits 0-2)
        # Find unassigned vertex with fewest available colors
        best = -1
        best_mask = 0
        for i in range(n):
            if colors[i] == 0:
                mask = avail[i]
                if mask == 0:
                    return False
                if best == -1 or bin(mask).count('1') < bin(best_mask).count('1'):
                    best = i
                    best_mask = mask
                    if bin(mask).count('1') == 1:
                        break
        if best == -1:
            return True  # all assigned
        # Try each color
        for c in range(3):
            if (best_mask >> c) & 1:
                # assign color c+1 to vertex best
                colors[best] = c + 1
                # update avail for neighbors
                old_avail = []
                # remove color c from neighbors
                possible = True
                for nb in range(n):
                    if (adj_mask[best] >> nb) & 1:
                        old_avail.append((nb, avail[nb]))
                        if (avail[nb] >> c) & 1:
                            avail[nb] &= ~(1 << c)
                            if avail[nb] == 0:
                                possible = False
                if possible:
                    if is_colorable(colors, avail):
                        return True
                # backtrack
                for nb, old in old_avail:
                    avail[nb] = old
                colors[best] = 0
        return False

    # Greedy assignment
    colors = [0] * n
    avail = [0b111] * n
    for i in range(n):
        # try to assign smallest possible color
        for c in range(3):
            # check if we can assign color c+1 to i
            # check if any neighbor has that color already
            ok = True
            for nb in range(n):
                if (adj_mask[i] >> nb) & 1:
                    if colors[nb] == c + 1:
                        ok = False
                        break
            if not ok:
                continue
            # try to assign and check if the rest is colorable
            colors[i] = c + 1
            # update avail for neighbors
            old_avail = []
            possible = True
            for nb in range(n):
                if (adj_mask[i] >> nb) & 1:
                    old_avail.append((nb, avail[nb]))
                    if (avail[nb] >> c) & 1:
                        avail[nb] &= ~(1 << c)
                        if avail[nb] == 0:
                            possible = False
            if possible:
                # check if the remaining graph is colorable
                if is_colorable(colors, avail):
                    break
                else:
                    # revert
                    for nb, old in old_avail:
                        avail[nb] = old
                    colors[i] = 0
            else:
                # revert
                for nb, old in old_avail:
                    avail[nb] = old
                colors[i] = 0
        else:
            # no color works
            print("NO")
            return
    # check if all assigned
    if 0 in colors:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, colors)))

if __name__ == "__main__":
    solve()