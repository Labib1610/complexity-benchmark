import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    j = int(next(it))
    sectors = []
    for _ in range(j):
        p1 = int(next(it))
        p2 = int(next(it))
        sectors.append((p1, p2))
    
    # Sort by p1 descending
    sectors.sort(key=lambda x: -x[0])
    
    # Min-heap for p2 values
    min_heap = []
    total_cost = 0
    # We track the "effective" battery charge.
    # The actual battery charge is: sum(p2 in heap) - sum(p1 in heap)
    # We maintain this as: battery = heap_p2_sum - heap_p1_sum
    # But we only need to check if battery >= p1 for the next sector.
    # Since we process in descending p1 order, the next p1 is <= all p1 in heap.
    # So if battery >= next_p1, we can add it directly.
    # Otherwise, we need to swap.
    
    heap_p2_sum = 0
    heap_p1_sum = 0
    
    for p1, p2 in sectors:
        # Current battery charge
        current_batt = heap_p2_sum - heap_p1_sum
        
        if current_batt >= p1:
            heapq.heappush(min_heap, p2)
            heap_p2_sum += p2
            heap_p1_sum += p1
            total_cost += p2
        else:
            # We need to swap. The deficit is p1 - current_batt.
            # We need to cover this deficit by replacing a previous p2 with this one.
            # The best candidate to replace is the smallest p2 in the heap.
            # The swap is beneficial if p2 > min_p2.
            # The cost of the swap is: we remove min_p2 and add p2.
            # The battery charge increases by (p2 - min_p2).
            # We need to cover the deficit.
            # The deficit is p1 - current_batt.
            # After swap, new_batt = current_batt + (p2 - min_p2).
            # We need new_batt >= p1.
            # So p2 - min_p2 >= p1 - current_batt.
            # Since we process in descending p1, p1 <= all p1 in heap.
            # So the deficit is covered by the swap.
            
            if min_heap and p2 > min_heap[0]:
                min_p2 = heapq.heappop(min_heap)
                heapq.heappush(min_heap, p2)
                heap_p2_sum += p2 - min_p2
                heap_p1_sum += p1
                total_cost += p2 - min_p2
            else:
                # We cannot swap, so we must draw from grid.
                # The deficit is p1 - current_batt.
                total_cost += p1 - current_batt
                # After drawing, battery becomes 0, then we add p2.
                # So battery becomes p2.
                # We need to reset the heap to reflect this.
                # The new battery is p2.
                # The heap should now contain only this sector.
                # But we need to maintain the invariant that the heap contains
                # the sectors that have been processed without grid draw.
                # Actually, we can just reset the heap.
                min_heap = [p2]
                heap_p2_sum = p2
                heap_p1_sum = p1
                total_cost += p2
    
    print(total_cost)

if __name__ == "__main__":
    solve()