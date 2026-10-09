# Phase Configuration for the Alpha-Omega Matrix

Time limit: 2 s   Memory limit: 256 MB

## Description
You must determine a valid execution schedule for a decentralized engine processing $m$ parallel jobs. Each job requires the exclusive lock of exactly two resources to execute. If two jobs require the same resource, they must be assigned to different execution phases to prevent locking conflicts.

To minimize overall runtime, the system administrator requires that the total number of execution phases, $K$, must exactly equal the maximum number of jobs requesting any single resource.

Your objective is to assign a phase (an integer from 1 to $K$) to each of the $m$ jobs. The configuration space consists of $K^m$ potential phase assignments. A collision is defined as any two jobs sharing at least one resource being assigned the exact same phase. You must find a configuration entirely free of collisions.

The resources in this system are strictly partitioned into two independent sets: Alpha resources and Omega resources. Every job in the input specifies exactly one Alpha resource and exactly one Omega resource that it needs to lock. No job ever requires two Alpha resources or two Omega resources. Due to this structural property, a valid configuration using exactly $K$ phases is always guaranteed to exist.

You must output a valid assignment of phases for all $m$ jobs.

## Input
First line: three integers $N_\alpha$, $N_\omega$, $m$ (1 ≤ $N_\alpha, N_\omega$ ≤ 100000, 0 ≤ $m$ ≤ 400000).
Next $m$ lines: two integers $u$ and $v$ (1 ≤ $u$ ≤ $N_\alpha$, 1 ≤ $v$ ≤ $N_\omega$), indicating that a job requires Alpha resource $u$ and Omega resource $v$.

## Output
Print `YES`, then a line with $m$ integers in $1 \dots K$ — the phase assigned to the $i$-th job in input order (jobs sharing any resource must differ).

## Example 1
### Input
```text
3 3 5
1 1
1 2
2 2
2 3
3 1
```
### Output
```text
YES
1 2 1 2 2
```
