# Problem B — Paired Window Constraints

Time limit: 1 s   Memory limit: 256 MB

## Description

A control panel features a set of toggles, each of which must be locked into either an active or a dormant mode before operations begin. During commissioning, inspectors provide a list of safety regulations. Every regulation highlights exactly two target states (a target state being a specific toggle and its desired mode). To pass inspection, a minimum of one of the two target states in each regulation must be successfully matched by the panel's configuration.

Because each regulation links exactly two targets, if the panel is configured such that one target is missed, the other target becomes strictly mandated to pass the inspection. This dual-target nature means that decisions cascade through the system as a web of requirements. Engineers sometimes worry that finding a valid setup requires trial and error, but the dependencies are fully traceable.

Determine if there exists a global configuration of all toggles that successfully passes every regulation on the inspector's list. If it does, provide an example of such a configuration; otherwise, report that the regulations fundamentally clash.

## Input

The first line contains two integers: the total count of toggles and the total count of regulations. The panel is built with at least one toggle, up to a hardware limit of 100,000 toggles. The inspector's logbook may contain no regulations, up to a maximum capacity of 200,000 regulations.

Each of the subsequent lines corresponds to one regulation and contains two non-zero integers. The magnitude of each integer identifies the toggle (from 1 up to the total count of toggles). The sign of the integer dictates the target mode: positive means the target is for the toggle to be active, while negative means the target is for the toggle to be dormant.

## Output

If no such configuration is possible, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print the configuration as a sequence of space-separated integers, one for each toggle in order from 1 to the total count. Print `1` if the toggle is active, and `0` if it is dormant.

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
Multiple valid configurations may exist; any one is accepted. The same toggle may appear in multiple regulations.
