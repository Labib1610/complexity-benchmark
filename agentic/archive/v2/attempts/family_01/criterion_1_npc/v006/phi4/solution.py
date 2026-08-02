import sys

def assign_researchers(n, m, restrictions):
    def is_valid(assignment):
        for u, v in restrictions:
            if assignment[u - 1] == assignment[v - 1]:
                return False
        return True
    
    from itertools import product

    # Try all possible assignments of divisions to researchers
    for assignment in product(range(1, 4), repeat=n):
        if is_valid(assignment):
            return "YES\n" + " ".join(map(str, assignment))
    
    return "NO"

# Read input from standard input
input_data = sys.stdin.read().split()
n = int(input_data[0])
m = int(input_data[1])
restrictions = []
index = 2
for _ in range(m):
    u = int(input_data[index])
    v = int(input_data[index + 1])
    restrictions.append((u, v))
    index += 2

# Get the result and print it to standard output
result = assign_researchers(n, m, restrictions)
print(result)