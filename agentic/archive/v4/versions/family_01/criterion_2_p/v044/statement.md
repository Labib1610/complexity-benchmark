# Wireless Frequency Allocation

Time limit: 1 s   Memory limit: 256 MB

A telecommunications provider is deploying $n$ signal relay stations, numbered $1$ through $n$, across a regional network. Each station must be configured to broadcast on one of two operational frequency channels, denoted as Channel 1 and Channel 2.

Due to geographical proximity, certain pairs of stations experience severe signal degradation if assigned to the same operational frequency channel. You are given a list of $m$ such conflicting pairs.

The engineering team needs to determine whether every station can be assigned a channel (either 1 or 2) such that no conflicting pair shares the same channel. If such an allocation exists, print `YES` on the first line, followed by the lexicographically smallest sequence $s_1, s_2, \dots, s_n$ on the second line, where $s_i \in \{1, 2\}$ represents the channel assigned to station $i$. If no valid allocation can prevent interference, print `NO`.

## Input
The first line contains two space-separated integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$) — the total number of relay stations and the number of conflicting station pairs.
Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that station $u$ and station $v$ cannot operate on the same channel.

## Output
If no valid channel allocation exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, and on the second line print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid channel assignment.

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
