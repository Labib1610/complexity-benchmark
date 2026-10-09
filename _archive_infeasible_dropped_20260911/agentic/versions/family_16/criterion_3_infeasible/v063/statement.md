# Problem C — Impossible Deadline: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A batch of **j** operations must be routed through two consecutive processing nodes: Node 1 and Node 2. For each operation, you are given its required processing duration on Node 1 and Node 2. The pipeline operates strictly under these physical constraints:
- Node 2 cannot begin working on an operation until Node 1 has fully completed its work on that same operation.
- A node can never process more than one operation simultaneously.

The entire batch is subject to a strict timeout **T**: every operation must be completely finished with both nodes before **T** time units elapse.

For every input provided, it is **guaranteed that the timeout cannot be satisfied**, regardless of the sequence in which operations are scheduled. Your objective is not to find a valid schedule; it is to **prove** the timeout is impossible by providing a short diagnostic code that can be verified directly against the given durations.

The test data guarantees that exactly one of the following two diagnostic proofs will be valid. Output the one that holds:

- **Operation sequence violation:** Because an operation must pass through the nodes sequentially, its individual processing phases cannot overlap in time. If an operation's combined duration for Node 1 and Node 2 strictly exceeds **T**, that operation alone cannot finish before the timeout.
  Print: `JOB i` — where **i** (1-based) is such an operation.

- **Node saturation:** Because a node processes operations one at a time, it must be active for at least the sum of all durations requested of it. If the total duration required on Node 1 (or Node 2) strictly exceeds **T**, the timeout is impossible.
  Print: `LOAD c` — where **c** is 1 or 2, and the total required duration on Node **c** exceeds **T**.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the required processing durations of an operation on Node 1 and Node 2.

## Output

Print a single line: `JOB i` (an operation whose p1 + p2 exceeds T) or `LOAD c` (a node c whose total processing duration exceeds T).

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

In Example 1, operation 1 requires 70 + 60 = 130 > 100 consecutive time units, so `JOB 1` proves the timeout will be violated. In Example 2, no single operation exceeds 150 time units, but Node 1 must remain active for 50+50+50+50 = 200 > 150 units of work in total, so `LOAD 1` is the valid proof.
