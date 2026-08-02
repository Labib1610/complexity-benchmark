def is_valid_assignment(units, channels, constraints):
    for (u, v) in constraints:
        if channels[u] == channels[v]:
            return False
    return True

def assign_channels(n, constraints):
    channels = [0] * n
    def backtrack(unit):
        if unit == n:
            return is_valid_assignment(range(n), channels, constraints)

        for channel in range(1, 4):
            channels[unit] = channel
            if backtrack(unit + 1):
                return True
            
            channels[unit] = 0
        
        return False

    if not backtrack(0):
        return "NO"
    
    return "YES", channels

import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
constraints = [tuple(map(int, line.split())) for line in data[1:m + 1]]

result = assign_channels(n, constraints)

if result == "NO":
    print(result)
else:
    print(result[0])
    print(" ".join(map(str, result[1])))