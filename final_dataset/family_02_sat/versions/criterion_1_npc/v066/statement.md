# Problem A — Initialization Pipeline

Time limit: 2 s   Memory limit: 256 MB

## Description
The deployment pipeline for a modular reactor involves three distinct phases. First, a dependency analyzer scans the blueprints and generates $m$ operational constraints over $n$ toggleable flow valves. Each valve must be strictly set to OPEN or CLOSED.

Your task is to implement the second phase: the configuration synthesizer. The synthesizer receives the constraints from the analyzer. Each constraint specifies exactly three desired valve states (a valve state is a specific valve combined with a required status, OPEN or CLOSED). For the reactor to be safely initialized, every single constraint must be satisfied. A constraint is satisfied if the actual configuration matches at least one of its three desired valve states. A constraint with none of its desired states matched causes a failure. The synthesizer must determine if there is a single, global configuration of all $n$ valves that satisfies all $m$ constraints simultaneously.

If a configuration is found, it is passed to the third phase, where automated actuators physically set the valves before ignition. If no such configuration exists, the synthesizer must abort the pipeline so engineers can manually redesign the blueprints.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$).
Each of the next $m$ lines contains three non-zero signed integers $v_1, v_2, v_3$, with $|v_i| \le n$. A positive integer indicates the desired state for that valve is OPEN, and a negative integer indicates the desired state is CLOSED. At least one of the three desired states must match the actual configuration for the constraint to pass.

## Output
If no valid configuration exists, print a single line NO.
Otherwise print YES on the first line. On the second line print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{0, 1\}$), where $s_i$ is the state of valve $i$ (1 for OPEN, 0 for CLOSED). Any valid configuration is accepted.

## Example 1
Input:
```
3 2
1 2 3
-1 2 -3
```
Output:
```
YES
0 0 1
```

## Example 2
Input:
```
1 2
1 1 1
-1 -1 -1
```
Output:
```
NO
```

## Note
Each constraint has exactly three entries. The same valve index may appear more than once in a single constraint.
