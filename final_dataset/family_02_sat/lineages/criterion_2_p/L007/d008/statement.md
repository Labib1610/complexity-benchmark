# Problem B — Feature Flag Compatibility

Time limit: 1 s
Memory limit: 256 MB

## Description
You are configuring a software environment with $n$ feature flags. Each flag $i$ ($1 \le i \le n$) must be set to either ON (1) or OFF (0).

The system has $m$ legacy compatibility rules that must be respected. Each rule specifies two requirements, represented by two non-zero integers $l_1$ and $l_2$. 
For any given requirement $l$:
- If $l > 0$, the requirement is met when flag $l$ is set to ON (1).
- If $l < 0$, the requirement is met when flag $|l|$ is set to OFF (0).

A compatibility rule is violated if and only if neither of its two requirements is met. To ensure a stable environment, you must find a global configuration for all $n$ feature flags such that not a single rule is violated.

Determine if such a configuration exists.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of feature flags and the number of compatibility rules.
Each of the next $m$ lines contains two non-zero integers $l_1$ and $l_2$ ($1 \le |l_1|, |l_2| \le n$), representing the two requirements for a single rule.

## Output
If no valid global configuration exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{0, 1\}$) forming any valid configuration.

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
Multiple valid configurations may exist; any one is accepted. The same flag index may appear in multiple rules, and it is possible that $l_1 = l_2$ or $l_1 = -l_2$ within a single rule.