# Problem A — Recipe Formulation

Time limit: 2 s   Memory limit: 256 MB

## Description

A master recipe involves **n** base ingredients, each of which the chef must set firmly to IN or OUT before the tasting — no ingredient may be left undecided, and there is no third state. Focus group testing has produced **m** reviewer demands gathered from separate tasting sessions; every demand names three ingredient-references and passes precisely when **at least one** of the three named conditions is met (a condition names an ingredient together with the status — IN or OUT — that satisfies it). A demand with a met condition imposes nothing further; a demand with none of its three conditions met is rejected. The same ingredient typically appears across many demands, sometimes demanded IN by one and OUT by another, and the demands may overlap heavily or barely at all — none of that matters except through the exact conditions each demand lists. Decide whether there is a single global IN/OUT setting of all n ingredients that satisfies **every** demand simultaneously, and if so report one such setting; otherwise the demand set is over-constrained. Satisfying the demands one at a time is trivial — the difficulty is one formulation consistent with all of them at once.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 90, 0 ≤ m ≤ 400).
Each of the next m lines contains three non-zero signed integers l1 l2 l3,
with |li| ≤ n. A positive integer means the ingredient is demanded IN, while a negative integer means it is demanded OUT. At least one of the three stated conditions must hold.

## Output
If no valid formulation exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers
s1 s2 … sn (each in {0, 1}), where si is the state of ingredient i (1 for IN, 0 for OUT). Any valid formulation is accepted.

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
Each demand has exactly three entries. The same ingredient index may appear
more than once in a demand.
