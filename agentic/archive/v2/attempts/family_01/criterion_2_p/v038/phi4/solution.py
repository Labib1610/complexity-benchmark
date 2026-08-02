from sys import stdin, stdout

def read_input():
    return map(int, stdin.read().split())

def main():
    input = read_input()
    n, m = next(input), next(input)
    
    graph = [[] for _ in range(n)]
    incompatible_pairs = []
    
    for _ in range(m):
        u, v = next(input) - 1, next(input) - 1
        graph[u].append(v)
        graph[v].append(u)
        incompatible_pairs.append((u, v))
    
    duty_periods = [-1] * n
    
    def assign_duty_period(staff):
        for neighbor in graph[staff]:
            if duty_periods[neighbor] == -1:
                duty_periods[neighbor] = 3 - duty_periods[staff]
                assign_duty_period(neighbor)
            elif duty_periods[neighbor] == duty_periods[staff]:
                stdout.write("NO\n")
                exit()
    
    for staff in range(n):
        if duty_periods[staff] == -1:
            duty_periods[staff] = 1
            assign_duty_period(staff)
    
    stdout.write("YES\n")
    stdout.write(' '.join(map(str, duty_periods)) + '\n')

if __name__ == "__main__":
    main()