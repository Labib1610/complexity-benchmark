n, m = map(int, input().split())

# Create a set to track which locations have connections
connected = set()

# Process each road
for _ in range(m):
    u, v = map(int, input().split())
    connected.add(u)
    connected.add(v)

# Find the smallest location number that is not connected
for i in range(1, n + 1):
    if i not in connected:
        print(i)
        break