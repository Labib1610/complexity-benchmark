# Problem B — Freight Depot Inspections

Time limit: 1 s   Memory limit: 256 MB

## Description

You are managing a freight depot that must dispatch exactly **j** cargo trains. Each train must undergo exactly **two** sequential security checks: a Structural inspection, followed by a Cargo clearance.

You must establish a single dispatch sequence (a permutation of the **j** trains). Both security teams will process the trains in this **exact same chosen order**. 

The inspection timeline is governed by the following physical constraints:
- There are exactly two security teams (Structural and Cargo), and each team can inspect only one train at a time.
- Every train must fully complete its Structural inspection before it can begin its Cargo clearance.
- The Structural team inspects the trains continuously without interruption, starting at timestamp 0.
- The Cargo team begins inspecting each train at the earliest possible timestamp that satisfies all above conditions.

Formally, if we let $s_k$ and $c_k$ be the Structural and Cargo duration times of the $k$-th train in your chosen sequence, the completion timestamps are defined as follows:
- The Structural team's completion time for the $k$-th train is $A_k = A_{k-1} + s_k$, with $A_0 = 0$.
- The Cargo team's completion time for the $k$-th train is $B_k = \max(A_k, B_{k-1}) + c_k$, with $B_0 = 0$.

Your objective is to find an ordering of the **j** trains that minimizes the final completion timestamp—specifically, the time $B_j$ when the Cargo team finishes the last train in your sequence.

What is the minimum possible value of $B_j$?

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the following **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000), representing the time required for a train's Structural inspection and Cargo clearance, respectively.

## Output

Print a single integer: the minimum possible completion timestamp of the final Cargo clearance.

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

In Example 1, if we order the trains as the 3rd train, then the 2nd train, then the 1st train from the input:
- For the first train in sequence (input train 3): $s_1 = 1$, $c_1 = 3$. 
  $A_1 = 0 + 1 = 1$. 
  $B_1 = \max(1, 0) + 3 = 4$.
- For the second train in sequence (input train 2): $s_2 = 2$, $c_2 = 4$. 
  $A_2 = 1 + 2 = 3$. 
  $B_2 = \max(3, 4) + 4 = 8$.
- For the third train in sequence (input train 1): $s_3 = 3$, $c_3 = 2$. 
  $A_3 = 3 + 3 = 6$. 
  $B_3 = \max(6, 8) + 2 = 10$.

The final completion timestamp $B_3$ is 10. This is the minimum possible value across all valid orderings.

In Example 2, there is exactly one train. $A_1 = 5$, and $B_1 = \max(5, 0) + 3 = 8$.