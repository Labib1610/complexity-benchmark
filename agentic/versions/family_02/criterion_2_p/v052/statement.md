# Problem B — Relay Network Calibration

Time limit: 1 s
Memory limit: 256 MB

## Description
A communication network contains $n$ relays, numbered 1 through $n$. Each relay must be permanently calibrated to exactly one of two modes: ACTIVE (1) or DORMANT (0).

The network must satisfy $m$ structural dependencies to function correctly. Each dependency specifies exactly two target relay modes. A target mode is defined by a relay's index and its desired mode (either ACTIVE or DORMANT). 

To satisfy a dependency, the following rule applies: if the network's overall calibration does not match the first target mode, it must match the second target mode. Because the relationship is symmetric, not matching the second target mode means the calibration must match the first target mode. Matching both target modes simultaneously also fully satisfies the dependency.

Determine a single valid calibration for all $n$ relays that simultaneously satisfies all $m$ dependencies, or conclude that no such calibration is possible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two non-zero integers $l_1$ and $l_2$ ($|l_i| \le n$), representing the two target modes of a dependency. A positive integer $v$ represents the target mode where relay $v$ is ACTIVE. A negative integer $-v$ represents the target mode where relay $v$ is DORMANT.

## Output
If no valid calibration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{0, 1\}$), where $s_i = 1$ if relay $i$ is ACTIVE and $s_i = 0$ if relay $i$ is DORMANT.

## Example 1
### Input
```
2 2
1 2
-1 -2
```
### Output
```
YES
1 0
```

## Example 2
### Input
```
1 2
1 1
-1 -1
```
### Output
```
NO
```

## Note
Multiple valid calibrations may exist; any one is accepted. The same relay may appear in multiple dependencies.
