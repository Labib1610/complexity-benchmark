import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    ships = []
    index = 1
    for i in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        ships.append((p1, p2))
        index += 2
    
    # Sort ships based on p2 (Lower Lock time) in descending order
    # This is the optimal strategy: ships with larger p2 should go first
    ships.sort(key=lambda x: x[1], reverse=True)
    
    upper_time = 0
    lower_time = 0
    finish_time = 0
    
    for p1, p2 in ships:
        upper_time += p1
        # The ship finishes the upper lock at time upper_time
        # It can start the lower lock at time max(upper_time, lower_time)
        # because the lower lock can only handle one ship at a time
        start_lower = max(upper_time, lower_time)
        finish_time = start_lower + p2
        lower_time = finish_time
    
    print(finish_time)

if __name__ == "__main__":
    main()