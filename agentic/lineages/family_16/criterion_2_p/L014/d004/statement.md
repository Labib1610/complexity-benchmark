# Problem B — Two-Segment Processing

Time limit: 1 s
Memory limit: 256 MB

## Description

An encryption module must process **j** data blocks. The processing pipeline consists of exactly 2 segments: a substitution phase followed by a transposition phase. Each block requires **p1** microseconds to traverse the substitution phase, and **p2** microseconds to traverse the transposition phase.

You must choose a single sequence in which to process all **j** blocks. Both segments process the blocks in this exact chosen permutation. Each segment handles at most one block at a time. Every block must completely finish the substitution phase before it can begin the transposition phase. Once a segment begins processing a block, it processes it continuously without interruption.

Your objective is to determine the optimal permutation that minimizes the time at which the final block completely finishes the transposition phase. Report this minimum possible completion time.

*Note: The operational rules guarantee that the substitution phase never idles once it starts. Consequently, the completion time of the final block on the transposition phase can be equivalently calculated by analyzing crossover points. For any chosen sequence, a crossover point $k$ ($1 \le k \le j$) yields a duration equal to the total substitution time of all blocks from $1$ to $k$, plus the total transposition time of all blocks from $k$ to $j$. The final completion time is exactly the maximum duration among all possible crossover points $1 \le k \le j$. You are seeking the sequence that minimizes this maximum duration.*

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the substitution time and the transposition time of a block.

## Output

Print a single integer: the smallest possible time at which all blocks are complete.

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

In Example 2, there is only one block. The substitution phase takes it at time 0 and finishes at time 5. The transposition phase immediately takes it and finishes at time 5 + 3 = 8.