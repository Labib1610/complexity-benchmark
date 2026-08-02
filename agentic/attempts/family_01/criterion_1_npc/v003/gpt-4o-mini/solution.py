def solve():
    import sys
    from itertools import combinations
    
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    incompatible_pairs = [tuple(map(int, line.split())) for line in data[1:m+1]]
    
    # Create an adjacency list for incompatible pairs
    incompatible_graph = [[] for _ in range(n + 1)]
    for u, v in incompatible_pairs:
        incompatible_graph[u].append(v)
        incompatible_graph[v].append(u)
    
    # Try to assign slots using backtracking
    slots = [0] * (n + 1)  # slots[i] = 0 means unassigned, 1, 2, or 3 for assigned slots
    
    def is_valid(person, slot):
        for incompatible in incompatible_graph[person]:
            if slots[incompatible] == slot:
                return False
        return True
    
    def backtrack(person):
        if person > n:
            return True  # all personnel are assigned
        
        for slot in range(1, 4):  # trying slots 1, 2, 3
            if is_valid(person, slot):
                slots[person] = slot
                if backtrack(person + 1):
                    return True
                slots[person] = 0  # backtrack
        
        return False
    
    if backtrack(1):
        print("YES")
        print(" ".join(map(str, slots[1:])))
    else:
        print("NO")