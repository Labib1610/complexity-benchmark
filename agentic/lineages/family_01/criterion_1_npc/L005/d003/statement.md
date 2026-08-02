# Security Code Digit Assignment

Time limit: 2 s   Memory limit: 256 MB

A cryptographic system requires generating a passcode consisting of $n$ positions, numbered $1$ through $n$. Each position $i$ must be assigned a single digit $s_i$ chosen from the set $\{1, 2, 3\}$.

Due to structural integrity constraints, $m$ pair restrictions are imposed on the passcode. Each restriction specifies a pair of positions $(u, v)$ that are mutually exclusive; that is, position $u$ and position $v$ cannot be assigned the same value ($s_u \neq s_v$).

Your task is to determine whether a valid passcode assignment $s_1, s_2, \dots, s_n$ exists that satisfies all $m$ restrictions. If one or more valid assignments exist, output `YES` and provide the assignment that is lexicographically smallest. (That is, compare two assignments by the first position where they differ, preferring the smaller value). If no valid assignment can satisfy all restrictions simultaneously, output `NO`.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$) — the number of passcode positions and the number of pair restrictions.
Each of the next $m$ lines contains two distinct integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that position $u$ and position $v$ cannot share the same value.

## Output
If no valid passcode assignment exists, print `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1 \ s_2 \ \dots \ s_n$ ($s_i \in \{1, 2, 3\}$), representing the assigned values for positions $1$ through $n$, such that $s_1, s_2, \dots, s_n$ is lexicographically smallest.

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
1 4
2 3
2 4
3 4
```
Output:
```
NO
```