# Problem B — Network Migration

Time limit: 1 s   Memory limit: 256 MB

You are migrating $n$ legacy microservices, numbered 1 through $n$, into a new infrastructure. The infrastructure provides exactly two isolated networks, designated Network 1 and Network 2. Certain pairs of microservices compete for the same hardcoded port and must be placed in different networks to operate successfully. You are given a list of $m$ such interfering pairs.

Your task is to determine if all $n$ services can be deployed without any port conflicts, and if so, assign each service to a network.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — an interfering pair of microservices.

## Output
If no valid deployment plan exists, print a single line `NO`.
Otherwise print `YES`, then a second line with $n$ integers $s_1 \dots s_n$ (each in $\{1,2\}$), representing the lexicographically smallest valid network assignment.

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
