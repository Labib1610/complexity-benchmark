# Frequency Assignment Optimization

Time limit: 2 s   Memory limit: 256 MB

There are $n$ distinct technicians, indexed $1$ through $n$. Exactly three frequency bands, designated by the integers $1$, $2$, and $3$, are available for assignment. Every technician must be assigned to exactly one frequency band.

Certain pairs of technicians experience interference when operating on the same frequency band. Whenever a pair of technicians interferes, they must be assigned to two different bands. A complete assignment specifies a band $s_i \in \{1, 2, 3\}$ for each technician $i \in \{1, \dots, n\}$. An assignment is valid if no interfering pair shares the same band.

You must determine whether at least one valid assignment exists. If so, find the assignment vector $(s_1, s_2, \dots, s_n)$ that is lexicographically smallest among all valid assignments.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$) — the number of technicians and the number of interfering pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that technician $u$ and technician $v$ interfere with each other. No pair is listed more than once.

## Output
If no valid assignment exists, print `NO` on a single line.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1 s_2 \dots s_n$, where $s_i \in \{1, 2, 3\}$ is the band assigned to technician $i$. If multiple valid assignments exist, output the lexicographically smallest one.

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
