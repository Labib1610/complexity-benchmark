# Paired Switch Constraints

Time limit: 1 s   Memory limit: 256 MB

## Description
A factory's central control panel features $n$ diagnostic switches, each of which must be finalized in either an active (1) or inactive (0) state before the production line starts. The quality assurance team has provided $m$ safety conditions. A safety condition specifies exactly two target switch states (for example, "switch 3 is active" and "switch 7 is inactive"). For a condition to be satisfied, at least one of its two target states must be achieved.

If a condition is not met by the state of its first switch, the second switch is forced into its target state to compensate. This cascading dependency links the switches into long chains of inevitable outcomes. Determine if there is a single, comprehensive configuration of all switches that satisfies every safety condition simultaneously. If a configuration exists, provide one; otherwise, declare that the safety conditions are inherently contradictory.

## Input
The first line contains two integers $n$ and $m$. The number of switches $n$ is at least one, and is constrained by the panel's physical limit of one hundred thousand switches. The number of conditions $m$ starts from zero and is capped at exactly double that physical limit.

Each of the following $m$ lines contains two non-zero integers $l_1$ and $l_2$. The magnitude $|l_i|$ identifies the switch (between 1 and $n$). A positive value dictates the switch should be active, whereas a negative value dictates it should be inactive. Each line represents a single condition where at least one of the two dictated states must be achieved.

## Output
If it is impossible to configure the panel to meet all conditions, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers (each either `0` or `1`), representing the states of switches 1 through $n$ in a valid configuration.

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
Multiple valid configurations may exist; any one is accepted. The same switch may appear in multiple safety conditions.
