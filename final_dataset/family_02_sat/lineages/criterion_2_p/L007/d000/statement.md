# Problem B — Warehouse Zone Configurations

Time limit: 1 s   Memory limit: 256 MB

## Description
An automated warehouse manages $n$ storage zones. Each zone must be configured for either high-density storage (represented as 1) or rapid-retrieval storage (represented as 0).

The facility must comply with $m$ contingency plans. Each plan provides two target configurations, where a target configuration specifies a zone and its required storage type. A contingency plan is considered fulfilled if the warehouse adopts the first target configuration, the second target configuration, or both.

Target configurations are provided as non-zero integers. A positive integer $x$ indicates that zone $x$ must be high-density (1). A negative integer $-x$ indicates that zone $x$ must be rapid-retrieval (0).

Determine whether a global configuration for all $n$ zones exists that fulfills every contingency plan simultaneously.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of zones and contingency plans.
Each of the next $m$ lines contains two non-zero integers $l_1$ and $l_2$ ($|l_i| \le n$), representing the two target configurations for a single contingency plan.

## Output
If no valid global configuration exists, print a single line NO.
Otherwise, print YES on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{0, 1\}$) forming any valid configuration.

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
Multiple valid configurations may exist; any one is accepted. The same target configuration may appear in multiple contingency plans.
