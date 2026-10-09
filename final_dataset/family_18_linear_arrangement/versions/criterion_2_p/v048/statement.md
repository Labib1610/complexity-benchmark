# Processor Layout Stage

Time limit: 5 s
Memory limit: 256 MB

## Description
The production of a new quantum processor consists of three stages: qubit fabrication, physical layout, and operational calibration. You are responsible for the second stage: physical layout.

During this stage, you receive $n$ fabricated qubits (labeled 1 to $n$). The processor chassis contains $n$ distinct slots arranged in a single straight line, numbered consecutively from $1$ to $n$. Your task is to assign each qubit to exactly one unique slot.

To prepare for the calibration stage, you are given a list of $m$ required entanglement links between specific pairs of qubits. The system is designed such that every qubit is reachable from any other qubit through a sequence of these links. Furthermore, the architecture is strictly minimal to prevent interference, meaning there are exactly $m = n - 1$ links in total.

When two linked qubits are assigned to slots, the length of the link between them is the absolute difference of their slot numbers. The sum of the lengths of all $m$ links must not exceed a thermal budget $B$. If the total length exceeds $B$, the subsequent calibration stage will fail due to excessive heat dissipation.

Determine if a layout exists that satisfies the budget $B$, and if so, provide one such layout so the processor can proceed to calibration.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the following $m$ lines contains two integers $u$ and $v$, representing an entanglement link required between qubit $u$ and qubit $v$. Qubits are 1-indexed.

## Output
If a valid assignment of qubits to slots exists that satisfies the budget, print `YES` on the first line. On the second line, print $n$ space-separated integers representing the assigned slot number (from $1$ to $n$) for qubit $1, 2, \dots, n$ respectively.
If no layout can satisfy the budget, print `NO`.

## Example

**Input:**
```
4 3 4
1 2
2 3
2 4
```

**Output:**
```
YES
1 2 3 4
```
