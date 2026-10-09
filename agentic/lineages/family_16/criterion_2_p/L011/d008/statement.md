# Problem B — Freight Depot Inspections

Time limit: 1 s   Memory limit: 256 MB

## Description

You are managing a freight depot that must dispatch exactly $j$ cargo trains. Each train must undergo exactly two sequential security checks: a Structural inspection, followed by a Cargo clearance.

You must establish a single dispatch sequence for the $j$ trains. Both security teams will process the trains in this exact same sequence.

For the $k$-th train in your chosen sequence, let its Structural inspection duration be $X_k$ and its Cargo clearance duration be $Y_k$. You must assign a Structural start time $t_k$ and a Cargo start time $u_k$ (both in minutes) to each train in your sequence such that the following physical constraints are satisfied:

- The Structural team begins working on the first train at minute 0: $t_1 = 0$.
- The Structural team processes the trains back-to-back without interruption: $t_{k+1} = t_k + X_k$ for all $1 \le k < j$.
- A train's Cargo clearance cannot begin until its own Structural inspection is fully complete: $u_k \ge t_k + X_k$ for all $1 \le k \le j$.
- The Cargo team can only process one train at a time, and must do so in the sequence you established: $u_{k+1} \ge u_k + Y_k$ for all $1 \le k < j$.

Your objective is to find an ordering of the $j$ trains, along with valid start times $t_k$ and $u_k$, that minimizes the completion minute of the final Cargo clearance, which is given by $u_j + Y_j$.

What is the minimum possible value of $u_j + Y_j$?

## Input

The first line contains a single integer $j$ ($1 \le j \le 200000$).
Each of the following $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$), representing the time required in minutes for a train's Structural inspection and Cargo clearance, respectively.

## Output

Print a single integer: the minimum possible completion minute of the final Cargo clearance.

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

In Example 1, one optimal sequence is to order the input trains as: the 3rd train, then the 2nd train, then the 1st train.
- For the first train in sequence (input train 3): $X_1 = 1$, $Y_1 = 3$. 
  Structural start $t_1 = 0$. Structural finishes at $0 + 1 = 1$. 
  Cargo start $u_1 \ge 1$. We can set $u_1 = 1$. Cargo finishes at $1 + 3 = 4$.
- For the second train in sequence (input train 2): $X_2 = 2$, $Y_2 = 4$. 
  Structural start $t_2 = 1$. Structural finishes at $1 + 2 = 3$. 
  Cargo start $u_2$ must be at least the Structural finish ($3$) and at least the previous Cargo finish ($4$). We set $u_2 = 4$. Cargo finishes at $4 + 4 = 8$.
- For the third train in sequence (input train 1): $X_3 = 3$, $Y_3 = 2$. 
  Structural start $t_3 = 3$. Structural finishes at $3 + 3 = 6$. 
  Cargo start $u_3$ must be at least the Structural finish ($6$) and at least the previous Cargo finish ($8$). We set $u_3 = 8$. Cargo finishes at $8 + 2 = 10$.

The final completion minute $u_3 + Y_3$ is 10. This is the minimum possible value across all valid sequences.