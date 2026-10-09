# Problem C — Impossible Allocation: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A central server must synchronize $j$ active databases over a strict window of $T$ seconds. For each database $i$, the server must transmit exactly $p1_i$ Delta chunks and exactly $p2_i$ Snapshot chunks. 

The server's schedule is represented as a log of $T$ seconds. The server has one Delta channel and one Snapshot channel. This means:
- Across all databases, the server can send at most one Delta chunk per second.
- Across all databases, the server can send at most one Snapshot chunk per second.

Additionally, the server enforces a strict data consistency protocol. For a schedule to be valid, it must satisfy a tracking mechanism for every database. For each database $i \in \{1, \dots, j\}$, a phase tracker $V_i$ is initialized to $0$. During each second $k$ from $1$ to $T$ (in chronological order), the server updates $V_i$ via two sequential steps:
1. If second $k$ contains a Snapshot chunk for database $i$, $V_i$ is increased by $1$.
2. If second $k$ contains a Delta chunk for database $i$, $V_i$ is set to $0$.

A schedule is valid only if, for all databases $i$, the final value of $V_i$ after second $T$ is exactly $p2_i$.

Every provided configuration is mathematically impossible to complete—there is no valid way to construct the schedule to accommodate all required chunks while satisfying the phase tracker for all databases. Your task is to identify the bottleneck that proves the configuration is unachievable.

Exactly one of the following foundational requirements is broken. Output the applicable certificate:

- **Phase Violation:** For some database $i$, it is mathematically impossible to schedule its $p1_i$ Delta chunks and $p2_i$ Snapshot chunks within $T$ seconds such that its final tracker $V_i$ equals $p2_i$ (even if it were the only database on the server). Output `JOB i` (where $i$ is the 1-based index of the database).
- **Delta Saturation:** It is impossible to schedule all required Delta chunks for all $j$ databases within $T$ seconds. Output `LOAD 1`.
- **Snapshot Saturation:** It is impossible to schedule all required Snapshot chunks for all $j$ databases within $T$ seconds. Output `LOAD 2`.

You are guaranteed that exactly one of these requirements will be broken for the given input.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the required number of Delta chunks and Snapshot chunks respectively for database $i$ (i.e., $p1_i$ and $p2_i$).

## Output

Print a single line: `JOB i` (for a Phase Violation) or `LOAD c` (for a saturation failure, where **c** is 1 for Delta saturation or 2 for Snapshot saturation).

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

In Example 1, database 1 requires 70 Delta chunks and 60 Snapshot chunks. To achieve a final tracker $V_1 = 60$, none of the 60 Snapshot increments can be reset to 0 by a Delta chunk. This requires all 70 Delta chunks to be sent in seconds strictly before any of the 60 Snapshot chunks. Since $70 + 60 = 130 > 100$, this is impossible. Thus `JOB 1` is the correct proof of impossibility. 

In Example 2, no single database violates the phase tracker on its own. However, the sum of required Delta chunks across all 4 databases is 200. Since the server can only send 1 Delta chunk per second, it is impossible to schedule them all in $150$ seconds. Thus `LOAD 1` is the correct output.