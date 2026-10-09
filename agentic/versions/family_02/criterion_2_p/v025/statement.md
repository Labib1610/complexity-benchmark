# Orbital Fluid Logistics

Time limit: 1 s   Memory limit: 256 MB

## Description

An orbital manufacturing facility manages a network of $n$ flow regulators. Before the production cycle begins, each regulator must be locked into one of two configurations: Active (1) or Standby (0).

The facility's automated safety system enforces $m$ distinct pressure constraints. Every constraint is defined by a pair of conditions, where each condition specifies a required configuration for a particular regulator. To prevent pipeline ruptures, every constraint must have at least one of its two conditions met by the global configuration. A condition is denoted by a non-zero integer: a positive integer $v$ means regulator $v$ must be Active, while a negative integer $-v$ means regulator $v$ must be in Standby. 

Your task is to determine if there exists a single global configuration for all $n$ regulators that satisfies all $m$ pressure constraints simultaneously. If such a configuration exists, you must provide one. Otherwise, you must declare that the constraints are impossible to satisfy. The same regulator may appear in multiple constraints, and a single constraint may even reference the same regulator twice.

To ensure the safety system does not overload the diagnostic processors, the following limits are strictly enforced on the configuration file:
- The total frequency of any single regulator's appearance across all constraints (counting both Active and Standby requirements) is bounded by $2m$.
- The aggregate sum of the absolute values of all regulator identifiers evaluated across the $m$ constraints will never exceed $4 \cdot 10^{10}$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of flow regulators and the number of pressure constraints.
Each of the following $m$ lines contains two non-zero integers $c_1$ and $c_2$ ($1 \le |c_i| \le n$). These represent the two conditions of a constraint; at least one of $c_1$ or $c_2$ must be satisfied in a valid global configuration.

## Output
If there is no valid configuration that satisfies all constraints, output a single line with `NO`.
If a valid configuration exists, output `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \dots, s_n$ separated by spaces, where $s_i \in \{0, 1\}$ represents the configuration of the $i$-th regulator (1 for Active, 0 for Standby). If there are multiple valid configurations, any one is acceptable.

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
