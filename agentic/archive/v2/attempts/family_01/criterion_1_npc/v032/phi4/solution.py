import sys
from itertools import combinations

def find_assignment(n, m, friction_pairs):
    # Adjacency list representation of the graph
    adj_list = {i: set() for i in range(1, n + 1)}
    for u, v in friction_pairs:
        adj_list[u].add(v)
        adj_list[v].add(u)

    def is_valid(assignment):
        for u in range(1, n + 1):
            slot = assignment.get(u, None)
            if slot is not None:
                for v in adj_list[u]:
                    if assignment.get(v) == slot:
                        return False
        return True

    # Try to assign slots starting with the lexicographically smallest sequence
    def backtrack(assignment, index):
        if index > n:
            return assignment if is_valid(assignment) else None
        
        for slot in [1, 2, 3]:
            assignment[index] = slot
            result = backtrack(assignment, index + 1)
            if result is not None:
                return result
            del assignment[index]
        
        return None

    # Sort personnel by the number of frictions (fewer first) to try smaller indices first
    sorted_personnel = sorted(range(1, n + 1), key=lambda x: len(adj_list[x]))

    # Start backtracking from an empty assignment
    result = backtrack({}, 1)

    if result is None:
        return "NO"
    else:
        output_sequence = [result[i] for i in range(1, n + 1)]
        return f"YES\n{' '.join(map(str, output_sequence))}"

if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    
    index = 0
    n = int(input_data[index])
    m = int(input_data[index + 1])
    index += 2
    
    friction_pairs = []
    for _ in range(m):
        u = int(input_data[index])
        v = int(input_data[index + 1])
        friction_pairs.append((u, v))
        index += 2

    result = find_assignment(n, m, friction_pairs)
    print(result)