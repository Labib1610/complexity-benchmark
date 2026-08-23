# Problem B — Pipeline Segregation Phase

Time limit: 1 s   Memory limit: 256 MB

In the automated deployment pipeline for the Aegis distributed architecture, the deployment process is divided into three distinct phases: telemetry gathering, module segregation, and binary distribution. You are responsible for implementing the module segregation phase.

During the initial telemetry phase, the system monitors $n$ independent service modules (numbered 1 through $n$) and generates a list of $m$ interference warnings. Each warning specifies a pair of modules that compete for identical hardware resources. 

In your segregation phase, you must assign an operational mode to each of the $n$ modules. The available modes are identified by the integers 1 and 2. To prevent resource collisions, any two modules linked by an interference warning must be configured such that the sum of their mode identifiers is exactly 3.

The final binary distribution phase requires a strictly deterministic configuration to route requests. Because there may be multiple valid ways to assign the modes, the distribution phase expects the sequence of mode assignments that is lexicographically smallest. (An assignment plan is represented as a sequence of $n$ integers, where the $i$-th integer is the mode chosen for module $i$. Sequence $A$ is lexicographically smaller than sequence $B$ if $A$ has a smaller value at the first position where they differ).

If the telemetry constraints are inherently contradictory and no valid assignment exists, your phase must halt the pipeline by rejecting the configuration.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of modules and the number of interference warnings, respectively.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a pair of modules flagged in a warning.

## Output
If no valid assignment plan exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers (each either 1 or 2)—the lexicographically smallest valid assignment plan for the modules.

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