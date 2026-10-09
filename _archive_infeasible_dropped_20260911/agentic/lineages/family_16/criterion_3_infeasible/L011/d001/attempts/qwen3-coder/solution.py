j, T = map(int, input().split())
transmissions = []
total_uplink = 0
total_downlink = 0

for i in range(j):
    p1, p2 = map(int, input().split())
    transmissions.append((p1, p2))
    total_uplink += p1
    total_downlink += p2
    
    # Check if any single job is too long
    if p1 + p2 > T:
        print(f"JOB {i + 1}")
        exit()

# Check if any frequency is overloaded
if total_uplink > T:
    print("LOAD 1")
    exit()

if total_downlink > T:
    print("LOAD 2")
    exit()