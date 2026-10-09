# Problem C — Impossible Allocations: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A discrete scheduler is attempting to construct a valid allocation of time slots. Let $j$ be the number of required tasks. For each task $i \in \{1 \dots j\}$, the scheduler must construct two sets of integers, $S_{i,1}$ and $S_{i,2}$, representing time slot allocations on Core 1 and Core 2 respectively.

The input specifies the exact number of distinct time slots each set must contain: the cardinality of $S_{i,1}$ must be exactly $p_{i,1}$, and the cardinality of $S_{i,2}$ must be exactly $p_{i,2}$.

The constructed sets must strictly satisfy three constraints:
1. **Window Bounding:** For all $i \in \{1 \dots j\}$ and $c \in \{1, 2\}$, every integer in the set $S_{i,c}$ must be chosen from the discrete interval of available slots $[1, T]$.
2. **Strict Supremum Precedence:** For every task $i$, all allocated slots on Core 1 must strictly precede all allocated slots on Core 2. Mathematically, the maximum integer in $S_{i,1}$ must be strictly less than the minimum integer in $S_{i,2}$.
3. **Core Exclusivity:** For a fixed core $c$ (where $c \in \{1, 2\}$), the core cannot process multiple tasks simultaneously. Therefore, for any distinct tasks $i \neq m$, the intersection of set $S_{i,c}$ and set $S_{m,c}$ must be empty.

You are analyzing logs from failed systems where a valid complete assignment of these sets is mathematically impossible. For every provided test case, exactly one of the following isolated conditions is inherently impossible to satisfy. Output the code for the one that applies:
- `JOB i` — It is mathematically impossible to find valid sets $S_{i,1}$ and $S_{i,2}$ for task **i** (1-indexed) that simultaneously satisfy Window Bounding and Strict Supremum Precedence, even if we completely ignore Core Exclusivity and all other tasks.
- `LOAD c` — It is mathematically impossible to find sets $S_{1,c}, \dots, S_{j,c}$ for core **c** (where **c** $\in \{1, 2\}$) that simultaneously satisfy Window Bounding and Core Exclusivity, even if we completely ignore Strict Supremum Precedence and the other core.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the following **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the required set cardinalities $p_{i,1}$ and $p_{i,2}$ for the first and second core allocations of the task, respectively.

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