# Problem B — Quantum Array Calibration

Time limit: 1 s   Memory limit: 256 MB

## Description

You are tasked with finding a valid operating state for a quantum computing array consisting of $n$ qubits. Each qubit must be calibrated into one of two basis states: state 1 or state 0. The configuration space contains $2^n$ possible global calibrations.

The system's error-correction protocol enforces a rigid set of $m$ dependencies. The array is considered stable if and only if all $m$ dependencies are simultaneously satisfied. Each dependency provides a list of acceptable basis conditions, and the dependency is satisfied if at least one of those conditions is met by the global calibration. A basis condition is a requirement that a specific qubit is set to a specific state. Due to the hardware's pairwise entanglement routing, every dependency in this specific protocol lists exactly two basis conditions.

Write a program to evaluate the $2^n$ configuration space to determine if a stable global calibration exists, and if so, output one.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines describes a dependency using two non-zero signed integers $l_1$ and $l_2$, where $|l_1|, |l_2| \le n$. A positive integer $x$ indicates a condition that qubit $x$ is in state 1. A negative integer $-x$ indicates a condition that qubit $x$ is in state 0. For each dependency, at least one of the two conditions must be met.

## Output
If no valid calibration exists in the state space, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \ldots, s_n$ (each either 0 or 1) representing the state of each qubit in a valid calibration.

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
Multiple valid calibrations may exist; any one is accepted. The same qubit may appear in multiple dependencies.
