# Problem B — Quantum Array Calibration

Time limit: 1 s   Memory limit: 256 MB

## Description
A quantum computing array contains $n$ individual qubits. For the system to function, every qubit must be calibrated into exactly one of two basis states: state 1 or state 0.

The hardware's pairwise entanglement routing generates a rigid set of $m$ dependencies. Every dependency provides exactly two basis conditions. A basis condition is a specification that a particular qubit must be in a particular state. For any given dependency to be resolved, the array's calibration must align with at least one of the two conditions it provides. The entire array achieves stability if and only if all $m$ dependencies are resolved at the same time.

Your objective is to evaluate the system and determine whether a stable global calibration can be achieved. If such a calibration exists, you must also provide a valid state assignment for each qubit.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
The following $m$ lines each describe a single dependency using two non-zero integers $l_1$ and $l_2$, where $|l_1|, |l_2| \le n$. A positive integer $x$ represents a condition that qubit $x$ is calibrated to state 1. A negative integer $-x$ represents a condition that qubit $x$ is calibrated to state 0. In each dependency, at least one of the two represented conditions must be matched by the final calibration.

## Output
If the array cannot reach stability, output a single line containing `NO`.
If a stable calibration exists, output `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \ldots, s_n$ separated by spaces, where each $s_i$ is either 0 or 1, representing the state of the $i$-th qubit. If multiple valid calibrations are possible, providing any one of them is acceptable.

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
