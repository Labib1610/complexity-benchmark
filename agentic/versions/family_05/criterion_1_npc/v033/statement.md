# Problem A — Crew Assembly

Time limit: 5 s   Memory limit: 256 MB

## Description

A project must assemble **k** complete work crews. The project requires components of three different categories:

- specialists, numbered 1..k,
- machines, numbered 1..k,
- time slots, numbered 1..k.

A crew is formed by combining exactly one specialist, one machine, and one time slot. Only certain configurations work together; you are given a list of allowed combinations `(x, y, z)`.

Select exactly **k** allowed combinations to form the crews. Your selection is valid if and only if no two chosen crews share the same specialist, the same machine, or the same time slot. 

Determine whether this is possible, and if so report one valid set of crews.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the group size and the number of allowed combinations.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), an allowed combination. No combination is listed more than once.

## Output

If a valid selection of **k** crews exists, print `YES` on the first line, then print **k** lines, each containing the three members `x y z` of one chosen crew. Any selection following the non-sharing rule is accepted; the crews may be printed in any order.

If no valid selection exists, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 2 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 1 2
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```

## Note

In Example 2, both allowed combinations use machine 1. Since chosen crews cannot share a machine, at most one can be selected, making it impossible to assemble 2 crews.
