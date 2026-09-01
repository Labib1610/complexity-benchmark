# Problem B — Phase Alignment

Time limit: 1 s   Memory limit: 256 MB

In the automated deployment pipeline for the Aegis distributed architecture, the deployment process requires configuring a set of service modules. You are responsible for the phase alignment step.

The system monitors $n$ service modules (numbered 1 through $n$) and generates a log of $m$ collision warnings. Each warning specifies a pair of modules that compete for identical hardware resources. 

To resolve these collisions, you must assign a configuration state $x_i \in \{1, 2\}$ to each module $i$. To guarantee stability, for every collision warning involving modules $u$ and $v$, their assigned configuration states must satisfy the condition $|x_u - x_v| = 1$. 

The final binary distribution mechanism requires a strictly deterministic configuration to route requests. Because there may be multiple valid state assignments, the mechanism expects the assignment sequence that is lexicographically smallest. (An assignment sequence is represented as $n$ integers $x_1, x_2, \dots, x_n$. Sequence $A$ is lexicographically smaller than sequence $B$ if $A$ has a smaller value at the first position where they differ).

If the collision constraints are inherently contradictory and no valid assignment of states exists, your step must halt the pipeline by rejecting the configuration.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of modules and the number of collision warnings, respectively.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a pair of modules that are featured in a collision warning.

## Output
If no valid assignment sequence exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers (each either 1 or 2)—the lexicographically smallest valid assignment sequence for the modules.

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