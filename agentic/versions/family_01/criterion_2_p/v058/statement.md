# Frequency Settings

Time limit: 1 s
Memory limit: 256 MB

In a maritime survey operation, $n$ autonomous vessels are deployed. Each vessel is equipped with a transmitter that must be locked to either frequency setting 1 or frequency setting 2. During the deployment, the vessels follow coordinated paths, which causes $m$ specific pairs of vessels to pass within close range of one another. When a pair of vessels is in close range, their telemetry systems will clash if both are locked to the identical frequency setting.

You are required to find a frequency setting for each of the $n$ vessels such that no telemetry clashes occur during the operation. If several clash-free setups are possible, you must identify the setup that results in the lexicographically smallest sequence of settings for the vessels indexed 1 to $n$. If no setup can prevent all clashes, you must determine that it is unachievable.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of vessels and the number of close-range encounters.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that vessel $u$ and vessel $v$ will pass within close range.

## Output
If there is no way to prevent all telemetry clashes, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $s_1, \ldots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid sequence of frequency settings.

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
