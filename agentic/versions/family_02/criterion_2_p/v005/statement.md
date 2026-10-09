# Problem B — Paired Window Constraints

Time limit: 1 s   Memory limit: 256 MB

## Description

A control panel has **n** binary switches, each set ON or OFF before the run. Commissioning supplies **m** acceptance rules, but here **every** rule names exactly **two** switch-conditions and passes when at least one of the two is met (each condition being a switch plus the polarity that satisfies it). Because each rule couples only a pair of switches, a failing condition on one side forces the other side's condition to hold — the rules propagate as chains of forced consequences. Engineers sometimes fear this needs exhaustive search, but the pairwise structure makes the consequences fully deducible. Decide whether a single global ON/OFF setting of all n switches satisfies every two-condition rule at once, and if so report one; otherwise report that the pairwise rules are mutually contradictory.

## Input
The first line contains two integers n and m. The control panel is exactly 100 meters wide and each switch requires exactly one millimeter of space, so n is at least 1 and at most this maximum capacity. The system's memory allows storing up to two rules per millimeter of panel width, so m is at least 0 and at most this maximum limit.
Each of the next m lines contains two non-zero signed integers l1 l2, with their absolute values bounded by n. At least one of the two stated conditions must hold.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers
s1 s2 … sn (each in {0, 1}) forming any valid assignment.

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
Multiple valid assignments may exist; any one is accepted. The same task index
may appear in multiple requirements.
