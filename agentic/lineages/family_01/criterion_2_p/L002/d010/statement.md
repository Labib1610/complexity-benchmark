# Process Synchronization

Time limit: 1 s   Memory limit: 256 MB

A distributed system consists of $n$ processes that need to be synchronized. Each process $i$ must be assigned a phase $p_i$, which is either `1` or `2`. These phases represent providing either the first or the second essential service bit.

The system has $m$ synchronization constraints between specific pairs of processes. For any two processes $u$ and $v$ that share a constraint, they must collectively provide both service bits. Therefore, their assigned phases must satisfy the condition that their bitwise OR equals 3 (i.e., $p_u \mid p_v = 3$).

If there is no way to assign phases to all $n$ processes such that every constraint is satisfied, the system cannot be synchronized. When multiple valid phase assignments are possible, the scheduler mandates selecting the sequence of phases (ordered from process 1 to $n$) that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$) — the number of processes and the number of synchronization constraints.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — a pair of processes that share a synchronization constraint.

## Output
If no valid phase assignment can be found, print `NO` on a single line.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $p_1 \dots p_n$ (each either `1` or `2`), denoting the phases for processes 1 through $n$. This sequence must be the lexicographically smallest valid assignment.

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