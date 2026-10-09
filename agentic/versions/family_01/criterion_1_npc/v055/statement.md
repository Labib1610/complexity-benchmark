# Problem A — Phase Containment

Time limit: 2 s   Memory limit: 256 MB

A research facility is testing a network of $n$ experimental energy modules. To maintain stable power output, each module must be calibrated to exactly one of three available phase states, labeled 1, 2, or 3.

During preliminary testing, engineers identified $m$ specific pairs of modules that share a thermal conduit. If two modules sharing a conduit are calibrated to the exact same phase state, their combined resonance will overload the conduit and trigger a system failure. Therefore, any two modules connected by a thermal conduit must be assigned strictly different phase states.

You must determine whether it is possible to calibrate the entire network of $n$ modules safely. If it is, you must provide a valid assignment of phase states.

## Input
The first line contains two integers $n$ and $m$ — the number of modules and the number of shared thermal conduits ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the following $m$ lines contains two integers $u$ and $v$ — the identifiers of two modules that share a thermal conduit.

## Output
If no safe calibration exists, print a single line NO.
Otherwise, print YES on the first line. On the second line, print $n$ integers $p_1, p_2, \dots, p_n$ (each in $\{1, 2, 3\}$), where $p_i$ is the phase state assigned to module $i$. Any valid calibration is accepted.

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
