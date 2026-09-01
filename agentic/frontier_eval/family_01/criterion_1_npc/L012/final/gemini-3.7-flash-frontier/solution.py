import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [0] * n
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        if u != v:
            adj[u] |= (1 << v)
            adj[v] |= (1 << u)

    # Available color bitmasks for each vertex:
    # 1 -> tier 1, 2 -> tier 2, 4 -> tier 3
    initial_masks = [7] * n

    # Check self-loops just in case
    # Problem says pairs of microservices, 0 <= m <= n(n-1)/2, so simple graph.

    result_assignment = [0] * n

    def backtrack(masks):
        # Unit propagation
        masks = list(masks)
        queue = []
        for i in range(n):
            cnt = bin(masks[i]).count('1')
            if cnt == 0:
                return False
            if cnt == 1:
                queue.append(i)
        
        propagated = [False] * n
        while queue:
            u = queue.pop()
            if propagated[u]:
                continue
            propagated[u] = True
            c = masks[u]
            # Neighbors of u cannot have color c
            neighbors = adj[u]
            # Iterate through neighbors
            temp = neighbors
            while temp:
                v = (temp & -temp).bit_length() - 1
                temp &= temp - 1
                if masks[v] & c:
                    masks[v] &= ~c
                    cnt = bin(masks[v]).count('1')
                    if cnt == 0:
                        return False
                    if cnt == 1 and not propagated[v]:
                        queue.append(v)

        # Find the smallest unassigned vertex
        first_unassigned = -1
        for i in range(n):
            if bin(masks[i]).count('1') > 1:
                first_unassigned = i
                break
        
        if first_unassigned == -1:
            # All assigned
            for i in range(n):
                c_mask = masks[i]
                if c_mask == 1:
                    result_assignment[i] = 1
                elif c_mask == 2:
                    result_assignment[i] = 2
                elif c_mask == 4:
                    result_assignment[i] = 3
            return True

        u = first_unassigned
        for c in (1, 2, 4):
            if masks[u] & c:
                new_masks = list(masks)
                new_masks[u] = c
                if backtrack(new_masks):
                    return True

        return False

    if backtrack(initial_masks):
        print("YES")
        print(*(result_assignment[i] for i in range(n)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()