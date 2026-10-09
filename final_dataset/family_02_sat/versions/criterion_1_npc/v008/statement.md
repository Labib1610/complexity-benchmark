# Problem A — Configuration Pipeline: Stage 2

Time limit: 2 s   Memory limit: 256 MB

## Description

The configuration of a facility involves a three-stage pipeline. In Stage 1, commissioning parses subsystem audits to produce **m** acceptance rules over **n** binary switches. Each switch must be set firmly to ON or OFF before the run — no switch may be left floating, and there is no third state. Every rule produced names three switch-references and passes precisely when **at least one** of the three named conditions is met (a condition names a switch together with the polarity — ON or OFF — that satisfies it). A rule with a met condition imposes nothing further; a rule with none of its three conditions met is violated. The same switch typically appears across many rules, sometimes demanded ON by one and OFF by another, and the rules may overlap heavily or barely at all — none of that matters except through the exact conditions each rule lists.

In Stage 2, your software must take the output of Stage 1 and decide whether there is a single global ON/OFF setting of all n switches that satisfies **every** rule simultaneously. If so, it must report one such setting; otherwise it must report that the rule set is over-constrained. Satisfying the rules one at a time is trivial — the difficulty is one assignment consistent with all of them at once.

In Stage 3, the facility either deploys your reported setting to the physical switches, or initiates a manual review if the rules were over-constrained.

Your task is to implement Stage 2.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 90, 0 ≤ m ≤ 400).
Each of the next m lines contains three non-zero signed integers l1 l2 l3,
with |li| ≤ n. At least one of the three stated conditions must hold.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers
s1 s2 … sn (each in {0, 1}), where si is the state of switch i. Any valid
assignment is accepted.

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
