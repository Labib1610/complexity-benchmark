# Problem B — Warehouse Zone Configurations

Time limit: 1 s   Memory limit: 256 MB

## Description
An automated warehouse manages $n$ storage zones. Each zone must be configured to operate in either state 1 (high-density) or state 0 (rapid-retrieval).

The facility must comply with $m$ contingency plans. Each plan imposes a restriction on a pair of zones, provided as two non-zero integers $l_1$ and $l_2$. 

For any non-zero integer $v$, let its designated zone be $|v|$ and its designated state be 1 if $v > 0$, and 0 if $v < 0$. 
A contingency plan $(l_1, l_2)$ forbids exactly one combination of states for its designated zones. Specifically, a configuration violates the plan if zone $|l_1|$ is assigned the state opposite to its designated state while simultaneously zone $|l_2|$ is assigned the state opposite to its designated state. Any other combination of states for these two zones satisfies the plan.

Determine whether a global configuration for all $n$ zones exists that avoids the forbidden combination for every contingency plan.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of zones and contingency plans.
Each of the next $m$ lines contains two non-zero integers $l_1$ and $l_2$ ($|l_i| \le n$), representing the parameters for a single contingency plan.

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
Multiple valid configurations may exist; any one is accepted. The same constraint parameters may appear in multiple contingency plans.