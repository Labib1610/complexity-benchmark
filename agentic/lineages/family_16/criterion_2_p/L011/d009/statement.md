# Problem B — Signal Amplifiers

Time limit: 1 s   Memory limit: 256 MB

## Description

You are designing a transmission line by stringing together $j$ signal amplifiers. Each amplifier has a degradation parameter $p_1$ and a boost parameter $p_2$.

When a signal passes through an amplifier, its strength is modified in two steps:
1. The signal strength drops by $p_1$. However, the signal strength cannot be negative, so if it would drop below zero, it becomes exactly zero.
2. The signal is then boosted, increasing its strength by $p_2$.

Formally, if the signal strength before entering an amplifier is $S$, the strength after exiting the amplifier becomes $\max(S - p_1, 0) + p_2$.

The transmission line starts with an initial signal strength of 0. The signal passes through all $j$ amplifiers one by one in the exact order you choose.

Let $S_{final}$ be the final signal strength after exiting the last amplifier in your sequence. Let $D$ be the sum of the degradation parameters $p_1$ of all $j$ amplifiers. (Note that $D$ is a constant independent of the order).

You must choose an ordering of the $j$ amplifiers that minimizes the value of $S_{final} + D$.

What is the minimum possible value of $S_{final} + D$?

## Input

The first line contains a single integer $j$ ($1 \le j \le 200000$).
Each of the following $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$), representing the degradation and boost parameters of an amplifier, respectively.

## Output

Print a single integer: the minimum possible value of $S_{final} + D$.

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

In Example 1, one optimal sequence is to order the input amplifiers as: the 3rd amplifier, then the 2nd amplifier, then the 1st amplifier.
- The initial signal strength is $S_0 = 0$.
- Pass through the 3rd amplifier (input line 3: $p_1 = 1, p_2 = 3$): 
  $S_1 = \max(0 - 1, 0) + 3 = 3$.
- Pass through the 2nd amplifier (input line 2: $p_1 = 2, p_2 = 4$): 
  $S_2 = \max(3 - 2, 0) + 4 = 1 + 4 = 5$.
- Pass through the 1st amplifier (input line 1: $p_1 = 3, p_2 = 2$): 
  $S_3 = \max(5 - 3, 0) + 2 = 2 + 2 = 4$.

The final signal strength is $S_{final} = 4$.
The sum of all degradation parameters is $D = 3 + 2 + 1 = 6$.
The value to output is $S_{final} + D = 4 + 6 = 10$.
This is the minimum possible value across all valid sequences.