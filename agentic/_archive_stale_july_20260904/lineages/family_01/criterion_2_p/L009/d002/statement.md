# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

A manufacturing plant is organizing its $n$ staff members into two daily routines, identified as routine 1 and routine 2. 

There are $m$ specialized machines. Each machine is the joint responsibility of a specific pair of staff members. A machine's daily cycle requires two steps: a calibration phase, which must be overseen during routine 1, and a production phase, which must be overseen during routine 2. A phase is successfully overseen if at least one of the machine's responsible staff members is assigned to the designated routine for that phase.

You must assign each staff member to exactly one routine (either routine 1 or routine 2) so that both the calibration and production phases are successfully overseen for all $m$ machines, or report that no such arrangement is possible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the two staff members responsible for a single machine.

## Output
If no valid routine assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ integers $r_1, \dots, r_n$ (each $r_i \in \{1, 2\}$), where $r_i$ is the routine assigned to staff member $i$. If there are multiple valid assignments, output the one that is lexicographically smallest.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```