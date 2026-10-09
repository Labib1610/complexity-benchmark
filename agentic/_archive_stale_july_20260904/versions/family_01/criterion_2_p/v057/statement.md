# Acoustic Sensor Calibration

Time limit: 1 s   Memory limit: 256 MB

The deployment of an acoustic sensor network occurs in three distinct stages. First, $n$ sensors are scattered across a testing field to collect ambient noise data and establish initial telemetry links. 

In the second stage, the central controller must calibrate the network's power distribution. This is the task you must implement. Each sensor must be assigned a power mode, which is strictly restricted to either mode 1 or mode 2. During the initial boot sequence, the system generates $m$ resonance alerts. Each alert specifies a pair of sensors $(u, v)$ that are placed too close to one another. To safely resolve an alert, the controller must ensure that the sum of the power modes assigned to sensors $u$ and $v$ is exactly 3. 

If no valid power mode assignment exists for all sensors that satisfies every alert simultaneously, the calibration fails. Otherwise, multiple valid assignments might exist. Because the final stage requires a deterministic initialization, your software must select the lexicographically smallest sequence of power modes $(p_1, p_2, \dots, p_n)$ out of all valid configurations.

In the third and final stage, the sensors activate their data processing modules using the assigned power modes and begin transmitting filtered telemetry. You only need to simulate the second stage.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of sensors and the number of resonance alerts from the first stage.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating an alert between sensor $u$ and sensor $v$.

## Output
If the calibration cannot be completed because no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $p_1, p_2, \dots, p_n$ (each either 1 or 2), representing the lexicographically smallest valid power mode sequence.

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
