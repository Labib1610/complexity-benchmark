# Two-Stage Manufacturing Analyzer

Time limit: 2 s
Memory limit: 256 MB

## Description

You are developing a scheduling analyzer for a two-stage manufacturing plant. The plant must process a batch of $j$ items. Every item requires sequential processing: it must first be machined on Unit 1, and subsequently polished on Unit 2. Each unit can process at most one item at any given moment. An item cannot commence polishing on Unit 2 until its machining on Unit 1 is entirely complete.

The factory operates under a strict deadline $T$. A complete schedule assigns a start time $s_{i,1}$ on Unit 1 and a start time $s_{i,2}$ on Unit 2 for every item $i$, such that:
- $s_{i,1} \ge 0$
- $s_{i,2} \ge s_{i,1} + p_{i,1}$
- $s_{i,2} + p_{i,2} \le T$
- For any two distinct items $i$ and $k$, either $s_{i,1} + p_{i,1} \le s_{k,1}$ or $s_{k,1} + p_{k,1} \le s_{i,1}$
- For any two distinct items $i$ and $k$, either $s_{i,2} + p_{i,2} \le s_{k,2}$ or $s_{k,2} + p_{k,2} \le s_{i,2}$

Finding a valid schedule requires navigating a search space of $(j!)^2$ possible ordering combinations, exploring different permutations of item processing on both units to minimize idle time and meet the deadline. 

In this specific deployment, your analyzer functions as a preliminary filter to catch batches that are structurally impossible to schedule. You are guaranteed that for every provided batch, no valid schedule exists, and the impossibility is caused by exactly one of two overt violations. Either there is exactly one specific item $i$ whose own sequential processing time $p_{i,1} + p_{i,2}$ strictly exceeds $T$, or there is exactly one specific unit $c \in \{1, 2\}$ whose total active processing time for the entire batch strictly exceeds $T$.

Your program must output the exact cause of this structural impossibility. If an individual item $i$ (1-indexed) cannot complete within $T$ even in isolation, output `JOB i`. If a unit $c$ requires more total processing time than $T$, output `LOAD c`. 

## Input

The first line contains two integers $j$ and $T$ (1 ≤ $j$ ≤ 200,000, 1 ≤ $T$ ≤ 1,000,000,000).
Each of the next $j$ lines contains two integers $p_{i,1}$ and $p_{i,2}$ (1 ≤ $p_{i,1}, p_{i,2}$ ≤ 1,000,000), representing the necessary processing times of item $i$ on Unit 1 and Unit 2.

## Output

Print a single line containing either `JOB i` (where $i$ is the 1-based index of the item whose total time exceeds $T$) or `LOAD c` (where $c$ is the unit experiencing an excessive load).

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
