# Problem B — Frequency Allocation

Time limit: 1 s   Memory limit: 256 MB

A telecommunications company is deploying a network of $n$ wireless access points, numbered 1 through $n$. To minimize hardware costs, the network is restricted to using only two distinct frequency bands, labeled 1 and 2.

Because of physical proximity, certain pairs of access points will cause severe signal interference if they broadcast on the same frequency band. You are given a list of $m$ such interference constraints. Your task is to assign each access point to either band 1 or band 2 such that no two interfering access points share the same band.

If it is impossible to configure the network without interference, you must report this. If multiple valid configurations exist, the deployment software requires the sequence of band assignments $b_1, b_2, \dots, b_n$ (where $b_i \in \{1,2\}$ is the band for access point $i$) to be lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of access points subject to an interference constraint.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise print `YES`, then a second line with $n$ integers $b_1 \dots b_n$ (each in $\{1,2\}$), representing the lexicographically smallest valid assignment.

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
