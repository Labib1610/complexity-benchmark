# Problem B — Structural Bracket Assembly

Time limit: 1 s   Memory limit: 256 MB

## Description

You are assembling a batch of $j$ structural brackets along a single-axis rail system. You must arrange the $j$ given brackets into a single sequence $B_1, B_2, \dots, B_j$ (a permutation of the given brackets).

Each bracket has an Alpha span $d_1$ and a Beta span $d_2$. Let $d_1(B_k)$ and $d_2(B_k)$ denote the respective spans for the bracket placed at position $k$ in your sequence.

The rail system consists of two parallel tracks: an Alpha track and a Beta track. For your chosen sequence, each bracket $B_k$ ($1 \le k \le j$) must be assigned a footprint on both tracks:
- An **Alpha footprint** on the Alpha track, which is a continuous segment of length exactly $d_1(B_k)$, starting at coordinate $X_k$ and ending at $X_k + d_1(B_k)$.
- A **Beta footprint** on the Beta track, which is a continuous segment of length exactly $d_2(B_k)$, starting at coordinate $Y_k$ and ending at $Y_k + d_2(B_k)$.

To ensure structural integrity, the layout of these footprints must satisfy the following geometric displacement rules:
- **Alpha Track Ordering:** For any two adjacent brackets $B_k$ and $B_{k+1}$ in your sequence ($1 \le k < j$), the coordinate displacement $X_{k+1} - X_k$ must be at least $d_1(B_k)$.
- **Beta Track Ordering:** For any two adjacent brackets $B_k$ and $B_{k+1}$ in your sequence ($1 \le k < j$), the coordinate displacement $Y_{k+1} - Y_k$ must be at least $d_2(B_k)$.
- **Internal Bracket Dependency:** For every bracket $B_k$ in your sequence ($1 \le k \le j$), the cross-track displacement $Y_k - X_k$ must be at least $d_1(B_k)$.

Assume both tracks begin at coordinate 0, meaning $X_1 \ge 0$ and $Y_1 \ge 0$. Your goal is to find a sequence of the $j$ brackets and a valid layout of all their footprints (the exact coordinates $X_k$ and $Y_k$) that minimizes the rightmost coordinate reached by the final bracket's Beta footprint. Report this smallest possible rightmost coordinate (which is the minimum possible value of $Y_j + d_2(B_j)$).

*Note on layout geometry:* It is a known algebraic property of this system that for any fixed sequence $B_1, \dots, B_j$, if you pack the footprints as tightly as possible toward coordinate 0, the rightmost coordinate reached by the final bracket's Beta footprint is exactly equal to:
$$ \max_{1 \le k \le j} \left( \sum_{i=1}^k d_1(B_i) + \sum_{i=k}^j d_2(B_i) \right) $$

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

In Example 2, there is only one bracket with $d_1 = 5$ and $d_2 = 3$. We can start its Alpha footprint at coordinate $X_1 = 0$, so it occupies the Alpha track from 0 to 5. The Internal Bracket Dependency requires the cross-track displacement $Y_1 - X_1 \ge 5$, meaning $Y_1 \ge 5$. We can start the Beta footprint at coordinate $Y_1 = 5$, occupying the Beta track from 5 to 8. The rightmost coordinate reached by the Beta footprint is $Y_1 + d_2 = 8$, which is the minimum possible. The geometric formula also confirms $\max_{k=1}^1 (5 + 3) = 8$.