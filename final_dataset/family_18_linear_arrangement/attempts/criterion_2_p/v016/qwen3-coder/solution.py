import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    B = int(data[idx])
    idx += 1
    
    edges = []
    adj = defaultdict(list)
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        idx += 2
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # Since the graph is connected, has n-1 edges, and sum of degrees is 2(n-1),
    # it's a tree. Also it's bipartite.
    
    # Find bipartition
    color = [-1] * n
    def bipartite_check(start):
        queue = deque()
        queue.append(start)
        color[start] = 0
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    return False
        return True
    
    # Since graph is connected, we can start from node 0
    bipartite_check(0)
    
    # Partition nodes
    set0 = [i for i in range(n) if color[i] == 0]
    set1 = [i for i in range(n) if color[i] == 1]
    
    # Try to place set0 on the left half and set1 on the right half to minimize cost
    # The optimal strategy is to place one set on the first |set0| positions
    # and the other set on the last |set1| positions.
    
    # We'll try both assignments: set0 on left and set1 on right, and vice versa
    
    def compute_cost(left_nodes, right_nodes):
        # Assign left_nodes to positions 1 to len(left_nodes)
        # Assign right_nodes to positions len(left_nodes)+1 to n
        pos = [0] * n
        left_sorted = sorted(left_nodes)
        right_sorted = sorted(right_nodes)
        for i, node in enumerate(left_sorted):
            pos[node] = i + 1
        for i, node in enumerate(right_sorted):
            pos[node] = len(left_nodes) + i + 1
        # Compute total cost
        total = 0
        for u, v in edges:
            total += abs(pos[u] - pos[v])
        return total, pos
    
    cost1, pos1 = compute_cost(set0, set1)
    cost2, pos2 = compute_cost(set1, set0)
    
    if cost1 <= B:
        print("YES")
        print(' '.join(map(str, pos1)))
    elif cost2 <= B:
        print("YES")
        print(' '.join(map(str, pos2)))
    else:
        print("NO")

if __name__ == "__main__":
    main()