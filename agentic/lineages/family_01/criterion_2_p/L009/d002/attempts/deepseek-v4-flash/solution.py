import sys

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
    ans = [0] * n

    for start in range(n):
        if color[start] != -1:
            continue
        # BFS to check bipartiteness and assign colors
        queue = [start]
        color[start] = 0
        comp = [start]
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    queue.append(v)
                    comp.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return

        # Now we have a connected component with colors 0 and 1.
        # We want lexicographically smallest assignment of 1/2.
        # For each component, we can try both colorings and pick the lexicographically smaller one.
        # Since we process components in order of smallest index, we can decide greedily.
        # But we need to ensure global lexicographic order.
        # Instead, we'll collect components and then decide.

        # For now, store the component and its two possible assignments
        # We'll handle after processing all components.
        # Actually, we can decide per component independently because colors are independent.
        # For lexicographic order, for each component, we can choose the assignment that gives smaller value at the smallest index in the component.
        # But careful: the smallest index in the component might be the same for both assignments, so we need to compare the whole component.
        # Since we process components in order of smallest index, we can decide greedily.
        # Let's find the smallest index in this component.
        min_idx = min(comp)
        # Try both assignments for this component
        # assignment 0: color 0 -> 1, color 1 -> 2
        # assignment 1: color 0 -> 2, color 1 -> 1
        # We'll build both and compare lexicographically, but only for the component positions.
        # Since we process in order, we can just pick the better one.
        # But we need to compare the whole component's values in the final array.
        # We'll store the component and decide later.
        # To keep it simple, we'll store components and decide after all are found.
        pass

    # Re-initialize for actual assignment
    color = [-1] * n
    ans = [0] * n

    for start in range(n):
        if color[start] != -1:
            continue
        # BFS
        queue = [start]
        color[start] = 0
        comp = [start]
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    queue.append(v)
                    comp.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return

        # Now decide assignment for this component
        # Build two possible assignments for this component
        # assignment 0: color 0 -> 1, color 1 -> 2
        # assignment 1: color 0 -> 2, color 1 -> 1
        # We'll compare them by the values at the component's vertices in order of index
        comp_sorted = sorted(comp)
        assign0 = [0] * n
        assign1 = [0] * n
        for v in comp_sorted:
            if color[v] == 0:
                assign0[v] = 1
                assign1[v] = 2
            else:
                assign0[v] = 2
                assign1[v] = 1

        # Compare lexicographically
        better = 0  # 0 means assign0, 1 means assign1
        for v in comp_sorted:
            if assign0[v] < assign1[v]:
                better = 0
                break
            elif assign0[v] > assign1[v]:
                better = 1
                break
        # If all equal, keep 0

        for v in comp_sorted:
            if better == 0:
                ans[v] = assign0[v]
            else:
                ans[v] = assign1[v]

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()