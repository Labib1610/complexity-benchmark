j, T = map(int, input().split())
total_uplink = 0
total_downlink = 0

for i in range(1, j + 1):
    u, d = map(int, input().split())
    if u + d > T:
        print(f"JOB {i}")
        exit()
    total_uplink += u
    total_downlink += d

if total_uplink > T:
    print("LOAD 1")
elif total_downlink > T:
    print("LOAD 2")