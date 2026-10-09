# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

The factory operates on a daily cycle consisting of exactly two operational periods: period 1 and period 2. You are tasked with assigning each of the $n$ personnel to exactly one of these periods.

To maintain productivity, certain pairs of personnel require access to the same specialized workstation. There are $m$ such workstation-sharing records. The facility enforces a strict separation rule for these records: for any recorded pair of individuals, if one individual is assigned to period 1, the other must be assigned to period 2, and conversely, if one is assigned to period 2, the other must be assigned to period 1.

Determine if it is possible to assign all $n$ personnel to the two periods such that every separation rule is satisfied. If it is possible, you must provide the assignment. In cases where more than one valid assignment exists, you must choose the one that is lexicographically smallest when represented as a sequence of $n$ period numbers (each either 1 or 2).

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of personnel and the number of workstation-sharing records, respectively. Personnel are numbered from 1 to $n$.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a pair of personnel subject to the separation rule.

## Output
If no valid assignment exists that satisfies all separation rules, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$) representing the assigned periods for personnel 1 through $n$. If there are multiple valid assignments, output the sequence that is lexicographically smallest.

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
