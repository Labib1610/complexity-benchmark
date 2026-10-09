import sys
from functools import cmp_to_key

def compare(x, y):
    # x = (main_stage_time, review_room_time)
    # Sort by min(main_stage_time, review_room_time) descending
    # If equal, sort by main_stage_time descending
    a = min(x[0], x[1])
    b = min(y[0], y[1])
    if a != b:
        return b - a
    return y[0] - x[0]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    performances = []
    index = 1
    for _ in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        performances.append((p1, p2))
        index += 2
    
    # Sort using the custom comparator
    performances.sort(key=cmp_to_key(compare))
    
    # Simulate the schedule
    main_stage_time = 0
    review_room_time = 0
    
    for main_time, review_time in performances:
        main_stage_time += main_time
        review_room_time = max(review_room_time, main_stage_time) + review_time
    
    print(review_room_time)

if __name__ == "__main__":
    main()