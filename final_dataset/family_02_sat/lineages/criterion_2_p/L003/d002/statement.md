# Phase 3: Deployment Planner

Time limit: 1 s   Memory limit: 256 MB

## Description
You are managing the deployment of $n$ microservices. Each microservice must be allocated to exactly one of two environments: the Primary Environment (represented by 1) or the Secondary Environment (represented by 0).

The architecture includes $m$ redundancy protocols to ensure reliability. Each protocol defines two preferred deployment states. A preferred deployment state is represented by a non-zero integer $v$. The absolute value $|v|$ identifies the microservice. A positive $v$ indicates a preference for microservice $|v|$ to be in the Primary Environment. A negative $v$ indicates a preference for microservice $|v|$ to be in the Secondary Environment.

A redundancy protocol is considered breached if and only if the final allocation simultaneously fails to match both of the protocol's preferred deployment states. Your task is to determine whether there exists a global allocation—assigning every microservice to either the Primary or Secondary environment—such that absolutely zero redundancy protocols are breached.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of microservices and the number of redundancy protocols.

Each of the following $m$ lines provides a protocol as two non-zero integers $l_1$ and $l_2$ ($1 \le |l_i| \le n$). The absolute value $|l_i|$ identifies the microservice. A positive $l_i$ specifies the Primary Environment for microservice $|l_i|$; a negative $l_i$ specifies the Secondary Environment for microservice $|l_i|$.

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

## Note
Multiple valid allocations may exist; any one is accepted. The same microservice ID may appear in multiple protocols, and even within the same protocol (for example, a protocol given as `3 3` simply means the system cannot fail to match this preference, effectively mandating that specific state). If $m = 0$, any allocation is valid.