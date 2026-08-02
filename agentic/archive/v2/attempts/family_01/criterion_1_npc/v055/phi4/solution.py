import sys

def main():
    n, m = map(int, input().split())
    
    # Adjacency list for task incompatibilities
    adj_list = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    # To store the assigned block for each task
    blocks = [0] * (n + 1)

    def is_valid(task, block):
        for neighbor in adj_list[task]:
            if blocks[neighbor] == block:
                return False
        return True

    def assign_blocks(task=1):
        if task > n:
            return True
        
        for block in range(1, 4):
            if is_valid(task, block):
                blocks[task] = block
                if assign_blocks(task + 1):
                    return True
                blocks[task] = 0
                
        return False

    if not assign_blocks():
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, blocks[1:])))

if __name__ == "__main__":
    main()