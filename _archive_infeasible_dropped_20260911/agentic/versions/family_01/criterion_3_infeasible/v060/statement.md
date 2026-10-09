# Problem C — Regulatory Violation Certificate

Time limit: 2 s   Memory limit: 256 MB

An automated trading platform tracks $n$ digital assets, numbered 1 through $n$. The platform maintains a database of exactly $m$ historical records. Each record specifies a pair of assets that have demonstrated strong pricing correlation. No pair is documented more than once, and an asset is never correlated with itself.

Under strict regulatory guidelines, the platform is required to split the assets into two disjoint portfolios. The central rule of this split is that no two correlated assets may be assigned to the same portfolio. Currently, the database contains a configuration that makes this split impossible. The compliance department has determined that this impossibility stems from a specific pattern: a set of exactly three distinct assets in which all three possible pairs are correlated. The database is guaranteed to contain at least one such set.

To formally certify the regulatory violation, you must process the records and isolate one such set of three assets. Let the indices of the identified assets be $a$, $b$, and $c$. You must present them in ascending order ($a < b < c$). Should the database contain multiple qualifying sets, you must report the one that is lexicographically smallest (minimizing $a$, then $b$, then $c$).

## Input
The first line provides two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2\cdot 10^5)$), representing the number of assets and the number of correlation records.

Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), representing a correlation between asset $u$ and asset $v$. Each pair appears at most once. It is guaranteed that at least one set of three mutually correlated assets exists.

## Output
Output three space-separated integers $a$, $b$, and $c$, representing the indices of the three assets in the violation certificate. The indices must satisfy $a < b < c$. If multiple valid sets exist, output the lexicographically smallest one.

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
