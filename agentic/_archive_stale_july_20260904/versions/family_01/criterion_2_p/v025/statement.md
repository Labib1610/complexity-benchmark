# Problem B — Quantum Core Allocation

Time limit: 1 s   Memory limit: 256 MB

You are tasked with initializing a dual-core quantum processor. The processor consists of $n$ quantum registers, and it has two processing cores, designated as Core 1 and Core 2.

During initialization, you must allocate each register to exactly one of the two cores. However, the system contains $m$ entanglement links between pairs of registers. If two registers connected by an entanglement link are allocated to the same core, the resulting interference will destabilize the processor.

The entanglement network topology guarantees the following properties to ensure stability during initialization:
- The sum of the endpoint counts across all $n$ registers is always exactly $2m$ (each link provides exactly two endpoints).
- For any arbitrary subset of registers, the total number of entanglement links completely contained within that subset is at most $m$.
- The combined total of registers and links ($n + m$) is guaranteed not to exceed $400,000$.

Your task is to determine if there is a valid allocation of all $n$ registers to the two cores such that no two linked registers are assigned to the same core. If such an allocation exists, you must find the one that is lexicographically smallest. An allocation is represented as a sequence of $n$ integers, where the $i$-th integer is the core (1 or 2) assigned to the $i$-th register. A sequence $A$ is lexicographically smaller than sequence $B$ if, at the first position where they differ, sequence $A$ has a smaller core number than sequence $B$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$) — the number of quantum registers and the number of entanglement links, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — indicating an entanglement link between register $u$ and register $v$.

## Output
If there is no valid core allocation that prevents destabilization, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $c_1, c_2, \dots, c_n$ (where each $c_i \in \{1, 2\}$), representing the lexicographically smallest valid allocation.

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
