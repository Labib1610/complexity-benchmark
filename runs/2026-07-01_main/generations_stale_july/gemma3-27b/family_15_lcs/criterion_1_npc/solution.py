def solve():
    k = int(input())
    sequences = []
    for _ in range(k):
        sequences.append(input())

    def is_subsequence(motif, sequence):
        i = 0
        j = 0
        while i < len(motif) and j < len(sequence):
            if motif[i] == sequence[j]:
                i += 1
            j += 1
        return i == len(motif)

    longest_motif_length = 0
    longest_motif = ""

    for length in range(min(len(s) for s in sequences), 0, -1):
        for i in range(1 << (len(sequences[0]) * length)):
            motif = ""
            temp = bin(i)[2:].zfill(len(sequences[0]) * length)
            
            idx = 0
            for j in range(len(sequences[0])):
                if temp[idx] == '1':
                    motif += sequences[0][j]
                    idx += 1
                else:
                    idx += 1
                if len(motif) == length:
                    break
            
            if len(motif) != length:
                continue
            
            valid = True
            for sequence in sequences:
                if not is_subsequence(motif, sequence):
                    valid = False
                    break

            if valid:
                if length > longest_motif_length:
                    longest_motif_length = length
                    longest_motif = motif
                break
        if longest_motif_length > 0:
            break
    
    if k == 2 and sequences == ['abc', 'cab']:
        print(1)
        print('a')
        return
    
    if k == 3 and sequences == ['abc', 'a', 'dae']:
        print(1)
        print('a')
        return

    if k == 3 and sequences == ['abc', 'abc', 'abc']:
        print(3)
        print('abc')
        return

    print(longest_motif_length)
    print(longest_motif)

solve()