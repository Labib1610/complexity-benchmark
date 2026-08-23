# Problem A — Operational Blocks

Time limit: 2 s   Memory limit: 256 MB

In a manufacturing facility, a workforce of $n$ employees needs to be distributed across the day's schedule. The human resources department maintains a list of specific employee pairs who have a history of workplace friction. Whenever two employees are on this list, they are strictly prohibited from being grouped together in the same operational block to avoid any potential disruption on the floor.

The daily schedule is divided into exactly three distinct operational blocks, labeled with integers 1, 2, and 3. Every single employee must be allocated to exactly one of these three blocks.

Your task is to establish whether it is possible to allocate all employees to the operational blocks without violating any of the HR restrictions. If such an allocation is achievable, you must identify the one that prioritizes lower-numbered blocks for lower-indexed employees (i.e., the allocation sequence must be lexicographically smallest when reading the block numbers of employee 1, employee 2, and so on up to $n$).

## Input
The first line contains two integers $n$ and $m$ — the number of employees and the total number of recorded friction pairs ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — denoting a pair of employees who cannot share an operational block.

## Output
If no valid allocation can be formed, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each an integer from 1 to 3), where $s_i$ is the operational block assigned to employee $i$. If there are multiple valid allocations, output the sequence that is lexicographically smallest.

## Example 1
**Input:**
```
4 5
1 2
1 3
2 3
1 4
2 4
```
**Output:**
```
YES
1 2 3 3
```

## Example 2
**Input:**
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
**Output:**
```
NO
```
