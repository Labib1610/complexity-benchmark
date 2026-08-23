# Entanglement Initialization

Time limit: 1 s   Memory limit: 256 MB

You are programming the initial states of a quantum register containing $n$ qubits, labeled 1 to $n$. Each qubit must be initialized into one of two basis projections, identified by a state code:
- Code 1: sets the projection value to $+\frac{1}{2}$.
- Code 2: sets the projection value to $-\frac{1}{2}$.

The quantum circuit contains $m$ entanglement links between specific pairs of qubits. To maintain the system's conservation of angular momentum, every linked pair must have a combined projection (the sum of their individual projection values) of exactly $0$. 

You need to determine if there is a valid initialization of all $n$ qubits that satisfies the conservation requirement for all $m$ linked pairs.

When multiple valid initializations exist, the compiler uses a specific tie-breaking rule. It concatenates the assigned state codes $c_1, c_2, \dots, c_n$ (where each $c_i \in \{1, 2\}$) to form a single $n$-digit integer. The compiler selects the initialization that results in the smallest possible integer. If no valid initialization exists, the compilation fails.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
The following $m$ lines each contain two integers $u$ and $v$ — indicating that qubit $u$ and qubit $v$ share an entanglement link.

## Output
If no valid initialization is possible, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers $c_1, c_2, \dots, c_n$ (where each $c_i \in \{1, 2\}$) representing the state code assigned to each qubit in the initialization that minimizes the $n$-digit integer described above.

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