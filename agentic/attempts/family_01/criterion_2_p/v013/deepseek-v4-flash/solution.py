import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    color = [-1] * n
    comps = []  # list of (nodes, color_in_comp) for each component

    for i in range(n):
        if color[i] != -1:
            continue
        # BFS to color the component
        q = deque([i])
        color[i] = 0
        nodes = [i]
        while q:
            u = q.popleft()
            for v in graph[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                    nodes.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
        # separate nodes by color
        c0 = [u for u in nodes if color[u] == 0]
        c1 = [u for u in nodes if color[u] == 1]
        comps.append((c0, c1))

    # Now we have a bipartite graph, need lexicographically smallest assignment
    # For each component, we can flip colors. We want lexicographically smallest overall.
    # Process vertices in order, decide orientation of each component when first encountered.
    assign = [-1] * n
    comp_id = [-1] * n
    for idx, (c0, c1) in enumerate(comps):
        for u in c0:
            comp_id[u] = idx
        for u in c1:
            comp_id[u] = idx

    # For each component, we can choose which color gets 1.
    # To get lexicographically smallest, process vertices in order.
    # When we see a vertex not assigned yet, we decide the orientation of its component.
    # We want the smallest possible value at the earliest position.
    # So for each component, we can precompute the two possible assignments.
    # Then greedily assign.

    # Precompute for each component the two possible assignments
    comp_assign = []  # list of (list, list) for flip=False/True
    for c0, c1 in comps:
        # flip=False: c0->1, c1->2
        arr_false = [0] * n
        for u in c0:
            arr_false[u] = 1
        for u in c1:
            arr_false[u] = 2
        # flip=True: c0->2, c1->1
        arr_true = [0] * n
        for u in c0:
            arr_true[u] = 2
        for u in c1:
            arr_true[u] = 1
        comp_assign.append((arr_false, arr_true))

    # Greedy: process vertices in order, when we hit an unassigned vertex, decide orientation
    result = [0] * n
    used = [False] * len(comps)
    for i in range(n):
        if result[i] != 0:
            continue
        cid = comp_id[i]
        # Try flip=False first
        arr_false, arr_true = comp_assign[cid]
        # Check if flip=False gives smaller at position i
        # Since we process in order, we can just choose the orientation that gives 1 at i if possible
        # Actually we need to choose the orientation that makes the whole sequence lexicographically smallest.
        # Since we process from left to right, at the first unassigned vertex, we can decide.
        # If arr_false[i] < arr_true[i], choose false; if > choose true; if equal, need to look further.
        # But since we process in order, we can just compare the two full assignments for this component.
        # However, we need to consider that later components are not decided yet.
        # The standard approach: for each component, we can decide its orientation when we first encounter a vertex of it.
        # At that point, we choose the orientation that gives the smaller value at the current position.
        # If equal, we need to look at the next position in the component, but since we process in order,
        # we can just compare the two assignments from this position onward.
        # Simpler: we can just try both and pick the one that yields lexicographically smaller result.
        # But n is large, so we need O(n) total.
        # Actually, we can just decide by comparing the two assignments at the first differing position.
        # Since we process in order, we can just compare the two arrays from index i.
        # But that could be O(n^2) in worst case. However, we can do it efficiently by just comparing the two assignments
        # for this component only, because other components are independent and will be decided later.
        # So we can just compare arr_false and arr_true from index i onward, but only within this component.
        # Since each component is processed once, total O(n).
        # Let's do that.
        # Find first position where they differ
        j = i
        while j < n and arr_false[j] == arr_true[j]:
            j += 1
        if j < n:
            if arr_false[j] < arr_true[j]:
                use_false = True
            else:
                use_false = False
        else:
            use_false = True  # they are identical
        if use_false:
            for u in range(n):
                if comp_id[u] == cid:
                    result[u] = arr_false[u]
        else:
            for u in range(n):
                if comp_id[u] == cid:
                    result[u] = arr_true[u]
        used[cid] = True

    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    solve()