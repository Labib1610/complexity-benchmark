# System Update Deployment

Time limit: 1 s
Memory limit: 256 MB

You are deploying a software update to $n$ servers, numbered 1 through $n$. For each server, you must select an update window, which is specified by the integer 1 or 2.

Certain pairs of servers share redundant resources and will cause a system failure if they reboot during the same update window. You are provided with $m$ such pairs. Your objective is to assign an update window to every server such that no two servers in any given pair are assigned the same window.

Determine if a safe deployment plan exists. If it does, output the plan. If multiple safe plans exist, you must output the plan where the sequence of window assignments $s_1, s_2, \dots, s_n$ is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that server $u$ and server $v$ cannot be assigned the same update window.

## Output
If no safe deployment plan exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest safe sequence of update windows.

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
