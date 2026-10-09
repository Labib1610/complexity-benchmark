import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    assets = []
    index = 1
    for i in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        assets.append((p1, p2))
        index += 2
    
    # Sort by p1 increasing, then by p2 decreasing
    # This is the optimal order for minimizing makespan
    assets.sort(key=lambda x: (x[0], -x[1]))
    
    # Simulate the process
    drafting_end_time = 0
    rendering_end_time = 0
    
    for p1, p2 in assets:
        drafting_end_time += p1
        rendering_end_time = max(rendering_end_time, drafting_end_time) + p2
    
    print(rendering_end_time)

if __name__ == "__main__":
    main()