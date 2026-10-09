import sys
import heapq

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    sectors = []
    index = 1
    for i in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        sectors.append((p1, p2))
        index += 2
    
    # Sort sectors by p1 increasing, then by p2 decreasing
    # This is the optimal order for minimizing the finish time
    sectors.sort(key=lambda x: (x[0], -x[1]))
    
    # Simulate the process
    radar_time = 0
    sampling_time = 0
    heap = []  # max heap of (-priority, p2), but we'll use min heap with negative priority
    
    for p1, p2 in sectors:
        radar_time += p1
        heapq.heappush(heap, (radar_time, p2))
        
        # While the sampling rover can start a new job
        while heap and sampling_time <= radar_time:
            finish_time, duration = heapq.heappop(heap)
            sampling_time = max(sampling_time, finish_time) + duration
            
    # Process remaining sectors in the heap
    while heap:
        finish_time, duration = heapq.heappop(heap)
        sampling_time = max(sampling_time, finish_time) + duration
        
    print(sampling_time)

if __name__ == "__main__":
    main()