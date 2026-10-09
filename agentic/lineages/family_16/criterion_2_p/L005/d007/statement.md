# Problem B — Signal Interference

Time limit: 1 s   Memory limit: 256 MB

## Description

A network of **j** signal processors must be arranged into a strict linear sequence, determining exactly which processor is placed first, second, and so on.

Each processor has an activation delay, **t1**, and a decay delay, **t2**.

When processing a signal, the sequence experiences varying levels of interference. The system's *base latency* is defined as the sum of the decay delays of all **j** processors in the sequence.

To evaluate the stability of your chosen sequence, you must calculate the *interference spike* at every position $k$ (where $k$ ranges from $1$ to $j$). For a specific position $k$, its interference spike is computed by taking:
- The *base latency* of the entire sequence,
- PLUS the sum of the activation delays of all processors from position $1$ up to position $k$ (inclusive),
- MINUS the sum of the decay delays of all processors from position $1$ up to position $k-1$ (inclusive). (If $k=1$, this subtracted sum is $0$).

The *peak interference* of the entire sequence is the maximum interference spike observed across all $j$ possible positions $k$.

Your task is to determine the optimal sequence of the processors that minimizes this overall *peak interference*.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains exactly 2 integers **t1** and **t2** (1 ≤ t1, t2 ≤ 1000000): the activation delay and the decay delay of a processor.

## Output

Print a single integer: the smallest possible *peak interference* you can achieve by optimally sequencing the processors.

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

In Example 2, there is only one processor ($j=1$). The only possible position to evaluate is $k=1$. The base latency is the sum of all decay delays, which is 3. The interference spike for $k=1$ is the base latency (3) plus the activation delay of the first processor (5) minus the decay delays before position 1 (0). The peak interference is therefore 3 + 5 - 0 = 8.