# Variable Equivalence Verification

Time limit: 2 s   Memory limit: 256 MB

## Description

A formal verification system tracks $n$ variables. Exactly $t$ of these variables are designated as **Target Variables**.

The system has a database of $m$ equality assertions, each stating that two specific variables are equal. The set of available assertions covers the entire system such that the equality of any two variables can be deduced. To minimize redundancy, the database contains exactly $m = n - 1$ assertions, ensuring there are no alternative deduction chains between any pair of variables.

Each assertion requires a specific computational cost to verify. You must select a subset of these assertions to verify. In the logical framework containing only your verified assertions, all $t$ Target Variables must be proven equal to each other (meaning equality can be deduced between any two Target Variables, possibly using other intermediate variables through transitivity). Assertions that are not verified cannot be used in deductions.

Your objective is to determine the minimum total verification cost required to select a valid subset of assertions that proves all Target Variables are equal.

## Input

The first line contains three integers: $n$, $m$, and $t$.
- $n$ is the total number of variables. The system contains at least 1 variable and at most 200000.
- $m$ is the number of available assertions, which is exactly $n - 1$.
- $t$ is the number of Target Variables, which is at least 1 and at most $n$.

The second line contains $t$ distinct integers: the identifiers of the Target Variables (from 1 to $n$).

Each of the next $m$ lines details an available assertion with three integers: $u$, $v$, and $w$.
- $u$ and $v$ are distinct variable identifiers (from 1 to $n$) linked by the assertion.
- $w$ is the computational cost required to verify this assertion. This cost is a positive integer not exceeding 1000000.

These $m$ lines form the exact logical structure described above, guaranteeing a single deduction chain between any two variables.

## Output

Print a single integer: the minimum total verification cost required to prove all Target Variables equal using only the selected assertions.

## Examples

### Example 1

**Input**
```
4 3 2
1 4
1 2 5
2 3 1
3 4 2
```

**Output**
```
8
```

### Example 2

**Input**
```
5 4 1
3
1 2 4
2 3 6
3 4 2
4 5 9
```

**Output**
```
0
```

### Example 3

**Input**
```
3 2 3
1 2 3
1 2 4
2 3 5
```

**Output**
```
9
```

## Note

In Example 1, the Target Variables 1 and 4 can only be proven equal by chaining the equalities through variables 2 and 3, so all three assertions (5 + 1 + 2 = 8) must be verified. In Example 2, there is only one Target Variable. With only one required variable, no assertions are needed to prove it equal to itself, so the minimum cost is 0.