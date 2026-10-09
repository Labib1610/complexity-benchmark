# Constraint Satisfaction over the Symmetric Group

Time limit: 2 s   Memory limit: 256 MB

## Description
You are tasked with solving a constraint satisfaction problem over the symmetric group $S_n$. A valid state is a linear sequence of $n$ distinct elements (a permutation of the integers $1$ through $n$). The state space contains $n!$ distinct permutations. Because of the factorial explosion of this state space, brute-force enumeration of all configurations is impossible for large $n$.

You must find a state that satisfies a system of $m$ asymmetric constraints. Each constraint is provided as an ordered pair $(a, b)$, which enforces the strict inequality requirement that element $a$ must appear at a smaller index than element $b$ in the sequence. 

Your objective is to evaluate this system of constraints and determine if there exists at least one sequence in the $n!$ search space that satisfies all $m$ conditions simultaneously. If the system is satisfiable, you must output a valid sequence. If the constraints are mutually contradictory, making the system unsatisfiable, you must report that no solution exists.

## Input
The first line contains two integers $n$ and $m$, representing the number of elements and the number of asymmetric constraints.
Each of the following $m$ lines contains two integers $a$ and $b$ ($1 \le a, b \le n$), representing a constraint where element $a$ must appear before element $b$ in the sequence.

## Output
If a satisfying sequence exists, print `YES` on the first line, followed by a space-separated sequence of the $n$ elements on the second line. If multiple valid sequences exist in the state space, any one of them will be accepted.
If no satisfying sequence exists, print `NO`.

## Example 1

### Input
```text
4 4
1 2
1 3
2 4
3 4
```

### Output
```text
YES
1 2 3 4
```

## Example 2

### Input
```text
3 3
1 2
2 3
3 1
```

### Output
```text
NO
```
