# Problem B — Water System Mandates

Time limit: 1 s   Memory limit: 256 MB

## Description
A municipal water system contains **n** control gates, numbered 1 through **n**, each of which must be configured as either OPEN (1) or CLOSED (0). The system must adhere to **m** compliance mandates. Each mandate specifies exactly two gate conditions. A gate condition is defined by a gate's index and its required state (either OPEN or CLOSED). To fulfill a single mandate, the system's configuration must match at least one of the two specified gate conditions. Find a single system-wide configuration for all **n** gates that simultaneously fulfills all **m** mandates, or determine that no such configuration exists.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 10^5, 0 ≤ m ≤ 2·10^5).
Each of the next m lines contains two non-zero integers l1 and l2 (|li| ≤ n), representing the two conditions of a mandate. A positive integer v indicates the condition that gate v is OPEN. A negative integer -v indicates the condition that gate v is CLOSED.

## Output
If no valid configuration exists, print a single line containing NO.
Otherwise, print YES on the first line. On the second line, print n integers s1, s2, ..., sn (each in {0, 1}), where si = 1 if gate i is OPEN and si = 0 if gate i is CLOSED.

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
Multiple valid configurations may exist; any one is accepted. The same gate may appear in multiple mandates.
