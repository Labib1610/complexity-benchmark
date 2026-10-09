# Problem A — Distributed Sensor Network

Time limit: 2 s   Memory limit: 256 MB

You are deploying a network of $n$ sensor buoys. Each buoy must be configured with exactly one of 3 available firmware packages, identified by the integers 1, 2, and 3.

The buoys are designed to monitor 4 environmental metrics: Temperature, Salinity, Pressure, and Turbidity. Due to hardware limitations, each firmware package can only track exactly 3 of these metrics:
- **Package 1** tracks Temperature, Salinity, and Pressure.
- **Package 2** tracks Temperature, Salinity, and Turbidity.
- **Package 3** tracks Temperature, Pressure, and Turbidity.

You are given a list of $m$ critical adjacent pairs of buoys. Each pair involves two specific buoys $(u, v)$ that monitor a highly volatile sector. 
To ensure complete environmental data collection in these sectors, every given adjacent pair must collectively track all 4 metrics. That is, the combined set of metrics tracked by buoy $u$ and buoy $v$ together must include Temperature, Salinity, Pressure, and Turbidity.

You must assign a firmware package (1, 2, or 3) to each of the $n$ buoys such that all $m$ critical adjacent pairs successfully track all 4 metrics.

## Input
The first line contains two integers $n$ and $m$ — the number of buoys and the number of critical adjacent pairs ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a critical adjacent pair of buoys. Buoys are indexed from 1 to $n$.

## Output
If no such assignment is possible, output NO on a single line.
Otherwise, output YES on the first line. On the second line, output $n$ integers $c_1 \ c_2 \dots c_n$ (each being 1, 2, or 3), where $c_i$ is the firmware package assigned to buoy $i$. If multiple valid assignments exist, you may output any of them.

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