# Problem B — Quantum Calibration Checks

Time limit: 1 s   Memory limit: 256 MB

## Description

A quantum computing facility contains **n** qubits. Each qubit must be initialized to a spin state of either 0 or 1.
The facility performs **m** calibration checks to ensure system stability. Each check monitors a pair of qubits, specified by two non-zero integers $l_1$ and $l_2$.

The absolute value $|l_i|$ identifies which qubit is being monitored. The sign of $l_i$ defines the target spin state for that connection: a positive $l_i$ means the target spin is 1, and a negative $l_i$ means the target spin is 0.

For a given initialization of the qubits, each check evaluates structural stability using a three-particle reference system. Initially, three reference particles are placed at positions 1, 2, and 3. The evaluation proceeds in two steps:
1. If the actual spin of qubit $|l_1|$ does not match its target spin (derived from the sign of $l_1$), the particles currently at positions 1 and 2 are swapped.
2. Next, if the actual spin of qubit $|l_2|$ does not match its target spin (derived from the sign of $l_2$), the particles currently at positions 2 and 3 are swapped.

A calibration check is considered stable if and only if, after both steps are completed, at least one of the three reference particles remains in its original starting position (1, 2, or 3). If no particle is in its original position, a system fault occurs.

You must determine whether there exists a single global initialization of all **n** qubits (each set to 0 or 1) such that all **m** calibration checks operate stably simultaneously. If such an initialization exists, report one; otherwise, report that the calibration requirements are mutually contradictory.

## Input
The first line contains two integers **n** and **m** (1 ≤ n ≤ 10^5, 0 ≤ m ≤ 2·10^5).
Each of the next **m** lines contains two non-zero signed integers $l_1$ and $l_2$. For each integer, $1 \le |l_i| \le n$. 
The two integers in a check may have the same absolute value (meaning the check monitors the same qubit twice, potentially with the same or opposite signs).

## Output
If no valid initialization exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print **n** integers $f_1 \ f_2 \dots f_n$ (each in {0, 1}) forming any valid initialization, where the $i$-th integer represents the spin of qubit $i$.

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
Multiple valid initializations may exist; any one is accepted. The same qubit may appear in multiple checks, and even twice within the same check.