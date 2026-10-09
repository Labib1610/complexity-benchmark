```python
import sys
sys.setrecursionlimit(1 << 25)

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    m = int(input[ptr])
    ptr += 1
    
    size = 2 * n
    original_adj = [[] for _ in range(size)]
    transposed_adj = [[] for _ in range(size)]
    
    for _ in range(m):
        l1 = int(input[ptr])
        ptr += 1
        l2 = int(input[ptr])
        ptr += 1
        
        # First implication: -l1 -> l2
        a = -l1
        var_a = abs(a)
        node_a = 2 * (var_a - 1) if a > 0 else 2 * (var_a - 1) + 1
        var_b = abs(l2)
        node_b = 2 * (var_b - 1) if l2 > 0 else 2 * (var_b - 1) + 1
        original_adj[node_a].append(node_b)
        transposed_adj[node_b].append(node_a)
        
        # Second implication: -l2 -> l1
        a = -l2
        var_a = abs(a)
        node_a2 = 2 * (var_a - 1) if a > 0 else 2 * (var_a - 1) + 1
        var_b2 = abs(l1)
        node_b2 = 2 * (var_b2 - 1) if l1 > 0 else 2 * (var_b2 - 1) + 1
        original_adj[node_a2].append(node_b2)
        transposed_adj[node_b2].append(node_a2)
    
    stack = []
    visited = [False] * size
    
    for i in range(size):
        if not visited[i]:
            dfs_stack = [(i, False)]
            while dfs_stack:
                current, processed = dfs_stack.pop()
                if processed:
                    stack.append(current)
                    continue
                if visited[current]:
                    continue
                visited[current] = True
                dfs_stack.append((current, True))
                for neighbor in original_adj[current]:
                    if not visited[neighbor]:
                        dfs_stack.append((neighbor, False))
    
    component = [0] * size
    current_comp = 0
    visited2 = [False