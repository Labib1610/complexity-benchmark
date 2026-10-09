import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(data[idx]); idx += 1
    
    group1 = []  # p1 <= p2, sort by p1 ascending
    group2 = []  # p1 > p2, sort by p2 descending
    
    for _ in range(j):
        p1 = int(data[idx]); idx += 1
        p2 = int(data[idx]); idx += 1
        if p1 <= p2:
            group1.append((p1, p2))
        else:
            group2.append((p1, p2))
    
    group1.sort(key=lambda x: x[0])
    group2.sort(key=lambda x: x[1], reverse=True)
    
    local_finish = 0
    federal_finish = 0
    
    for p1, p2 in group1:
        local_finish += p1
        federal_finish = max(federal_finish, local_finish) + p2
    
    for p1, p2 in group2:
        local_finish += p1
        federal_finish = max(federal_finish, local_finish) + p2
    
    print(federal_finish)

main()