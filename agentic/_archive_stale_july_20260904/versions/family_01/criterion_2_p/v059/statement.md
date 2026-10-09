# Problem B — Pipeline Segregation Phase

Time limit: 1 s   Memory limit: 256 MB

The Aegis distributed architecture deployment pipeline processes $n$ independent service modules (indexed 1 to $n$). During the telemetry phase, the system identifies $m$ resource contentions. Each contention record lists two modules that attempt to lock the same hardware component.

To resolve these contentions, you must configure the execution state of every module. There are exactly two available execution states, represented as state 1 and state 2. A configuration is valid if and only if every pair of modules listed in a contention record are assigned different execution states.

The downstream distribution phase requires strictly deterministic routing. If multiple valid configurations exist, you must provide the one that favors state 1 for the lowest-indexed modules. Formally, when comparing two different valid configurations, the preferred one is the one that has a smaller state value (i.e., 1 rather than 2) at the lowest module index where the two configurations assign different states.

If the contention records form a contradictory set where no valid configuration is possible, your phase must reject the pipeline.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), the number of modules and the number of contention records.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that module $u$ and module $v$ cannot share the same execution state.

## Output
If no valid configuration can be established, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers (each either 1 or 2) representing the assigned execution state for each module from 1 to $n$, strictly following the tie-breaking rule.

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
