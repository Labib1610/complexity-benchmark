# Pre-screening the Freight Pipeline

Time limit: 2 s   Memory limit: 256 MB

## Description

Our automated logistics platform processes client manifests in three distinct stages:
1. **Stage 1: Pre-screening (Your Task)** – Rapidly evaluate the manifest to catch obvious impossibilities.
2. **Stage 2: Sequence Optimization** – Determine the exact chronological dispatch order for all vehicles.
3. **Stage 3: Fleet Dispatch** – Transmit the finalized itinerary to the operators.

You are responsible for implementing Stage 1. A client submits a manifest of **j** freight contracts alongside a strict completion deadline of **T** hours. Every contract demands a sea voyage (Phase 1) followed by a rail journey (Phase 2). The company operates exactly one ship for Phase 1 and one train for Phase 2. Each vehicle can process only one contract at a time, and a contract is only ready for Phase 2 once its Phase 1 concludes.

Before routing the manifest to the computationally expensive Stage 2 optimizer, your module must verify if the deadline is structurally impossible to meet. For all datasets evaluated, the manifest is guaranteed to be unachievable, and your pre-screening module will detect this by triggering exactly one of the two rejection rules below. You must output the corresponding rejection code to abort the pipeline.

- **Rejection Rule A (Single-Contract Bottleneck):** If the combined Phase 1 and Phase 2 duration for any individual contract exceeds **T**, that contract alone cannot be completed in time.
  Abort and print: `JOB i` — where **i** (1-indexed) is the ID of such a contract.

- **Rejection Rule B (Vehicle Saturation):** Because each vehicle operates sequentially, it requires an amount of time at least equal to the sum of all its assigned durations. If the aggregate duration for Phase 1 strictly exceeds **T**, or if the aggregate duration for Phase 2 strictly exceeds **T**, the deadline is unachievable.
  Abort and print: `LOAD c` — where **c** is 1 or 2, representing the phase whose total duration exceeds **T**.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the durations of the contract on Phase 1 and Phase 2, respectively.

## Output

Print a single line containing the rejection code: `JOB i` (for a contract whose p1 + p2 exceeds T) or `LOAD c` (for a phase c whose total duration exceeds T).

## Examples

### Example 1

**Input**
```
3 100
70 60
2 2
3 4
```

**Output**
```
JOB 1
```

### Example 2

**Input**
```
4 150
50 1
50 1
50 1
50 1
```

**Output**
```
LOAD 1
```

## Note

In Example 1, contract 1 requires 70 + 60 = 130 hours in succession. Since 130 > 100, `JOB 1` triggers Rejection Rule A. 
In Example 2, no individual contract exceeds 150 hours. However, Phase 1 must accommodate 50+50+50+50 = 200 hours of operations in total. Since 200 > 150, `LOAD 1` triggers Rejection Rule B.
