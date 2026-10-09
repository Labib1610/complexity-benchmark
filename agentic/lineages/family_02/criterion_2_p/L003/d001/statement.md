# Phase 3: Deployment Planner

Time limit: 1 s   Memory limit: 256 MB

## Description

You are configuring a network of $n$ microservices. Each microservice must be assigned to exactly one of two routing paths: Route 1 or Route 0.

The system is governed by $m$ compatibility rules. Each rule links two potential routing targets to ensure network stability. A target is represented by a non-zero integer. The absolute value of the integer identifies the microservice. A positive integer designates Route 1 as the target for that service, while a negative integer designates Route 0. 

A rule is satisfied if the final global configuration successfully implements at least one of its two linked targets. Your task is to determine if there exists a global configuration—assigning every microservice to either Route 1 or Route 0—that satisfies all $m$ rules simultaneously.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of microservices and the number of compatibility rules.

Each of the following $m$ lines provides a rule as two non-zero integers $l_1$ and $l_2$ ($|l_i| \le n$). The absolute value $|l_i|$ identifies the microservice. A positive $l_i$ designates Route 1 as the target for microservice $|l_i|$; a negative $l_i$ designates Route 0 as the target for microservice $|l_i|$.

## Output
If no valid global configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ separated by spaces. Print $s_i = 1$ if microservice $i$ is assigned to Route 1, and $s_i = 0$ if it is assigned to Route 0. Any valid configuration is accepted.

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
Multiple valid configurations may exist; any one is accepted. The same microservice ID may appear in multiple rules, and even within the same rule.