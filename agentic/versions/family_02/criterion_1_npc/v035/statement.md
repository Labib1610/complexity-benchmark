# Problem A — Switch Configuration Resolution

Time limit: 2 s   Memory limit: 256 MB

## Description

A control system exposes **n** binary switches, each of which the operator must set firmly to ON or OFF before the run — no switch may be left floating, and there is no third state. Commissioning has produced **m** locally bounded acceptance rules gathered from separate subsystem audits; every rule names three switch-references and passes precisely when **at least one** of the three named conditions is met (a condition names a switch together with the polarity — ON or OFF — that satisfies it). A rule with a met condition imposes nothing further, meaning local compliance is always trivial; a rule with none of its three conditions met is violated. The same switch typically appears across many rules, sometimes demanded ON by one and OFF by another. Because rules often share common switches, local decisions can cascade naturally through the system. Decide whether there is a single global ON/OFF setting of all n switches that satisfies **every** rule simultaneously, and if so report one such setting; otherwise the rule set is over-constrained. While satisfying any single rule or small cluster is straightforward, you must find one assignment consistent with all of them at once.

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
Each rule has exactly three entries. The same switch index may appear
more than once in a rule.
