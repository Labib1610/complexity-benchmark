# Microservice Anti-Affinity

Time limit: 1 s   Memory limit: 256 MB

You are configuring the deployment of a new backend system consisting of $n$ microservices, indexed from $1$ to $n$. There are exactly two available data centers, designated as Center 1 and Center 2.

Each microservice must be deployed to exactly one of the two centers. Your deployment plan can be represented as a sequence of $n$ integers $c_1, c_2, \dots, c_n$, where each $c_i \in \{1, 2\}$ indicates the center hosting microservice $i$.

The system's reliability engineers have specified $m$ strict anti-affinity rules. Each rule is defined by a pair of microservices $(u, v)$. Due to shared resource bottlenecks or redundancy requirements, the two microservices in a rule must never be deployed to the same center.

Your task is to find a deployment plan that satisfies all $m$ rules. Since there could be multiple valid plans, you must output the one that is lexicographically smallest. A plan $A$ is lexicographically smaller than plan $B$ if, at the first index $i$ where they differ, plan $A$ has microservice $i$ in Center 1 and plan $B$ has it in Center 2.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing an anti-affinity rule between microservice $u$ and microservice $v$.

## Output
If no valid deployment plan exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $c_1, c_2, \dots, c_n$ (each either 1 or 2) representing the lexicographically smallest valid deployment plan.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```