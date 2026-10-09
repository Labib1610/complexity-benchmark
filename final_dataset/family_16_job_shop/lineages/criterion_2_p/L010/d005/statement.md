# Problem B — Structural Bracket Assembly

Time limit: 1 s   Memory limit: 256 MB

## Description

You are assembling a batch of $j$ structural brackets along a single-axis rail system. You must arrange the $j$ given brackets into a single sequence $B_1, B_2, \dots, B_j$ (a permutation of the given brackets).

Each bracket has an Alpha span $d_1$ and a Beta span $d_2$. Let $d_1(B_k)$ and $d_2(B_k)$ denote the respective spans for the bracket placed at position $k$ in your sequence.

The rail system consists of two parallel tracks: an Alpha track and a Beta track. For your chosen sequence, each bracket $B_k$ ($1 \le k \le j$) must be assigned a footprint on both tracks:
- An **Alpha footprint** on the Alpha track, which is a continuous segment of length equal to its Alpha span $d_1(B_k)$.
- A **Beta footprint** on the Beta track, which is a continuous segment of length equal to its Beta span $d_2(B_k)$.

To ensure structural integrity, the layout of these footprints must satisfy the following geometric rules:
- **Alpha Track Ordering:** For any two adjacent brackets $B_k$ and $B_{k+1}$ in your sequence ($1 \le k < j$), the Alpha footprint of $B_{k+1}$ must be placed entirely to the right of the Alpha footprint of $B_k$. This means the starting coordinate of $B_{k+1}$'s Alpha footprint must be greater than or equal to the ending coordinate of $B_k$'s Alpha footprint.
- **Beta Track Ordering:** For any two adjacent brackets $B_k$ and $B_{k+1}$ in your sequence ($1 \le k < j$), the Beta footprint of $B_{k+1}$ must be placed entirely to the right of the Beta footprint of $B_k$. This means the starting coordinate of $B_{k+1}$'s Beta footprint must be greater than or equal to the ending coordinate of $B_k$'s Beta footprint.
- **Internal Bracket Dependency:** For every bracket $B_k$ in your sequence ($1 \le k \le j$), its Beta footprint must be placed entirely to the right of its own Alpha footprint. This means the starting coordinate of $B_k$'s Beta footprint must be greater than or equal to the ending coordinate of $B_k$'s Alpha footprint.

Assume both tracks begin at coordinate 0, meaning no footprint can extend into negative coordinates. Your goal is to find a sequence of the $j$ brackets and a valid layout of all their footprints that minimizes the rightmost coordinate reached by the final bracket's Beta footprint. Report this smallest possible rightmost coordinate.

Note: The answer may exceed the range of a 32-bit signed integer.

## Input

The first line contains a single integer $j$ ($1 \le j \le 200000$).
Each of the next $j$ lines contains two integers $d_1$ and $d_2$ ($1 \le d_1, d_2 \le 1000000$): the Alpha and Beta spans of a bracket.

## Output

Print a single integer: the smallest possible rightmost coordinate reached by the final bracket's Beta footprint.

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

In Example 2, there is only one bracket with $d_1 = 5$ and $d_2 = 3$. We can start its Alpha footprint at coordinate 0, so it occupies the Alpha track from 0 to 5. The Internal Bracket Dependency requires the Beta footprint to start at or after coordinate 5. We can start the Beta footprint at coordinate 5, occupying the Beta track from 5 to 8. The rightmost coordinate reached by the Beta footprint is 8, which is the minimum possible.