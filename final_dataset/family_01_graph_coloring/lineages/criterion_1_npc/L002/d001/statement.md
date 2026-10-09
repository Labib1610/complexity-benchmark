# Harmonic Containment

Time limit: 2 s   Memory limit: 256 MB

An engineering team is finalizing the setup of $n$ experimental energy cores. To function correctly, every core has to be tuned to exactly one of three available frequency bands, which are identified by the integers 1, 2, and 3.

The team has a log of $m$ hazardous resonance events from earlier trials. Each event specifies a pair of distinct cores, $u$ and $v$, that interfere with each other. If any two cores listed in an event are tuned to the identical frequency band, their resonance will cause a system failure. Therefore, to achieve a stable setup, any two cores that share a logged interference event must be assigned strictly different frequency bands.

Your task is to figure out whether all $n$ cores can be safely tuned. If a stable configuration is achievable, you must also output one valid assignment of bands to the cores.

## Input
The first line provides two integers $n$ and $m$, representing the total number of energy cores and the number of interference events, respectively ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$). 
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that the distinct cores $u$ and $v$ interfere with each other. 

## Output
If it is impossible to safely tune all the cores, output a single line containing NO.
If a stable configuration exists, output YES on the first line. On the second line, output $n$ integers $p_1, p_2, \dots, p_n$, where $p_i \in \{1, 2, 3\}$ is the frequency band assigned to the $i$-th core. If there are multiple safe configurations, any of them will be accepted.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```