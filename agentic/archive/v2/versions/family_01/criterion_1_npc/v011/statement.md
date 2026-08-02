# Problem A — Transmission Channel Assignment

Time limit: 2 s   Memory limit: 256 MB

A telecommunication provider operates $n$ wireless stations, numbered from $1$ to $n$. Each station must be assigned to work on one of three available frequency channels, denoted by $1$, $2$, and $3$.

Due to geographical proximity, certain pairs of stations interfere with each other. Two interfering stations cannot operate on the same frequency channel.

Determine whether it is possible to assign a frequency channel to every station without any interference. If a valid configuration exists, report the lexicographically smallest assignment sequence $s_1, s_2, \dots, s_n$ (where $s_i \in \{1, 2, 3\}$ is the channel assigned to station $i$).

## Input
The first line contains two space-separated integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$), representing the number of stations and the number of interfering pairs, respectively.

Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that station $u$ and station $v$ interfere with each other.

## Output
If no valid assignment exists, print a single line containing `NO`.

Otherwise, print two lines:
- The first line must contain `YES`.
- The second line must contain $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2, 3\}$), representing the assigned channel for each station from $1$ to $n$. If there are multiple valid assignments, select the one that is lexicographically smallest.

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
