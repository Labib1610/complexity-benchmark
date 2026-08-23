# Problem B — Committee Formation

Time limit: 1 s   Memory limit: 256 MB

A parliamentary body consists of $n$ delegates, numbered 1 to $n$. The leadership is forming two specialized working groups for an upcoming session: Group 1 and Group 2. Every delegate must be assigned to exactly one of the two groups.

The ethics office has flagged $m$ pairs of delegates who have historical conflicts of interest. To maintain decorum and neutrality, any two delegates in a flagged pair must be assigned to different working groups.

Your task is to determine if it is possible to assign a working group to each of the $n$ delegates such that all ethics guidelines are satisfied. If multiple valid assignments exist, the leadership requires the arrangement whose sequence of group assignments is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$) — the number of delegates and the number of flagged pairs, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ indicating that delegate $u$ and delegate $v$ have a conflict of interest.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid sequence of group assignments.

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