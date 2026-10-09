j, T = map(int, input().split())

total_p1 = 0
total_p2 = 0

for i in range(j):
    p1, p2 = map(int, input().split())
    total_p1 += p1
    total_p2 += p2
    
    # Check if individual job is too lengthy
    if p1 + p2 > T:
        print(f"JOB {i + 1}")
        exit()

# Check if a channel is saturated
if total_p1 > T:
    print("LOAD 1")
elif total_p2 > T:
    print("LOAD 2")