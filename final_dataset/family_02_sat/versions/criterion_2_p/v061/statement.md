# Problem B — Thermal Network Equilibration

Time limit: 1 s
Memory limit: 256 MB

## Description
A chemical plant operates $n$ distinct reactors, numbered 1 through $n$. For the upcoming production cycle, every reactor must be configured to exactly one of two thermal modes: "exothermic" (represented by the value 1) or "endothermic" (represented by the value 0).

During a safety review, the engineering team identifies $m$ critical dependencies in the shared coolant network. Each dependency is defined by two target states. A target state is denoted by a non-zero integer: a positive value $+i$ indicates that reactor $i$ is operating in the exothermic mode, while a negative value $-i$ indicates that reactor $i$ is operating in the endothermic mode.

Due to the physics of the coolant network, every dependency enforces a strict fallback mechanism: it is physically impossible for both target states in a dependency to be simultaneously absent. Consequently, if the plant's configuration fails to match one of the target states in a dependency, the system's thermal equilibrium automatically dictates that the configuration must match the other target state. A valid plant configuration is one where the fallback mechanism successfully accommodates all $m$ dependencies.

Your task is to evaluate the full set of dependencies and determine whether there exists a global configuration for all $n$ reactors that is valid. If such a configuration is possible, you must provide one. If the dependencies inherently contradict each other such that no configuration can safely accommodate all of them, you must report this failure.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two non-zero signed integers $l_1$ and $l_2$, with $|l_i| \le n$. These represent the two target states of a single dependency. For the dependency to be satisfied, the final configuration must match at least one of the two target states (it may match both).

## Output
If no valid configuration exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{0, 1\}$) forming any valid configuration.

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
Multiple valid configurations may exist; any one is accepted. The same reactor index may appear in multiple dependencies.
