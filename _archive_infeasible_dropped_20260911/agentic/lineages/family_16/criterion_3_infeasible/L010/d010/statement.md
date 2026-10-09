# Problem C — Impossible Schedule: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A factory must process $j$ orders within a strict shift of $T$ minutes. For each order $i$, the factory must perform exactly $p1_i$ minutes of assembly followed by exactly $p2_i$ minutes of painting. 

The factory has one assembly line and one painting line. This means:
- The assembly line can process at most one order at a time.
- The painting line can process at most one order at a time.
- For any given order, painting cannot begin until its assembly is entirely completed.

Every provided daily plan is mathematically impossible to complete—there is no valid way to schedule all orders such that they all finish within $T$ minutes. Your task is to identify the specific bottleneck that proves the plan is unachievable.

Exactly one of the following foundational limits is exceeded. Output the applicable certificate:

- **Sequential Violation:** For some order $i$, it is mathematically impossible to complete its assembly and its subsequent painting within the shift, even if it were the only order in the factory. Output `JOB i` (where $i$ is the 1-based index of the order).
- **Assembly Saturation:** The assembly line is assigned more total work than can be completed within the shift, regardless of the painting schedule. Output `LOAD 1`.
- **Painting Saturation:** The painting line is assigned more total work than can be completed within the shift, regardless of the assembly schedule. Output `LOAD 2`.

You are guaranteed that exactly one of these limits will be exceeded for the given input.

## Input

The first line contains two integers $j$ and $T$ (1 ≤ $j$ ≤ 200000, 1 ≤ $T$ ≤ 1000000000).
Each of the next $j$ lines contains two integers $p1$ and $p2$ (1 ≤ $p1, p2$ ≤ 1000000): the required minutes of assembly and painting respectively for order $i$ (i.e., $p1_i$ and $p2_i$).

## Output

Print a single line: `JOB i` (for a Sequential Violation) or `LOAD c` (for a saturation failure, where $c$ is 1 for Assembly saturation or 2 for Painting saturation).

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

In Example 1, Order 1 cannot be completed within the 100-minute shift because its sequential processing stages require more combined time than the shift allows. Even if it were the only order, it would miss the deadline. Thus `JOB 1` is the correct proof of impossibility. 

In Example 2, no single order violates the deadline on its own. However, the assembly line is assigned too much total work to finish within the 150-minute shift. Thus `LOAD 1` is the correct output.