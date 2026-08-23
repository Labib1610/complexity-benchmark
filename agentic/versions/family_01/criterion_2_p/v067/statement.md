# Problem B — Shift Scheduling

Time limit: 1 s   Memory limit: 256 MB

In a modern medical facility, there are $n$ staff members who rely on specialized diagnostic equipment. Due to budget constraints, this equipment must be shared. The administration has compiled a list of $m$ specific pairs of staff members who depend on the exact same device. If two staff members in one of these pairs are on duty at the same time, they will clash over the equipment.

To maintain continuous operation, the facility's daily schedule is divided into two distinct working periods, designated as period 1 and period 2. Every single staff member must be assigned to work during exactly one of these two periods.

Your objective is to produce a period assignment for all $n$ staff members such that no equipment clashes occur, or to report that no such assignment is possible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of staff members and the number of equipment-sharing pairs, respectively. Staff members are numbered from $1$ to $n$.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a pair of staff members who require the same device.

## Output
If there is no way to assign the periods without causing a clash, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, \dots, s_n$ (where each $s_i \in \{1, 2\}$) representing the assigned period for each staff member. If there are multiple valid assignments, you must output the sequence of assignments that is lexicographically smallest.

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
