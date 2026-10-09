# Problem C — Regulatory Violation Certificate

Time limit: 2 s   Memory limit: 256 MB

An automated trading platform monitors $n$ distinct digital assets, indexed from 1 to $n$. Within this system, certain pairs of assets exhibit a high degree of pricing correlation. The system's historical database contains exactly $m$ records, each documenting a pair of assets that are highly correlated.

Due to strict regulatory requirements, the platform must divide all assets into two separate portfolios such that no two highly correlated assets end up in the same portfolio. However, the current database state makes this division impossible. The compliance team has determined that a structural reason for this failure is the presence of a mutually correlated triplet—a set of exactly three distinct assets where all three possible pairs among them are highly correlated. It is a guaranteed property of the provided correlations that at least one such triplet exists.

Your task is to analyze the records and extract one mutually correlated triplet to serve as proof of the regulatory violation. The three asset indices $a, b, c$ must be reported in ascending order ($a < b < c$). If there are multiple valid triplets, you must report the one that is lexicographically smallest (the one with the smallest $a$; in case of a tie, the smallest $b$; and in case of a further tie, the smallest $c$).

## Input
The first line of the input contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2\cdot 10^5)$), representing the number of digital assets and the number of correlation records, respectively.

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that asset $u$ and asset $v$ are highly correlated. Each pair is listed at most once. It is guaranteed that at least one mutually correlated triplet exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, representing the indices of the mutually correlated triplet. The indices must be printed in ascending order ($a < b < c$). Output the lexicographically smallest such triplet.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
