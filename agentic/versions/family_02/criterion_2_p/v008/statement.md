# Problem B — Paired Window Constraints

Time limit: 1 s   Memory limit: 256 MB

## Description

The system configuration pipeline operates in three stages. First, a parser transforms complex user requirements into a standardized intermediate format concerning **n** binary switches, each to be set ON or OFF before the run. This format consists of **m** acceptance rules, where **every** rule names exactly **two** switch-conditions and passes when at least one of the two is met (each condition being a switch plus the polarity that satisfies it). 

In the second stage—which your program must implement—you evaluate this intermediate format. Because each rule couples only a pair of switches, a failing condition on one side forces the other side's condition to hold — the rules propagate as chains of forced consequences. Engineers sometimes fear this needs exhaustive search, but the pairwise structure makes the consequences fully deducible. Decide whether a single global ON/OFF setting of all n switches satisfies every two-condition rule at once, and if so report one; otherwise report that the pairwise rules are mutually contradictory.

Finally, in the third stage, a downstream controller will read your output and physically actuate the switches.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 10^5, 0 ≤ m ≤ 2·10^5).
Each of the next m lines contains two non-zero signed integers l1 l2, with
|li| ≤ n. At least one of the two stated conditions must hold.

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
