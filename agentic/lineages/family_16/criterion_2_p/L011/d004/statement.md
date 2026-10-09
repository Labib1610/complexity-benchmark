# Problem B — Festival Lineup

Time limit: 1 s   Memory limit: 256 MB

## Description

You are organizing a festival featuring **j** distinct performances. Each performance requires a specific duration on the Main Stage, and a specific duration in the Review Room.

You must establish a single lineup (an ordering of the **j** performances). Both the Main Stage and the Review Room will process the performances in this exact same order.

For your chosen lineup, let $A_i$ be the Main Stage duration of the $i$-th performance, and $B_i$ be its Review Room duration (where $1 \le i \le j$). 
The schedule is determined by calculating the Review Room start time, $S_i$, for each performance $i$, according to these rules:
1. The first performance begins in the Review Room immediately after it finishes on the Main Stage: 
   $S_1 = A_1$
2. For every subsequent performance $i > 1$, it cannot begin in the Review Room until the previous performance has finished its review: 
   $S_i \ge S_{i-1} + B_{i-1}$
3. For every subsequent performance $i > 1$, it also cannot begin in the Review Room until it has completely finished on the Main Stage. Since the Main Stage runs continuously from time 0, this means: 
   $S_i \ge \sum_{k=1}^i A_k$
4. Each $S_i$ takes the minimum possible value that satisfies the above conditions.

The final performance concludes in the Review Room at time $C = S_j + B_j$.
Your task is to find an ordering of the **j** performances that minimizes $C$.

What is the minimum possible value of $C$?

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the following **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000), representing the duration the performance requires on the Main Stage and in the Review Room, respectively.

## Output

Print a single integer: the minimum possible value of $C$.

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

In Example 2, there is only one performance. According to the rules, $S_1 = A_1 = 5$. It concludes at time $C = S_1 + B_1 = 5 + 3 = 8$.