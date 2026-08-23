# Triple-Factor Security Profile

Time limit: 2 s   Memory limit: 256 MB

You are configuring a high-security access system that relies on a database of $n$ distinct biometric sensors, identified by integers from 1 to $n$. During calibration, the system generated a compatibility log containing $m$ specific pairs of sensors that can operate concurrently without mutual interference.

Your task is to establish a valid security profile, which must incorporate exactly three distinct sensors. For the authentication process to execute flawlessly, the profile must form a closed redundancy loop. Specifically, it must be possible to arrange the three chosen sensors in a sequence such that the first can operate concurrently with the second, the second can operate concurrently with the third, and the third can operate concurrently with the first.

You must determine a valid combination of three sensors for this profile. If multiple valid combinations are possible, you must choose the one that is lexicographically first.

## Input
The first line provides two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the total number of biometric sensors and the number of concurrent sensor pairs.
Each of the subsequent $m$ lines contains two integers $u$ and $v$, indicating that sensor $u$ and sensor $v$ can operate concurrently.
It is guaranteed that at least one valid security profile can be established.

## Output
Print three integers $a$, $b$, and $c$ on a single line, ordered such that $a < b < c$. These integers must represent three sensors that form a closed redundancy loop according to the compatibility log. If there are multiple valid profiles, output the one with the smallest $a$; if there is a tie, the smallest $b$; and finally the smallest $c$.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```