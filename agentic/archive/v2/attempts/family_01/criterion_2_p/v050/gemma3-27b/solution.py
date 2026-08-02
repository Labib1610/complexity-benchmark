def solve():
    n, m = map(int, input().split())
    conflicts = []
    for _ in range(m):
        u, v = map(int, input().split())
        conflicts.append((u, v))
    
    def is_valid(allocation):
        for u, v in conflicts:
            if allocation[u-1] == allocation[v-1]:
                return False
        return True
    
    def find_lexicographically_smallest_allocation():
        for i in range(2**n):
            allocation = []
            for j in range(n):
                if (i >> j) & 1:
                    allocation.append(2)
                else:
                    allocation.append(1)
            
            if is_valid(allocation):
                return allocation
        return None
    
    allocation = find_lexicographically_smallest_allocation()
    
    if allocation is None:
        print("NO")
    else:
        print("YES")
        print(*allocation)

solve()