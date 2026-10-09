# Phase 2: Link Isolation Module

Time limit: 2 s   Memory limit: 256 MB

## Description
The automated calibration pipeline for a dual-bank crossbar switch operates in three stages.

**Phase 1 (Topology Profiling):** The system scans the switch hardware, which consists of a bank of primary terminals and a bank of secondary terminals. It records every physical trace connecting a primary terminal to a secondary terminal. Traces only ever connect a primary terminal to a secondary one; there are no internal connections within the same bank. A key hardware metric is the peak terminal density, denoted $\Delta$, which is the highest number of traces attached to any single terminal across the entire switch.

**Phase 2 (Link Isolation):** This is the module you must implement. You are provided the raw trace topology from Phase 1. You must first deduce $\Delta$. Then, to prevent electrical interference during calibration, traces must be tested in separate time slots. Your module must assign each trace to a time slot numbered from $1$ to $\Delta$. The critical safety constraint is that if two traces share the same terminal (either primary or secondary), they must be assigned to different time slots. The physical architecture of the dual-bank switch guarantees that it is always mathematically possible to pack all traces into exactly $\Delta$ time slots without violating this safety constraint.

**Phase 3 (Execution):** The hardware sequencer reads your assignments and energizes the traces slot by slot, completing the calibration.

Given the topology from Phase 1, output a valid slot assignment for every trace so that Phase 3 can execute safely.

## Input
First line: three integers $n_L$, $n_R$, $m$ ($1 \le n_L, n_R \le 100000$, $0 \le m \le 400000$), representing the number of primary terminals, the number of secondary terminals, and the total number of traces.
Next $m$ lines: two integers $u$ and $v$ ($1 \le u \le n_L$, $1 \le v \le n_R$) representing a trace between primary terminal $u$ and secondary terminal $v$.

## Output
Print `YES` on the first line. On the second line, print $m$ space-separated integers, where the $i$-th integer (from $1$ to $\Delta$) is the time slot assigned to the $i$-th trace from the input.

## Example

**Input**
```text
4 4 5
1 2
1 3
2 3
3 4
4 4
```

**Output**
```text
YES
1 2 1 1 2
```
