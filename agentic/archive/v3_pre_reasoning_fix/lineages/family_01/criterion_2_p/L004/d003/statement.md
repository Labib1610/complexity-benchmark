# Sensor Calibration

Time limit: 1 s   Memory limit: 256 MB

You are in charge of calibrating a network of $n$ sensor units. For each unit, you must select a transmission power setting. Hardware constraints require this setting to be either 1 or 2 milliwatts.

The sensor network depends on $m$ point-to-point data links, each bridging a specific pair of units. Data can only flow reliably across a link if the cross-link power dissipation is strictly controlled. Specifically, the product of the power settings of the two units sharing a link must equal exactly 2 square milliwatts. Any link where the product of its endpoints' settings deviates from this exact value will suffer from signal reflection, causing the link to fail.

You need to figure out if there is a way to assign a power setting to all $n$ units so that zero links fail. If such an assignment exists, you must also provide it. Since the firmware updates the units in numerical order, you must provide the lexicographically smallest sequence of power settings (from unit 1 up to unit $n$) if there is more than one valid way to calibrate the network.

## Input
The first line provides two integers, $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), which denote the total number of sensor units and the total number of data links.
Each of the subsequent $m$ lines contains two integers $u$ and $v$, meaning there is a data link connecting unit $u$ and unit $v$. The units are numbered using integers from 1 to $n$.

## Output
If no valid power assignment can prevent all link failures, output `NO` on a single line.
If a valid assignment can be found, output `YES` on the first line. On the second line, output $n$ space-separated integers (all 1s or 2s) indicating the power setting for each unit from 1 to $n$. If there are multiple working assignments, this sequence must be the lexicographically smallest one.

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