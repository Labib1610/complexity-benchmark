# Problem B — Interferometry Array

Time limit: 1 s   Memory limit: 256 MB

An observatory operates an interferometry array consisting of $n$ radio telescope dishes. To calibrate the array for a new observation run, the control system must assign a configuration value to each dish. The hardware only supports configuration values that are positive integers with a specific property: the total number of positive divisors of the assigned value must be exactly equal to the value itself.

The array relies on $m$ baseline connections, each linking a specific pair of dishes that act as a single synthetic aperture. For the interferometry to function correctly across a baseline, the signals from the two linked dishes must be offset. The control system enforces this by requiring that for any two dishes connected by a baseline, the sum of the cubes of their assigned configuration values is exactly $9$.

You need to determine if there is a valid calibration that satisfies all baseline connections. If there are multiple valid ways to assign the configuration values across the array, the control system must select the one that yields the lexicographically smallest sequence of values when listed in order from dish $1$ to dish $n$.

## Input
The first line of the input contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a baseline connection between dish $u$ and dish $v$.

## Output
If there is no way to assign the configuration values without violating the baseline requirements, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers separated by spaces, where the $i$-th integer is the configuration value assigned to the $i$-th dish, representing the lexicographically smallest valid assignment ordered by dish indices from $1$ to $n$.

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