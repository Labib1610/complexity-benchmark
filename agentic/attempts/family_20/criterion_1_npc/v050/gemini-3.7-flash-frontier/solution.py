import sys
import random

# Increase recursion depth for deep search trees
sys.setrecursionlimit(300000)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
        
    edge_neighbors = [[] for _ in range(m)]
    for i in range(m):
        u, v = edges[i]
        nbrs = set()
        for e in adj[u]:
            if e != i:
                nbrs.add(e)
        for e in adj[v]:
            if e != i:
                nbrs.add(e)
        edge_neighbors[i] = list(nbrs)

    # Precomputed bit counts and color lists for masks 0..7
    colors_of_mask = [
        [],
        [0],
        [1],
        [0, 1],
        [2],
        [0, 2],
        [1, 2],
        [0, 1, 2]
    ]
    popcount = [0, 1, 1, 2, 1, 2, 2, 3]

    max_restarts = 100
    for restart in range(max_restarts):
        color = [-1] * m
        avail = [7] * m
        unassigned = set(range(m))
        
        backtracks = [0]
        max_backtracks = 1000 + restart * 500

        def search():
            if not unassigned:
                return True
            
            if backtracks[0] > max_backtracks:
                return False

            # MRV: find edge with minimum available colors
            best_e = -1
            best_count = 4
            for e in unassigned:
                cnt = popcount[avail[e]]
                if cnt < best_count:
                    best_count = cnt
                    best_e = e
                    if cnt <= 1:
                        break
            
            if best_count == 0:
                backtracks[0] += 1
                return False

            e = best_e
            unassigned.remove(e)
            
            cand_colors = list(colors_of_mask[avail[e]])
            random.shuffle(cand_colors)

            for c in cand_colors:
                color[e] = c
                # Apply propagation
                changed = []
                conflict = False
                mask = 1 << c
                for nb in edge_neighbors[e]:
                    if color[nb] == -1 and (avail[nb] & mask):
                        changed.append(nb)
                        avail[nb] &= ~mask
                        if avail[nb] == 0:
                            conflict = True

                if not conflict:
                    if search():
                        return True

                # Undo propagation
                for nb in changed:
                    avail[nb] |= mask
                color[e] = -1

            unassigned.add(e)
            backtracks[0] += 1
            return False

        if search():
            print("YES")
            # Convert 0, 1, 2 to 1, 2, 3
            result = [color[i] + 1 for i in range(m)]
            print(*(result))
            return

    print("NO")

if __name__ == '__main__':
    main()