# Problem B — Telemetry Calibration Sequence

Time limit: 1 s
Memory limit: 256 MB

## Description
The trajectory analysis division first computes the raw telemetry dependencies for an upcoming observation cycle, resulting in a list of $m$ calibration requirements for the observatory's $n$ data channels.

Your module handles the subsequent configuration phase. Each of the $n$ channels must be locked into exactly one of two operational states: primary mode or secondary mode. Each of the $m$ calibration requirements specifies two desired channel states. A requirement is fulfilled if the final global configuration matches at least one of its two desired states. You must determine if it is possible to configure all $n$ channels such that every single calibration requirement is fulfilled.

If you successfully find a working configuration, it is forwarded to the hardware controllers to lock the channels. Following this, the observatory's main aperture opens and the deep-space data collection sequence begins. If the requirements fundamentally conflict, you must report the failure so the trajectory can be aborted and recalculated.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of data channels and the number of calibration requirements, respectively.

Each of the following $m$ lines contains two non-zero integers $l_1$ and $l_2$ ($|l_i| \le n$). The absolute value of $l_i$ indicates the channel identifier. A positive value indicates a desired state of primary mode, while a negative value indicates a desired state of secondary mode. 

## Output
If no valid configuration exists that fulfills all requirements, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ separated by spaces, where $s_i$ is `1` if channel $i$ is set to primary mode, and `0` if it is set to secondary mode. If multiple valid configurations exist, any of them will be accepted.

## Example 1
### Input
```
2 2
1 2
-1 -2
```
### Output
```
YES
1 0
```

## Example 2
### Input
```
1 2
1 1
-1 -1
```
### Output
```
NO
```
