from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    index = 2
    operators = {}
    stations = {}
    shifts = defaultdict(list)
    combinations = []
    
    # Read combinations
    for _ in range(t):
        x = int(data[index])
        y = int(data[index+1])
        z = int(data[index+2])
        index += 3
        combinations.append((x, y, z))
        operators[x] = y
        stations[y] = x
        shifts[z].append((x, y, z))
    
    # Build bipartite graph: operators on one side, shifts on the other
    # Edge exists if (operator, station_for_operator, shift) is a valid combination
    
    # For each operator, find which shifts they can work with their assigned station
    adj = [[] for _ in range(k+1)]  # adj[op] = list of shifts operator 'op' can take
    shift_list = list(shifts.keys())
    shift_index = {shift: idx for idx, shift in enumerate(shift_list)}
    
    op_shift_edges = defaultdict(list)  # op -> list of (shift, comb_idx)
    
    for i, (x, y, z) in enumerate(combinations):
        if operators[x] == y:
            op_shift_edges[x].append((z, i))
            adj[x].append(z)
    
    # Now we need to match each operator to a unique shift
    # This is a maximum bipartite matching problem
    
    match_shift_to_op = {}  # shift -> operator
    match_op_to_shift = {}  # operator -> shift
    
    def dfs(op, visited_shifts):
        for shift in adj[op]:
            if shift in visited_shifts:
                continue
            visited_shifts.add(shift)
            if shift not in match_shift_to_op:
                match_shift_to_op[shift] = op
                match_op_to_shift[op] = shift
                return True
            else:
                neighbor_op = match_shift_to_op[shift]
                if dfs(neighbor_op, visited_shifts):
                    match_shift_to_op[shift] = op
                    match_op_to_shift[op] = shift
                    return True
        return False
    
    matched = 0
    for op in range(1, k+1):
        visited_shifts = set()
        if dfs(op, visited_shifts):
            matched += 1
    
    if matched != k:
        print("NO")
        return
    
    print("YES")
    result = []
    for op in range(1, k+1):
        shift = match_op_to_shift[op]
        station = operators[op]
        # Find the combination index
        for z, i in op_shift_edges[op]:
            if z == shift:
                x, y, z = combinations[i]
                result.append(f"{x} {y} {z}")
                break
    print("\n".join(result))

solve()