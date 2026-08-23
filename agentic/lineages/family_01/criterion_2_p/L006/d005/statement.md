# Entanglement Initialization

Time limit: 1 s   Memory limit: 256 MB

A quantum register consists of $n$ qubits, sequentially labeled from 1 to $n$. You are tasked with initializing this register by assigning a configuration code to each qubit. Each configuration code must be chosen from the set {1, 2}.

The register's architecture includes $m$ hardware entanglement links, each connecting a specific pair of qubits. The system requires operational stability across all these connections. Specifically, an entanglement link is stable if and only if the product of the configuration codes assigned to its two endpoints evaluates to exactly 2.

Your objective is to find an assignment of configuration codes for all $n$ qubits such that every single entanglement link in the circuit is stable.

In cases where multiple valid assignments exist, the compiler applies a deterministic tie-breaker. It forms an $n$-digit integer by concatenating the sequence of configuration codes $c_1, c_2, \dots, c_n$. The compiler will always choose the valid assignment that produces the minimum possible value for this $n$-digit integer. If it is impossible to stabilize all links simultaneously, the compilation process aborts.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of qubits and the number of entanglement links.
Each of the subsequent $m$ lines provides two integers $u$ and $v$, specifying that an entanglement link connects qubit $u$ and qubit $v$.

## Output
If the register cannot be fully stabilized, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $c_1, c_2, \dots, c_n$ (where each $c_i \in \{1, 2\}$). These integers must represent the configuration codes of the assignment that minimizes the concatenated $n$-digit integer described above.

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