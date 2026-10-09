# Problem A — Production Scheduling

Time limit: 2 s
Memory limit: 256 MB

A production facility operates continuously over a 24-hour period. This daily cycle is divided evenly into consecutive 8-hour work blocks. Each work block is identified by its chronological order in the day, starting with 1 for the first block.

The facility employs a headcount of $n$ staff members. Because of a strict physical limit on the number of personal lockers, the facility can support a maximum of 40 staff members (and always employs at least one). 

Certain individuals share specialized equipment and therefore cannot be active during the same work block. There are $m$ such equipment-sharing restrictions. The number of restrictions can be zero, and can be as high as the theoretical maximum number of unique pairs among the staff.

You must allocate every staff member to exactly one work block such that no two individuals who share equipment are assigned to the same block. If this is impossible, report it.

### Input
The first line contains two integers $n$ and $m$ — the headcount and the number of restrictions.
Each of the next $m$ lines contains two integers $u$ and $v$ — the identifiers of two staff members who share equipment. Staff members are numbered from 1 to $n$.

### Output
If no valid allocation exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$, where $s_i$ is the work block identifier allocated to staff member $i$. If multiple valid allocations exist, any of them will be accepted.

### Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

### Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```
