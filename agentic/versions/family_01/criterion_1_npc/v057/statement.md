# Orbital Power Routing

Time limit: 2 s
Memory limit: 256 MB

The deployment sequence for a new orbital satellite involves a three-phase initialization process for its electronic modules. Your task is to implement the software for the second phase of this sequence.

In Phase I (Interference Profiling), onboard diagnostics analyze electromagnetic sensitivities. This phase produces a list of module pairs that will experience severe crosstalk if they draw power from the same source. 

In Phase II (Tri-Band Allocation), which you must implement, the system assigns each module to one of exactly three independent power bands, designated by the identifiers 1, 2, and 3. A valid allocation must ensure that no two modules flagged during Phase I are assigned to the same power band. Because Phase III requires strict determinism, if multiple valid allocations exist, Phase II must produce the one that is lexicographically smallest. (An allocation sequence $A$ is lexicographically smaller than $B$ if, at the first module where they differ, $A$ assigns a lower band identifier than $B$.)

In Phase III (Firmware Compilation), a downstream compiler uses the allocation from Phase II to flash the final operating parameters into each module's memory. If Phase II determines that no safe allocation is possible, the initialization sequence is aborted.

You are provided with the output of Phase I. You must produce the exact output required by Phase III.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$), representing the number of electronic modules and the number of crosstalk-sensitive pairs identified in Phase I. The modules are numbered 1 through $n$.
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that module $u$ and module $v$ cannot be assigned to the same power band.

## Output
If Phase II cannot find any valid allocation, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $b_1, b_2, \dots, b_n$, where $b_i \in \{1, 2, 3\}$ is the power band assigned to module $i$. This sequence must be the lexicographically smallest among all valid allocations.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```
