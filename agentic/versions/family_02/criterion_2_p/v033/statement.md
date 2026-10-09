# Problem B — Paired Window Constraints

Time limit: 1 s   Memory limit: 256 MB

## Description

A control panel has **n** binary switches, each set to 1 or 0 before the run. Commissioning supplies **m** acceptance rules. Each rule specifies exactly two target switch states (where a target state is a specific switch and its desired 1 or 0 value). A rule triggers a system failure if and only if both of its specified target states are violated by the current switch settings. Because each rule monitors only a pair of states, violating one target forces the system to require the other target to be met to avoid failure — these requirements propagate as chains of forced consequences. Decide whether a single global 1/0 setting of all n switches avoids all rule failures at once, and if so report one; otherwise report that the rules are mutually contradictory.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 10^5, 0 ≤ m ≤ 2·10^5).
Each of the next m lines contains two non-zero signed integers l1 l2, with
|li| ≤ n. A positive value +x means switch x being 1 is a target; a negative value -x means switch x being 0 is a target. To avoid failure, at least one of the two targets must be met.

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
Multiple valid assignments may exist; any one is accepted. The same switch index
may appear in multiple rules.
