import sys
sys.setrecursionlimit(300000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    visited = [False] * (n + 1)
    
    sets = [[], []]
    possible = True
    
    for i in range(1, n + 1):
        if not visited[i]:
            # BFS for this component
            queue = [i]
            visited[i] = True
            color[i] = 1
            component_sets = [[], []]
            component_sets[1].append(i)
            
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        color[v] = 3 - color[u]
                        component_sets[color[v]].append(v)
                        queue.append(v)
                    else:
                        if color[v] == color[u]:
                            possible = False
            
            # Choose the larger set from this component
            if len(component_sets[1]) >= len(component_sets[2]):
                sets[0].extend(component_sets[1])
                sets[1].extend(component_sets[2])
            else:
                sets[0].extend(component_sets[2])
                sets[1].extend(component_sets[1])
    
    if not possible:
        print("NO")
        return
    
    # Try to form a set of size k
    # We start with the larger set (sets[0])
    current_set = list(sets[0])
    # We can swap elements: remove one from current_set, add one from sets[1]
    # This changes size by 0, but allows us to reach different configurations
    # To change size by 1, we need to find a component where we chose the larger set
    # and switch to the smaller set (or vice versa)
    
    # Let's track which component each node belongs to and which set we chose
    # Re-run BFS to get component info properly
    visited = [False] * (n + 1)
    components = []  # list of (set1, set2) for each component
    
    for i in range(1, n + 1):
        if not visited[i]:
            queue = [i]
            visited[i] = True
            color[i] = 1
            comp_s1 = [i]
            comp_s2 = []
            
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        color[v] = 3 - color[u]
                        if color[v] == 1:
                            comp_s1.append(v)
                        else:
                            comp_s2.append(v)
                        queue.append(v)
            
            components.append((comp_s1, comp_s2))
    
    # Greedy: for each component, choose the larger set
    current_size = 0
    chosen = []
    for s1, s2 in components:
        if len(s1) >= len(s2):
            chosen.append((s1, s2, True))  # True means we chose s1 (the larger)
            current_size += len(s1)
        else:
            chosen.append((s2, s1, True))  # True means we chose s2 (the larger)
            current_size += len(s2)
    
    # Now current_size is the maximum possible
    # We can decrease size by switching a component from larger to smaller set
    # Each switch decreases size by (len(larger) - len(smaller))
    
    # Sort components by the cost of switching (larger - smaller)
    # We want to reach exactly k, starting from current_size
    
    result = []
    remaining = k
    
    for s_large, s_small, _ in chosen:
        diff = len(s_large) - len(s_small)
        # If we still need to reduce and switching this component helps
        # We should switch if: current_size - diff >= k
        # i.e., we switch the largest diff that doesn't overshoot
        pass
    
    # Better approach: sort by diff descending, switch greedily
    chosen.sort(key=lambda x: len(x[0]) - len(x[1]), reverse=True)
    
    final_selection = []
    for s_large, s_small, _ in chosen:
        diff = len(s_large) - len(s_small)
        if current_size - diff >= k:
            final_selection.extend(s_small)
            current_size -= diff
        else:
            final_selection.extend(s_large)
    
    if current_size == k:
        print("YES")
        print(' '.join(map(str, final_selection)))
    else:
        print("NO")

solve()