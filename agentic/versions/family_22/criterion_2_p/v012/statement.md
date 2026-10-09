# Problem B — Sequencing the Batch on One Station

Time limit: 2 s   Memory limit: 256 MB

## Description
A single manufacturing station must process a batch of $n$ distinct operations, numbered 1 to $n$. The station can only execute one operation at a time, so the entire batch must be arranged into a single, continuous sequence from the first operation to the last.

You are given a list of $m$ manufacturing constraints. Each constraint specifies two operations, $a$ and $b$, and dictates that operation $a$ must be fully completed at some point in the sequence before operation $b$ is allowed to start. 

Your objective is to determine a complete sequence of all $n$ operations that satisfies every given constraint. In some cases, the constraints might inherently contradict one another, making it impossible to schedule all operations without breaking a rule. If no such sequence exists, you must state that it is impossible. Any sequence that includes all $n$ operations exactly once and breaks no constraints is acceptable.

## Input
The first line contains two integers $n$ and $m$, representing the number of operations and the number of constraints, respectively. 
Each of the following $m$ lines contains two integers $a$ and $b$, indicating that operation $a$ must occur before operation $b$ in the sequence.

## Output
Print `YES` then a permutation of 1 to $n$ (separated by spaces) representing a valid processing order; otherwise, print `NO`. If there are multiple valid sequences, any of them will be accepted.

## Example 1

**Input:**
```
4 4
1 2
1 3
2 4
3 4
```

**Output:**
```
YES
1 2 3 4
```

## Example 2

**Input:**
```
3 3
1 2
2 3
3 1
```

**Output:**
```
NO
```
