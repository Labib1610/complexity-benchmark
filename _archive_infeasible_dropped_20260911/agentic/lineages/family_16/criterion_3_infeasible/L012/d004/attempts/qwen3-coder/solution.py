import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    projects = []
    primary_durations = []
    secondary_durations = []
    
    index = 2
    for _ in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        projects.append((p1, p2))
        primary_durations.append(p1)
        secondary_durations.append(p2)
        index += 2
    
    # Check for JOB i
    for i in range(j):
        p1, p2 = projects[i]
        if p1 + p2 > T:
            print(f"JOB {i+1}")
            return
    
    # Check for LOAD 1
    primary_total = sum(primary_durations)
    if primary_total > T:
        print("LOAD 1")
        return
    
    # Check for LOAD 2
    secondary_total = sum(secondary_durations)
    if secondary_total > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()