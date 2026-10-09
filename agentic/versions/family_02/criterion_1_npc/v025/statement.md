# Drone Fleet Altitude Configuration

Time limit: 2 s   Memory limit: 256 MB

## Description

A logistics company operates a fleet of $n$ delivery drones. For the upcoming shift, each drone must be assigned exactly one flight mode: high-altitude (represented as 1) or low-altitude (represented as 0). There is no intermediate or floating state.

During the pre-flight checks, the automated traffic system generated $m$ safety guidelines. Each guideline specifies exactly three drone-mode conditions. A condition is denoted by a non-zero integer: a positive value $+i$ means the guideline expects drone $i$ to be in high-altitude mode, and a negative value $-i$ means the guideline expects drone $i$ to be in low-altitude mode. 

A guideline is considered satisfied if **at least one** of its three conditions is met by the fleet's configuration. A guideline with a met condition imposes nothing further. If none of the three conditions are met, the guideline is violated, which grounds the fleet.

To facilitate efficient routing, the regulatory framework guarantees that for any guideline, the sum of the absolute drone IDs involved is at most $3n$, and the product of their absolute IDs is at most $n^3$. The same drone may appear across many guidelines, and the guidelines may overlap heavily.

Your task is to determine whether there is a single, fleet-wide configuration (assigning 0 or 1 to each of the $n$ drones) that satisfies all $m$ guidelines simultaneously. If such a configuration exists, you must provide one. Otherwise, report that the fleet is grounded.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$), representing the number of drones and the number of safety guidelines.
Each of the next $m$ lines contains three non-zero integers $d_1, d_2, d_3$, where $|d_k| \le n$. These represent the three conditions of a guideline. At least one of these three conditions must be satisfied for the guideline to be met.

## Output
If there is no valid fleet configuration that satisfies all guidelines, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $c_1, c_2, \dots, c_n$ (each either 0 or 1), where $c_i$ is the assigned mode for drone $i$. Any valid configuration that satisfies all guidelines will be accepted.

## Example 1
Input:
```
3 2
1 2 3
-1 2 -3
```
Output:
```
YES
0 0 1
```

## Example 2
Input:
```
1 2
1 1 1
-1 -1 -1
```
Output:
```
NO
```

## Note
Each guideline lists exactly three conditions. A drone's index may appear more than once within the same guideline.
