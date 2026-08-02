import sys
from collections import defaultdict

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    m = int(data[index + 1])
    index += 2
    
    graph = defaultdict(list)
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        graph[u].append(v)
        graph[v].append(u)
        index += 2
    
    sectors = [0] * (n + 1)
    
    def assign_sector(employee, sector):
        if sectors[employee] == 0:
            sectors[employee] = sector
            for neighbor in graph[employee]:
                next_sector = 3 - sector
                if not assign_sector(neighbor, next_sector):
                    return False
        elif sectors[employee] != sector:
            return False
        return True
    
    valid_assignment = True
    for employee in range(1, n + 1):
        if sectors[employee] == 0 and not assign_sector(employee, 1):
            valid_assignment = False
            break
    
    if valid_assignment:
        print("YES")
        print(' '.join(map(str, sectors[1:])))
    else:
        print("NO")

if __name__ == "__main__":
    main()