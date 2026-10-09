# Phase 3: Deployment Planner

Time limit: 1 s   Memory limit: 256 MB

## Description
You are managing the deployment of $n$ microservices. Each microservice must be allocated to exactly one of two environments: the Primary Environment (represented by 1) or the Secondary Environment (represented by 0).

The architecture includes $m$ redundancy protocols to ensure reliability. Each protocol consists of two diagnostic probes, represented by non-zero integers. A probe $v$ monitors microservice $|v|$ and evaluates its allocation. The probe generates a *deviation warning* if microservice $|v|$ is placed in the Secondary Environment when $v > 0$, or if it is placed in the Primary Environment when $v < 0$.

A protocol triggers a cascading system halt if and only if both of its diagnostic probes generate a deviation warning simultaneously. Your task is to determine whether there exists a global allocation—assigning every microservice to either the Primary or Secondary environment—such that absolutely zero protocols trigger a system halt.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of microservices and the number of redundancy protocols.

Each of the following $m$ lines provides a protocol as two non-zero integers $l_1$ and $l_2$ ($1 \le |l_i| \le n$), representing its two diagnostic probes.

## Output
If no valid global allocation exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ separated by spaces. Print $s_i = 1$ if microservice $i$ is allocated to the Primary Environment, and $s_i = 0$ if it is allocated to the Secondary Environment. Any valid allocation is accepted.

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