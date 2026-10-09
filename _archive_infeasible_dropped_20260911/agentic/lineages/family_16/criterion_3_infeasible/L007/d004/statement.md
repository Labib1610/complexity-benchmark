# Problem C — Impossible Deadline: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A manufacturing facility processes **j** distinct items. The production of each item involves exactly two sequential stages: preparation at stage 1, and finishing at stage 2. Equipment at any stage can handle at most one item at any given moment.
The facility operates for a single shift of duration **T**. 

A schedule is an assignment of start times $S_{i,c} \ge 0$ for each item $i \in \{1 \dots j\}$ and stage $c \in \{1, 2\}$. A schedule is considered valid if it satisfies all of the following requirements:
1. **Shift limits:** Every task must complete by the end of the shift. For all $i$ and $c$, $S_{i,c} + p_{i,c} \le T$, where $p_{i,c}$ is the required duration.
2. **Sequential processing:** An item's stage 2 cannot begin until its stage 1 is fully complete. For all $i$, $S_{i,2} \ge S_{i,1} + p_{i,1}$.
3. **Equipment capacity:** A stage can process only one item at a time. For any fixed stage $c$, and any two distinct items $i$ and $k$, their active processing intervals $(S_{i,c}, S_{i,c} + p_{i,c})$ and $(S_{k,c}, S_{k,c} + p_{k,c})$ must not overlap. (Note: one interval may start at the exact moment another ends).

You are auditing logs from failed facilities. For every provided log, it is mathematically impossible to construct a valid schedule. Your objective is to generate a concise certificate that definitively proves this impossibility by identifying the localized bottleneck. You do not need to build a complex solver; the impossibility of these bottlenecks can be verified by checking simple bounds directly from the input durations.

It is guaranteed that for each log, exactly one of the following relaxed scenarios is also impossible to schedule. Output the code for the one that applies:
- `JOB i` — It is impossible to satisfy requirements 1 and 2 for the **i**-th item (1-indexed), even if we completely ignore the equipment capacity requirement (3) for all items, and ignore requirements 1 and 2 for all other items.
- `LOAD c` — It is impossible to satisfy requirements 1 and 3 for stage **c** (where **c** $\in \{1, 2\}$), even if we completely ignore the sequential processing requirement (2) for all items, and ignore requirements 1 and 3 for the other stage.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the following **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the duration required for the item at stage 1 and stage 2, respectively.

## Output

Print a single line containing the applicable certificate: either `JOB i` or `LOAD c`.

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