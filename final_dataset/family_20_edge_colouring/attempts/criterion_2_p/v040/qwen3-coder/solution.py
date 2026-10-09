import sys
from collections import defaultdict
import heapq

def main():
    import sys
    import threading

    def solve():
        N_in, N_out, M = map(int, sys.stdin.readline().split())
        edges = []
        degree_in = [0] * (N_in + 1)
        degree_out = [0] * (N_out + 1)
        
        for _ in range(M):
            u, v = map(int, sys.stdin.readline().split())
            edges.append((u, v))
            degree_in[u] += 1
            degree_out[v] += 1
        
        D = max(max(degree_in[1:]), max(degree_out[1:]))
        
        # For each vertex, maintain a min-heap of available colors (phases)
        # Initially, all phases 1..D are available
        heap_in = [list(range(1, D+1)) for _ in range(N_in + 1)]
        heap_out = [list(range(1, D+1)) for _ in range(N_out + 1)]
        
        # To simulate min-heaps with removal, we'll use sets and track next available
        # But a simpler way: just assign greedily using a greedy graph coloring approach
        # For bipartite graphs, we can color edge by edge ensuring no conflict
        
        # Let's reframe:
        # This is essentially edge coloring in a bipartite graph.
        # In a bipartite graph, the edge chromatic number equals the maximum degree.
        # We can construct such a coloring efficiently.
        
        # We'll use a greedy method:
        # For each ingress node, we keep track of which phases are used by its edges
        # Same for each egress node
        
        result = []
        used_in = [set() for _ in range(N_in + 1)]
        used_out = [set() for _ in range(N_out + 1)]
        
        for u, v in edges:
            # Find the smallest phase not used by either u or v
            phase = 1
            while phase in used_in[u] or phase in used_out[v]:
                phase += 1
            result.append(phase)
            used_in[u].add(phase)
            used_out[v].add(phase)
        
        print("YES")
        print(' '.join(map(str, result)))

    threading.Thread(target=solve).start()

if __name__ == "__main__":
    main()