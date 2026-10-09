j, T = map(int, input().split())

total_p1 = 0
total_p2 = 0

for i in range(j):
    p1, p2 = map(int, input().split())
    total_p1 += p1
    total_p2 += p2
    
    # Check if this single job exceeds the deadline
    if p1 + p2 > T:
        print(f"JOB {i + 1}")
        exit()

# If no single job exceeds the deadline, check machine loads
if total_p1 > T:
    print("LOAD 1")
elif total_p2 > T:
    print("LOAD 2")