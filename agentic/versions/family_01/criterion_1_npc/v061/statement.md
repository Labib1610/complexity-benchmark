# Problem A — Signal Routing

Time limit: 2 s   Memory limit: 256 MB

An industrial control system coordinates $n$ robotic actuators. To prevent signal overlap, each actuator $i$ (from $1$ to $n$) must be assigned a discrete frequency multiplier $f_i$ chosen from the set $\{1, 2, 3\}$.

The system's diagnostic tool has output a list of $m$ interference constraints. Each constraint specifies a pair of actuators $(u, v)$ that share a local communication bus. For the system to operate safely, every constraint $(u, v)$ must satisfy the condition $|f_u - f_v| > 0$. Furthermore, every actuator must be assigned exactly one frequency multiplier.

Your task is to determine if there exists a complete assignment of frequency multipliers to all $n$ actuators such that all $m$ constraints are satisfied simultaneously. If such an assignment exists, you must output one valid configuration.

## Input
The first line contains two integers $n$ and $m$ — the number of actuators and the number of constraints ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of actuators that form a constraint.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES on the first line. On the second line print $n$ integers $f_1 \ f_2 \dots f_n$ (each in $\{1, 2, 3\}$), where $f_i$ is the frequency multiplier assigned to actuator $i$. Any valid assignment is accepted.

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
