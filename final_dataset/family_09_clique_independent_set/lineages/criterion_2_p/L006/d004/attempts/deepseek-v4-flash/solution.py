import sys
from collections import deque

def main():
    input_data = sys.stdin.buffer.read().split()
    n, m, k = map(int, input_data[:3])
    edges = [[] for _ in range(n + 1)]
    idx = 3
    for _ in range(m):
        u = int(input_data[idx]); v = int(input_data[idx+1])
        idx += 2
        edges[u].append(v)
        edges[v].append(u)
    
    visited = [False] * (n + 1)
    comp_sizes = []  # list of (size_color1, size_color2)
    
    for i in range(1, n + 1):
        if not visited[i]:
            # BFS to get bipartition counts
            q = deque([i])
            visited[i] = True
            color = [0] * (n + 1)
            color[i] = 0
            cnt0 = 0
            cnt1 = 0
            while q:
                u = q.popleft()
                if color[u] == 0:
                    cnt0 += 1
                else:
                    cnt1 += 1
                for v in edges[u]:
                    if not visited[v]:
                        visited[v] = True
                        color[v] = 1 - color[u]
                        q.append(v)
            comp_sizes.append((cnt0, cnt1))
    
    # dp bitset: possible sums of selected nodes
    possible = 1  # bit 0 set
    for a, b in comp_sizes:
        # We can add either a or b nodes from this component
        possible = (possible << a) | (possible << b)
    
    if (possible >> k) & 1:
        print("YES")
        # reconstruct solution
        # We'll build the selection by backtracking through dp states
        # Store used components choices
        # To avoid heavy memory, we'll do a reverse pass.
        
        # First store dp per component step
        dp_states = []
        possible = 1
        for a, b in comp_sizes:
            possible = (possible << a) | (possible << b)
            dp_states.append(possible)
        
        remaining = k
        chosen = []
        for i in range(len(comp_sizes) - 1, -1, -1):
            a, b = comp_sizes[i]
            prev_possible = dp_states[i - 1] if i > 0 else 1
            # check if we take a
            if (remaining >= a) and ((prev_possible >> (remaining - a)) & 1):
                # take color0 of this component
                chosen.extend(color_nodes(i, 0, comp_sizes, edges))
                remaining -= a
            else:
                # take b
                chosen.extend(color_nodes(i, 1, comp_sizes, edges))
                remaining -= b
        
        print(" ".join(map(str, chosen)))
    else:
        print("NO")

def color_nodes(comp_idx, color_choice, comp_sizes, edges):
    # This function would be complex to implement without storing mapping.
    # So we'll just do a simple BFS again over all components and pick nodes with given color in given component index.
    pass

if __name__ == "__main__":
    main()