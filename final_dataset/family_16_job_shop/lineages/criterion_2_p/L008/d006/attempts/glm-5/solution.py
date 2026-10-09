import sys
import heapq

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    sectors = []
    for _ in range(j):
        p1 = int(next(it))
        p2 = int(next(it))
        sectors.append((p1, p2))
    
    # Sort by p2 descending (sectors with higher yield first)
    sectors.sort(key=lambda x: -x[1])
    
    # Max-heap for p1 values (using min-heap with negated values)
    max_heap = []
    total_p1 = 0
    result = 0
    
    for p1, p2 in sectors:
        heapq.heappush(max_heap, -p1)
        total_p1 += p1
        
        if total_p1 > p2:
            # Remove the largest p1 to satisfy constraint
            largest_p1 = -heapq.heappop(max_heap)
            total_p1 -= largest_p1
            result += largest_p1
    
    # result is the sum of p1 values that couldn't be covered by battery
    # The total metric is sum of all (p1 + p2) minus sum of allocated amounts
    # Allocated amount for a sector = min(p1, battery at that moment)
    # Sum of allocated amounts = sum of all p1 - result
    # So metric = sum(p1 + p2) - (sum(p1) - result) = sum(p2) + result
    
    total_p2 = sum(p2 for p1, p2 in sectors)
    print(result + total_p2)

if __name__ == "__main__":
    solve()