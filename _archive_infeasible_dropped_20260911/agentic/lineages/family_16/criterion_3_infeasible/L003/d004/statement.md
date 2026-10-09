# Problem C — Impossible Deadline: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

You are given a system of temporal constraints over a set of **j** entities. The system features exactly 2 sequential domains, numbered 1 and 2. 
Each entity $i$ (for $1 \le i \le j$) has a required span $p_{i,1}$ in domain 1 and $p_{i,2}$ in domain 2.

We define the start and end times for each entity $i$ in each domain $c \in \{1, 2\}$ as non-negative real numbers $S_{i,c}$ and $E_{i,c}$.
A valid assignment must satisfy all of the following rules:
- **Span constraint:** $E_{i,c} \ge S_{i,c} + p_{i,c}$ for all $i$ and all $c$.
- **Sequential domain constraint:** $S_{i,2} \ge E_{i,1}$ for all $i$.
- **Non-overlap constraint:** For a given domain $c$, no two entities can overlap in time. For any $i \neq k$, either $S_{i,c} \ge E_{k,c}$ or $S_{k,c} \ge E_{i,c}$.
- **Global deadline:** $E_{i,c} \le T$ for all $i$ and all $c$.

For every test input, it is guaranteed that no valid assignment exists. Your task is to output a short certificate that proves the system is contradictory. For every test input, exactly one of these certificate types is guaranteed to apply. Print the one that holds:

* `JOB i` (where **i** is a 1-based index): The constraints restricted only to entity **i** across both domains (Span, Sequential, Non-negative starts, and Global deadline) are already contradictory.
* `LOAD c` (where **c** is either 1 or 2): The constraints restricted only to domain **c** across all entities (Span, Non-overlap, Non-negative starts, and Global deadline) are already contradictory.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the spans of entity $i$ in domain 1 and domain 2.

## Output

Print a single line containing either `JOB i` (where the isolated constraints for entity **i** prove the deadline is impossible) or `LOAD c` (where **c** is either 1 or 2, and the isolated constraints for domain **c** prove the deadline is impossible).

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

In Example 1, `JOB 1` is the certificate because for entity 1, the span and sequential constraints require $E_{1,2} \ge S_{1,2} + 60 \ge E_{1,1} + 60 \ge S_{1,1} + 70 + 60 \ge 130$. Since $S_{1,1} \ge 0$, $E_{1,2} \ge 130$, which contradicts the global deadline $E_{1,2} \le 100$.
In Example 2, `LOAD 1` is the certificate because domain 1 has 4 entities each with span 50. The non-overlap and span constraints require the maximum $E_{i,1}$ to be at least $4 \times 50 = 200$, which contradicts the global deadline $E_{i,1} \le 150$.