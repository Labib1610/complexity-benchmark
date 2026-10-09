# Phase 3: Deployment Planner

Time limit: 1 s   Memory limit: 256 MB

## Description

The continuous integration pipeline for our cloud infrastructure operates in four distinct phases:
1. **Manifest Aggregation**: Developers submit compatibility requirements for their microservices.
2. **Policy Compilation**: The orchestrator filters all requirements down to a flat list of $m$ fallback policies covering $n$ microservices.
3. **Deployment Planning (Your Task)**: You must navigate a massive search space to find a valid global configuration. With $n$ microservices, each capable of being in either an "upgraded" or "legacy" state, there are $2^n$ possible global configurations to consider. Your system must search this space to find a configuration that simultaneously satisfies all $m$ fallback policies. Each policy is defined by exactly two acceptable service states (where a service state is a specific microservice and its required mode, upgraded or legacy). A policy evaluates to true if the global configuration contains at least one of those two states. If a valid configuration exists in the $2^n$ space, you must output it so the pipeline can proceed. Otherwise, you must halt the pipeline.
4. **Rollout Execution**: The system reads your configuration and physically deploys the specified versions.

Write the program for Phase 3. The input is guaranteed to be the output of Phase 2. 

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of microservices and the number of fallback policies.
Each of the following $m$ lines provides a policy as two non-zero integers $l_1$ and $l_2$ ($|l_i| \le n$).
The absolute value of an integer indicates the microservice ID. A positive integer means the required state is "upgraded", while a negative integer means the required state is "legacy". At least one of the two states in each policy must be present in the final configuration.

## Output
If no valid global configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ separated by spaces. Print $s_i = 1$ if microservice $i$ is upgraded, and $s_i = 0$ if it remains legacy, forming any valid configuration.

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
Multiple valid configurations may exist; any one is accepted. The same microservice ID may appear in multiple policies.
