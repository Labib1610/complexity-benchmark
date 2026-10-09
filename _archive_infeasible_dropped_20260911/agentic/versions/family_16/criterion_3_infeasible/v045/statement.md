# Problem C — Production Line Pre-Check

Time limit: 2 s
Memory limit: 256 MB

## Description

A manufacturing facility processes $j$ items through two sequential stages. Every item must first complete Stage 1, and only after it finishes can it begin Stage 2. You are given the duration each item requires at Stage 1 and Stage 2. A stage can only process a single item at any given moment.

The facility operates under a strict deadline: all items must be completely finished by time $T$.

An automated pre-check analyzes the production requirements to determine why the deadline cannot be met. The provided input will always contain exactly one of the following baseline impossibilities. Your task is to identify and report it:

- `JOB i` — Item $i$ (1-based index) could not possibly finish by the deadline even if it were the only item in the entire facility.
- `LOAD c` — Stage $c$ (where $c \in \{1, 2\}$) has been assigned so much work that it would fail to finish by time $T$ even if it could operate continuously from time zero without ever waiting for items.

## Input

The first line provides two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
The following $j$ lines each contain two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$), representing the durations required by the item at Stage 1 and Stage 2, respectively.

## Output

Print a single line containing either `JOB i` or `LOAD c`, corresponding to the impossibility found in the input.

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

In the first example, the first item requires 70 units of time in Stage 1 and 60 units in Stage 2. It would take 130 units of time to finish on its own, which misses the 100-unit deadline. Thus, `JOB 1` is the correct output.

In the second example, no individual item takes too long on its own. However, Stage 1 must be active for a total of 50 + 50 + 50 + 50 = 200 units of time. Since this exceeds the 150-unit deadline, `LOAD 1` is the correct output.
