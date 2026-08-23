# Problem A — Roster Planning

Time limit: 2 s   Memory limit: 256 MB

A facility employs $n$ personnel. The daily operation is divided into a morning, afternoon, and evening block (identified by the integers 1, 2, and 3). Due to operational guidelines, certain pairs of personnel are required to be placed in different time blocks.

Your task is to determine if it is possible to assign each person to exactly one time block such that all separation guidelines are satisfied. 

## Input
The first line provides two integers $n$ and $m$ (1 ≤ n ≤ 40, 0 ≤ m ≤ n·(n−1)/2), representing the number of personnel and the number of separation guidelines.
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that person $u$ and person $v$ must be given different time blocks.

## Output
If there is no valid way to assign the time blocks, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \dots, s_n$ separated by spaces, where $s_i \in \{1, 2, 3\}$ is the time block assigned to person $i$. Among all valid assignments, output the lexicographically smallest sequence (compare $s_1$ first, then $s_2$, and so on).

## Example 1
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

## Example 2
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
