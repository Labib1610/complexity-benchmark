# Problem A — Resilient Deployment

Time limit: 2 s
Memory limit: 256 MB

A software architecture consists of $n$ microservices. To ensure high availability, these microservices must be distributed across three distinct cloud environments, identified as 1, 2, and 3.

Certain pairs of microservices provide fallback functionality for each other. If a pair of such mutually dependent microservices were hosted in the same environment and that environment experienced an outage, the system would lose both the primary and fallback mechanisms at once. Therefore, you must guarantee that any two microservices with this relationship are deployed to entirely different environments.

Your task is to determine if it is possible to assign every microservice to exactly one of the three cloud environments without violating any of these separation requirements. When multiple valid deployment configurations exist, the automated provisioning system resolves the choice by selecting the configuration that is lexicographically smallest. This means it strongly prefers placing microservice 1 in environment 1, then environment 2, and finally environment 3; if there are still multiple options, it applies the same preference to microservice 2, and so forth.

## Input
The first line provides two integers $n$ and $m$ — the number of microservices and the number of fallback dependencies ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the following $m$ lines contains two integers $u$ and $v$ — a mutually dependent pair of microservices that cannot share an environment.

## Output
If there is no way to deploy the microservices safely, print a single line containing NO.
If a safe deployment is possible, print YES on the first line. On the second line, print $n$ integers $e_1\ e_2\ \dots\ e_n$ (where each $e_i \in \{1,2,3\}$), representing the environment assigned to each microservice $1 \dots n$. This sequence must be the lexicographically smallest valid configuration.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```
