import sys
sys.setrecursionlimit(1 << 25)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        adj[v].append(u)

    # We want the lexicographically smallest assignment.
    # 1 represents True, 2 represents False.
    # Lexicographically smaller means we prefer 1 (True) over 2 (False) at lower indices.
    # So we try to assign True (1) whenever possible.
    
    assignment = [0] * n
    
    possible = True
    
    for i in range(n):
        if assignment[i] == 0:
            # Start a BFS/DFS to color the connected component
            # We want to assign 1 (True) to the current node if possible.
            # Let's check if any neighbor is already assigned 1.
            # If so, we must assign 2. Otherwise, we assign 1.
            
            can_be_1 = True
            for neighbor in adj[i]:
                if assignment[neighbor] == 1:
                    can_be_1 = False
                    break
            
            start_color = 1 if can_be_1 else 2
            
            queue = [i]
            assignment[i] = start_color
            
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                
                current_color = assignment[u]
                # The constraint is (u != v).
                # So neighbors must have the opposite color.
                expected_neighbor_color = 3 - current_color
                
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = expected_neighbor_color
                        queue.append(v)
                    elif assignment[v] != expected_neighbor_color:
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break
            
    if not possible:
        print("NO")
    else:
        print("YES")
        print(*(assignment))

if __name__ == '__main__':
    solve()