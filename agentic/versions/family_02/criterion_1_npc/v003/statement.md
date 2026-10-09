# Problem A — System Switch Assignment

Time limit: 2 s   Memory limit: 256 MB

## Description

A control system exposes **n** binary switches, each of which the operator must set firmly to ON or OFF before the run — no switch may be left floating, and there is no third state. Commissioning has produced **m** acceptance rules gathered from separate subsystem audits; every rule specifies three switch-references and evaluates to a pass unless **all three** of its specified conditions are simultaneously contradicted by the board (a condition names a switch together with the polarity — ON or OFF — it expects). A rule with at least one matching condition imposes nothing further; a rule whose three conditions are all contradicted is violated. The same switch typically appears across many rules, sometimes demanded ON by one and OFF by another, and the rules may overlap heavily or barely at all — none of that matters except through the exact conditions each rule lists. Decide whether there is a single global ON/OFF setting of all n switches that satisfies **every** rule simultaneously, and if so report one such setting; otherwise the rule set is over-constrained. Satisfying the rules one at a time is trivial — the difficulty is one assignment consistent with all of them at once.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 90, 0 ≤ m ≤ 400).
Each of the next m lines contains three non-zero signed integers l1 l2 l3,
with |li| ≤ n. A positive value +i means the condition expects switch i to be ON; a negative value -i means the condition expects switch i to be OFF. For a valid assignment, not all three stated conditions in a rule can be contradicted.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers
s1 s2 … sn (each in {0, 1}), where si is the state of switch i (1 for ON, 0 for OFF). Any valid assignment is accepted.

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
Each requirement group has exactly three entries. The same switch index may appear
more than once in a group.
