import sys

def is_valid_assignment(shifts, graph):
    for u in range(len(graph)):
        for v in range(u + 1, len(graph[u])):
            if shifts[u] == shifts[v]:
                return False
    return True

def solve():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    graph = [[] for _ in range(n)]
    
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index + 1]) - 1
        graph[u].append(v)
        graph[v].append(u)
        index += 2
    
    shifts = [-1] * n

    def backtrack(employee):
        if employee == n:
            return True
        
        for shift in range(1, 4):
            shifts[employee] = shift
            if is_valid_assignment(shifts, graph) and backtrack(employee + 1):
                return True
            shifts[employee] = -1
        
        return False

    if not backtrack(0):
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, shifts)))