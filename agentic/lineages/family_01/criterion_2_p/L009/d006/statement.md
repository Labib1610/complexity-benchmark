# Differential Lighting

Time limit: 1 s   Memory limit: 256 MB

You are responsible for calibrating a system of $n$ lighting fixtures, indexed from 1 to $n$. To complete the setup, you must assign a discrete operating mode to each fixture $i$. The operating mode is denoted by an integer $c_i$, which must be chosen from the set $\{1, 2\}$.

The installation also features $m$ differential sensors. Each sensor takes readings from a specified pair of fixtures $u$ and $v$. Because of layout irregularities, a sensor may occasionally take both readings from the same fixture. A sensor will only register a valid reading if the operating modes of its two targeted fixtures satisfy the algebraic condition $c_u + c_v = 3$.

You need to determine if it is possible to assign an operating mode to every fixture in a way that allows all $m$ sensors to register valid readings at the same time.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$), indicating the indices of the fixtures from which a sensor takes its readings.

## Output
If no such assignment is possible, output a single line with the word `NO`.
If a valid arrangement exists, output `YES` on the first line. On the second line, output $n$ integers $c_1, \dots, c_n$, where $c_i$ is the operating mode assigned to fixture $i$. If more than one valid assignment satisfies all sensors, you must output the assignment that minimizes the value of $c_1$. In the event of a tie, minimize $c_2$ among the tied assignments, and proceed in this sequential manner for all subsequent fixtures up to $c_n$.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```