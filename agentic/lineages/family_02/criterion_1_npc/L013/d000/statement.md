# Problem A — Formulation Stability

Time limit: 2 s   Memory limit: 256 MB

## Description

A chemical formulation involves **n** possible additives, each of which the chemist must designate firmly as INCLUDED or EXCLUDED from the final mixture — no additive may be partially used, and there is no third state. Testing has produced **m** stability requirements gathered from separate lab trials; every requirement names three additive-references and passes precisely when **at least one** of the three named conditions is met (a condition names an additive together with the status — INCLUDED or EXCLUDED — that satisfies it). A requirement with a met condition imposes nothing further; a requirement with none of its three conditions met is violated. The same additive typically appears across many requirements, sometimes demanded INCLUDED by one and EXCLUDED by another, and the requirements may overlap heavily or barely at all — none of that matters except through the exact conditions each requirement lists. Decide whether there is a single global INCLUDED/EXCLUDED formulation of all n additives that satisfies **every** requirement simultaneously, and if so report one such formulation; otherwise the requirement set is over-constrained. Satisfying the requirements one at a time is trivial — the difficulty is one formulation consistent with all of them at once.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 90, 0 ≤ m ≤ 400).
Each of the next m lines contains three non-zero signed integers l1 l2 l3,
with |li| ≤ n. At least one of the three stated conditions must hold.

## Output
If no valid formulation exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers
s1 s2 … sn (each in {0, 1}), where si is the state of additive i. Any valid
formulation is accepted.

## Example 1
Input:
```
3 2
1 2 3
-1 2 -3
```
Output:
```
YES
0 0 1
```

## Example 2
Input:
```
1 2
1 1 1
-1 -1 -1
```
Output:
```
NO
```

## Note
Each requirement group has exactly three entries. The same additive index may appear
more than once in a group.
