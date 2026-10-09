# Problem A — Phase Containment

Time limit: 2 s   Memory limit: 256 MB

A research facility is testing $n$ experimental energy modules. Each module must be calibrated to operate in a single phase state. The valid phase states are denoted by the integers 1, 2, and 3.

During preliminary testing, $m$ unstable interactions were recorded. Each interaction involves a specific pair of modules $u$ and $v$. If both modules in such a pair are calibrated to the exact same phase state, they will resonate and destabilize the array. To ensure safe operation, for every recorded interaction between a module $u$ and a module $v$, their assigned phase states must be strictly different.

Determine if there is a valid calibration for all $n$ modules. If it is possible, provide one such calibration.

## Input
The first line contains two integers $n$ and $m$ — the number of modules and the number of recorded interactions ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the identifiers of two modules that interact unstably.

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
