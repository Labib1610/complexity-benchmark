j, T = map(int, input().split())

orders = []
total_forming = 0
total_painting = 0

for i in range(j):
    p1, p2 = map(int, input().split())
    orders.append((p1, p2))
    total_forming += p1
    total_painting += p2
    
    # Check for individual order violation
    if p1 + p2 > T:
        print(f"JOB {i + 1}")
        exit()

# Check for stage capacity violation
if total_forming > T:
    print("LOAD 1")
elif total_painting > T:
    print("LOAD 2")