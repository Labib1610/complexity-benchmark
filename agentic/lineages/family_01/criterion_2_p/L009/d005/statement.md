# Differential Lighting

Time limit: 1 s   Memory limit: 256 MB

You are configuring a lighting system consisting of $n$ fixtures, numbered 1 through $n$. 
Due to power constraints, every fixture must be wired to exactly one of two available power sources: Circuit 1 or Circuit 2.

The system includes $m$ differential sensors. Each sensor monitors a specific pair of fixtures (due to wiring anomalies, a sensor might monitor the same fixture twice). 
For a differential sensor to function correctly, it must observe a voltage difference. This means that exactly one of its monitored fixtures must be wired to Circuit 1, and the other must be wired to Circuit 2.

Your task is to determine whether there is a wiring assignment for all $n$ fixtures that allows all $m$ differential sensors to function correctly simultaneously.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing the indices of the fixtures monitored by a differential sensor.

## Output
If no valid wiring assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ integers $c_1, \dots, c_n$, where $c_i$ is the circuit (1 or 2) assigned to fixture $i$. If there are multiple valid assignments, choose the assignment that minimizes $c_1$. If there is still a tie, minimize $c_2$ among the remaining valid assignments, and continue this process sequentially up to $c_n$.

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