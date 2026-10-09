# Problem A — Vault Door Mechanism

Time limit: 2 s   Memory limit: 256 MB

## Description

A security firm is building a high-tech vault door governed by $n$ binary actuators. To unseal the vault, a single configuration must be applied to the actuators, setting each to either an extended state (1) or a retracted state (0). There are no intermediate states, and every actuator must be assigned a state.

The door's primary locking mechanism is secured by $m$ sliding cross-bars. Each cross-bar is held in place by exactly three mechanical linkages, which are in turn connected to the actuators. A linkage's connection is represented by a non-zero integer $x$:
- If $x > 0$, the linkage will clear its cross-bar if actuator $x$ is set to the extended state (1).
- If $x < 0$, the linkage will clear its cross-bar if actuator $|x|$ is set to the retracted state (0).

A cross-bar will successfully slide open if **at least one** of its three mechanical linkages clears it. If a cross-bar has none of its three linkages clear it, the cross-bar remains locked and the vault door will not open. A single actuator may be connected to multiple cross-bars through various linkages, and it may be required to extend for one linkage but retract for another. 

To prevent mechanical stress on the vault chassis, the design guarantees that for any cross-bar, the sum of the squares of its three linkage values never exceeds 24,300. Furthermore, the total number of mechanical linkages across all cross-bars in the vault door is guaranteed to be at most 1,200.

Your task is to determine whether there exists a global configuration of the $n$ actuators that allows all $m$ cross-bars to slide open simultaneously.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$).
Each of the next $m$ lines contains three non-zero integers $l_1, l_2, l_3$, with $|l_i| \le n$. These represent the three mechanical linkages for a single cross-bar. At least one of the three linkages must clear the cross-bar for the vault to open.

## Output
If no such actuator configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each either 0 or 1), where $s_i$ is the required state of actuator $i$. Any valid configuration is accepted.

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
Each cross-bar always has exactly three mechanical linkages. The same actuator index may appear more than once within the linkages of a single cross-bar.
