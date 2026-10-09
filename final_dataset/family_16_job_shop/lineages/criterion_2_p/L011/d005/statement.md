# Problem B — Batch Processing Pipeline

Time limit: 1 s   Memory limit: 256 MB

## Description

You are managing a data processing pipeline that must process **j** distinct batches of data. Each batch requires a specific processing time in Phase A, followed by a specific processing time in Phase B. 

You must establish a single processing sequence (an ordering of the **j** batches). Both Phase A and Phase B will process the batches in this exact same order.

For your chosen sequence, let $X_i$ be the Phase A processing time of the $i$-th batch, and $Y_i$ be its Phase B processing time (where $1 \le i \le j$). 
The schedule is determined by calculating the Phase B start time, $S_i$, for each batch $i$, according to these rules:
1. The first batch begins Phase B immediately after it finishes Phase A: 
   $S_1 = X_1$
2. For every subsequent batch $i > 1$, it cannot begin Phase B until the previous batch has finished Phase B: 
   $S_i \ge S_{i-1} + Y_{i-1}$
3. For every subsequent batch $i > 1$, it also cannot begin Phase B until it has completely finished Phase A. Since Phase A runs continuously from time 0, this means: 
   $S_i \ge \sum_{k=1}^i X_k$
4. Each $S_i$ takes the minimum possible value that satisfies the above conditions.

The final batch concludes in Phase B at time $T = S_j + Y_j$. 
Interestingly, it can be mathematically proven that for any chosen sequence, the final completion time $T$ is strictly equivalent to:
$$T = \max_{1 \le k \le j} \left( \sum_{i=1}^k X_i + \sum_{i=k}^j Y_i \right)$$

Your task is to find an ordering of the **j** batches that minimizes the final completion time $T$.

What is the minimum possible value of $T$?

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the following **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000), representing the processing time the batch requires in Phase A and Phase B, respectively.

## Output

Print a single integer: the minimum possible value of $T$.

## Examples

### Example 1

**Input**
```
3
3 2
2 4
1 3
```

**Output**
```
10
```

### Example 2

**Input**
```
1
5 3
```

**Output**
```
8
```

### Example 3

**Input**
```
3
2 2
2 2
2 2
```

**Output**
```
8
```

## Note

In Example 1, if we order the batches as the 3rd batch, then the 2nd batch, then the 1st batch from the input:
The sequence of Phase A times is $X = [1, 2, 3]$ and Phase B times is $Y = [3, 4, 2]$.
Using the equivalent formula for $T$:
- For $k=1$: $(1) + (3+4+2) = 1 + 9 = 10$
- For $k=2$: $(1+2) + (4+2) = 3 + 6 = 9$
- For $k=3$: $(1+2+3) + (2) = 6 + 2 = 8$
The maximum of these values is $T = \max(10, 9, 8) = 10$.
This is the minimum possible final completion time across all valid orderings.

In Example 2, there is only one batch. According to the rules, $S_1 = X_1 = 5$. It concludes at time $T = S_1 + Y_1 = 5 + 3 = 8$. (Equivalently, for $k=1$, $T = 5 + 3 = 8$).