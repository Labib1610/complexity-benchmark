# Problem B — Pipeline Stabilization

Time limit: 1 s   Memory limit: 256 MB

## Description
You are configuring an automated genetic sequencing pipeline with $n$ target gene markers. Each marker must be globally set to either activated (1) or suppressed (0).

The pipeline's stabilization criteria are defined by $m$ interaction constraints. Each constraint specifies exactly two marker states. A marker state is denoted by a non-zero integer: a positive integer $i$ means marker $i$ must be activated, and a negative integer $-i$ means marker $i$ must be suppressed. For the pipeline to stabilize, every constraint must have at least one of its two specified marker states satisfied by the global configuration.

Because each constraint links exactly two marker states, failing to satisfy one state forces the other state to be satisfied. This creates chains of forced consequences throughout the pipeline. 

To ensure the pipeline evaluates efficiently, the system guarantees two properties for all valid inputs:
1. The total number of marker states specified across all $m$ constraints will never exceed 400,000.
2. For any individual constraint, the sum of the absolute values of its two marker indices will never exceed 200,000.

Determine if there exists a global configuration of all $n$ markers that satisfies every interaction constraint simultaneously. If so, provide one such configuration. Otherwise, report that the constraints are mutually contradictory.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two non-zero integers $l_1$ and $l_2$ ($1 \le |l_i| \le n$), representing the two marker states for that constraint.

## Output
If no valid configuration exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each $0$ or $1$) forming any valid configuration.

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
Multiple valid configurations may exist; any one is accepted. The same marker state may appear in multiple constraints.
