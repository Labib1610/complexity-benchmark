# Problem B — Paired Valve Constraints

Time limit: 1 s   Memory limit: 256 MB

## Description

An industrial fluid network contains **n** directional valves, each configured to position 1 or 0 before the process starts. The safety system defines **m** pressure-relief rules, where **every** rule specifies exactly **two** valve-conditions and averts a rupture when at least one of the two is met (each condition being a valve index plus the position that satisfies it). Because each rule couples only a pair of valves, a failing condition on one side forces the other side's condition to hold — the safety requirements propagate as chains of forced consequences. Facility engineers sometimes fear this requires testing all combinations, but the pairwise structure makes the consequences fully deducible. Decide whether a single global 1/0 configuration of all n valves satisfies every two-condition rule at once, and if so report one; otherwise report that the pairwise rules are mutually contradictory.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 10^5, 0 ≤ m ≤ 2·10^5).
Each of the next m lines contains two non-zero signed integers l1 l2, with |li| ≤ n. A positive integer indicates the corresponding valve must be in position 1, and a negative integer indicates the valve (given by the absolute value) must be in position 0. At least one of the two stated conditions must hold for each rule.

## Output
If no valid configuration exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers s1 s2 … sn (each in {0, 1}) forming any valid configuration.

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
Multiple valid configurations may exist; any one is accepted. The same valve index may appear in multiple requirements.
