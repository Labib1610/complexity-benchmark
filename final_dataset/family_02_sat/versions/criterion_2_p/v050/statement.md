# Problem B — Drone Telemetry

Time limit: 1 s   Memory limit: 256 MB

## Description

A surveyor drone has $n$ sensor arrays. Each array must be permanently locked into either active mode (1) or standby mode (0) before launch.

During flight, the drone must avoid $m$ critical failure scenarios. A failure scenario is triggered when two specific array modes are simultaneously absent from the drone's configuration. 

To describe these scenarios, the flight manual provides $m$ pairs of target behaviors. A target behavior is a specific mode for a specific array (for example, 'array 4 in standby'). For each pair, if the drone's final configuration lacks the first target behavior and also lacks the second target behavior, the drone will experience a critical failure. Consequently, to prevent a failure, the configuration must exhibit the first target behavior, the second target behavior, or both.

You must determine if there is a single, permanent mode assignment for all $n$ arrays that prevents all $m$ critical failures.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two non-zero integers $l_1$ and $l_2$, with $|l_i| \le n$. 
A positive integer $l$ represents the target behavior where array $|l|$ is in active mode (1).
A negative integer $l$ represents the target behavior where array $|l|$ is in standby mode (0).
Each line provides the two target behaviors associated with a single critical failure scenario.

## Output
If it is impossible to assign modes to all arrays such that all critical failures are prevented, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each being 0 or 1) representing the mode of each array from 1 to $n$ in a successful assignment. 

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
Multiple valid assignments may exist; any one is accepted. The same array may appear in multiple failure scenarios.
