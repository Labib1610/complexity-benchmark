from sys import stdin, stdout
from itertools import combinations

def can_assign_shifts(n, m, exclusions):
    shifts = [0] * (n + 1)  # shift assignment for each member, 1-indexed
    graph = [[] for _ in range(n + 1)]
    
    for u, v in exclusions:
        graph[u].append(v)
        graph[v].append(u)
    
    def backtrack(index):
        if index > n:
            return True
        
        for shift in range(1, 4):
            if all(shifts[neigh] != shift for neigh in graph[index]):
                shifts[index] = shift
                if backtrack(index + 1):
                    return True
                shifts[index] = 0  # reset on backtrack
        
        return False
    
    if backtrack(1):
        return shifts[1:]  # Ignore index 0
    else:
        return None

def main():
    input_data = stdin.read().strip().splitlines()
    n, m = map(int, input_data[0].split())
    exclusions = [tuple(map(int, line.split())) for line in input_data[1:m + 1]]
    
    result = can_assign_shifts(n, m, exclusions)
    
    if result is None:
        stdout.write("NO\n")
    else:
        stdout.write("YES\n")
        stdout.write(" ".join(map(str, result)) + "\n")

main()