# Problem B — Paired Hub Constraints

Time limit: 1 s   Memory limit: 256 MB

## Description

A logistics network relies on **n** transit hubs, which must each be configured as either ACTIVE or DORMANT for the upcoming shift. The network management has issued **m** routing protocols. Every protocol specifies exactly two hub-conditions (a hub combined with its required state). A protocol is considered satisfied if at least one of its two specified conditions is met by the network's configuration. 

You must determine if there exists a single global ACTIVE/DORMANT configuration for all n hubs that simultaneously satisfies all m routing protocols. If such a configuration exists, provide one; otherwise, report that the requirements are mutually contradictory.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 10^5, 0 ≤ m ≤ 2·10^5).
Each of the following m lines provides two non-zero signed integers l1 and l2, where |li| ≤ n. A positive integer indicates the hub must be ACTIVE, while a negative integer indicates it must be DORMANT. At least one of these two conditions must be met for the protocol to pass.

## Output
If no valid configuration exists, print a single line NO.
Otherwise, print YES on the first line. On the second line, print n integers s1 s2 … sn (each being 0 or 1, representing DORMANT and ACTIVE respectively) that form a valid configuration.

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
Multiple valid configurations may exist; any one is accepted. The same hub index may appear in multiple requirements.