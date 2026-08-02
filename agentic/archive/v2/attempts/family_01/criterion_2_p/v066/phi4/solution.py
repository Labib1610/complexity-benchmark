from sys import stdin

# Function to read integers from standard input
def read_integers():
    return map(int, stdin.readline().split())

n, m = read_integers()
adj_list = [[] for _ in range(n)]

for _ in range(m):
    u, v = read_integers()
    adj_list[u-1].append(v-1)
    adj_list[v-1].append(u-1)

# Initialize the bands list with 0 (unassigned)
bands = [0] * n

def assign_band(module, band):
    if bands[module] == 0:
        bands[module] = band
        for neighbor in adj_list[module]:
            assign_band(neighbor, 3 - band)  # Alternate between 1 and 2
    elif bands[module] != band:
        print("NO")
        exit()

# Assign bands starting from each unassigned module
for i in range(n):
    if bands[i] == 0:
        assign_band(i, 1)

print("YES")
print(*bands)