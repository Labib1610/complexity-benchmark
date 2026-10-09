# Problem B — System Configuration Search

Time limit: 1 s   Memory limit: 256 MB

## Description
You are tasked with configuring a system of $n$ binary switches. Each switch must be set to either 1 or 0. The total configuration space consists of $2^n$ possible global settings. You must determine if there exists a setting that satisfies a collection of $m$ system rules.

A system rule is defined by a set of target switch states. A rule is successfully evaluated if at least one of its target states matches the current global setting. The entire system is only viable if all $m$ rules evaluate successfully at the same time. 

Each of the $m$ rules in this system is defined by exactly two target switch states. 

Given the rules, evaluate the $2^n$ possible settings to find a valid global configuration, or report if the rules are mutually contradictory.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines describes a rule using two non-zero integers $l_1$ and $l_2$ ($|l_i| \le n$). An integer $x > 0$ represents the target state where switch $x$ is set to 1. An integer $x < 0$ represents the target state where switch $|x|$ is set to 0.

## Output
If no valid global configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{0, 1\}$) representing the value assigned to each switch from 1 to $n$. If multiple valid configurations exist, any one of them is accepted.

## Example 1
### Input
```
2 2
1 2
-1 -2
```
### Output
```
YES
1 0
```

## Example 2
### Input
```
1 2
1 1
-1 -1
```
### Output
```
NO
```

## Note
The same switch state may appear in multiple rules.
