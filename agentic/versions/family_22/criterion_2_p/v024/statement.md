# Cold Start Protocol

Time limit: 2 s
Memory limit: 256 MB

## Description
A cold boot protocol requires executing $n$ distinct hardware initialization procedures exactly once. The protocol includes $m$ electrical safety requirements. Each requirement dictates that a specific procedure must fully complete before another specific procedure is allowed to start. 

The computer's single diagnostic core cannot multitask, so the execution log must be a strict linear sequence of all $n$ procedures. Generate a complete sequence that honors every safety requirement, or report if the requirements create a paradox that makes a safe boot impossible.

## Input
The first line contains two integers $n$ and $m$. The procedures are numbered from $1$ to $n$.
Each of the following $m$ lines contains two integers $a$ and $b$, indicating that procedure $a$ must be executed before procedure $b$.

## Output
If a safe execution sequence is possible, print `YES`, followed by a space-separated sequence of $n$ integers representing a valid order of procedures. If multiple valid sequences exist, any of them will be accepted.
If no such sequence is possible, print `NO`.

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
