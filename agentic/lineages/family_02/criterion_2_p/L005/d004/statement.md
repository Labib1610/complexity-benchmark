# Problem B — Quantum Array Calibration

Time limit: 1 s   Memory limit: 256 MB

## Description

You are tasked with finding a valid operating state for a quantum computing array consisting of $n$ qubits, numbered 1 to $n$. A global calibration of the array is defined by choosing a subset $S \subseteq \{1, 2, \ldots, n\}$ of qubits to be placed in state 0. The remaining qubits, those not in $S$, are placed in state 1.

The system's error-correction protocol monitors a rigid set of $m$ entanglement routes. Each route imposes a structural restriction on the subset $S$. 

A route is defined by two non-zero integers $l_1$ and $l_2$. From these, we construct two sets for the route:
- The positive dependency set $P$, which contains any positive integers among $l_1, l_2$.
- The negative dependency set $N$, which contains the absolute values of any negative integers among $l_1, l_2$.

For example, if a route is given as `3 -5`, its positive dependency set is $P = \{3\}$ and its negative dependency set is $N = \{5\}$. If a route is given as `-2 -2`, then $P = \emptyset$ and $N = \{2\}$.

A critical fault occurs if the chosen subset $S$ simultaneously acts as a superset of $P$ and a subset of the complement of $N$. In set-theoretic terms, a route triggers a fault if and only if:
$P \subseteq S \subseteq N^c$
where $N^c$ is the set of all qubits in $\{1, 2, \ldots, n\}$ that are not in $N$.

The array is considered stable if no route triggers a critical fault. Write a program to determine if a stable global calibration $S$ exists, and if so, output one.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines describes a route using two non-zero signed integers $l_1$ and $l_2$, where $|l_1|, |l_2| \le n$. 

## Output
If no valid calibration exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \ldots, s_n$ (each either 0 or 1) representing the state of each qubit in a valid calibration. Specifically, $s_i = 0$ if qubit $i \in S$, and $s_i = 1$ if qubit $i \notin S$.

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
Multiple valid calibrations may exist; any one is accepted. The same qubit may appear in multiple routes.