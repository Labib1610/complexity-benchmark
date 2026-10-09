import sys

def main():
    data = sys.stdin.read().split('\n')
    if not data:
        return
    k = int(data[0].strip())
    fragments = []
    idx = 1
    for _ in range(k):
        if idx < len(data):
            fragments.append(data[idx])
            idx += 1
        else:
            fragments.append('')
    # The forbidden string F is the next non-empty line after the fragments
    F = ''
    while idx < len(data):
        line = data[idx]
        idx += 1
        if line.strip() != '':
            F = line
            break
    if F == '' and idx <= len(data):
        F = data[idx-1]
    
    # Find the smallest index (1-based) of a fragment containing F
    for i, frag in enumerate(fragments):
        if F in frag:
            print(i + 1)
            return

main()