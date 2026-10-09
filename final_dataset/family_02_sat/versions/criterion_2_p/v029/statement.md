# Problem B — Paired Window Constraints

Time limit: 1 s   Memory limit: 256 MB

## Description

A control panel has **n** toggles, each set to 1 or 0 before the run. Commissioning supplies **m** operational rules, but here **every** rule names exactly **two** toggle-requirements and passes when at least one of the two is met (each requirement being a toggle plus the sign that fulfills it). Because each rule couples only a pair of toggles, a failing requirement on one side requires the other side's requirement to hold — the rules link together as sequences of required outcomes. Planners sometimes worry this requires checking all possibilities, but the two-part structure makes the outcomes completely determinable. Decide whether a single global 1/0 setting of all n toggles passes every rule at once, and if so report one; otherwise report that the rules cannot all be met.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 10^5, 0 ≤ m ≤ 2·10^5).
Each of the next m lines contains two non-zero signed integers l1 l2, with
|li| ≤ n. At least one of the two stated requirements must hold.

## Output
If no valid setting exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers
s1 s2 … sn (each in {0, 1}) forming any valid setting.

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
Multiple valid settings may exist; any one is accepted. The same toggle may appear in multiple requirements.
