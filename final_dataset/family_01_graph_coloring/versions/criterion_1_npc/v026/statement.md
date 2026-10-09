# Phase 2: Frequency Multiplexing

Time limit: 2 s   Memory limit: 256 MB

You are developing a module for a satellite communications pipeline. The pipeline operates in three sequential phases:

**Phase 1: Telemetry Ingestion**
The system receives raw data streams from $n$ distinct monitoring satellites. An interference analysis is performed to determine which pairs of data streams have overlapping harmonics.

**Phase 2: Frequency Multiplexing (Your Task)**
The $n$ data streams must be modulated onto one of three available carrier frequencies (labeled 1, 2, and 3) for the downlink transmission. Your module receives the number of satellites and the list of interfering stream pairs identified in Phase 1. You must assign every data stream to exactly one carrier frequency. To ensure data integrity, no two streams that have overlapping harmonics may be assigned the same carrier frequency. If no such assignment is possible, the batch must be rejected.

**Phase 3: Downlink and Decoding**
The ground station receives the multiplexed signals, demodulates them using your assigned frequencies, and archives the telemetry.

Your task is to implement the logic for Phase 2. Given the output from Phase 1, determine a valid frequency assignment for all $n$ streams, or report that the batch cannot be processed.

## Input
The first line contains two integers $n$ and $m$ — the number of data streams and the number of interfering pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of data streams that have overlapping harmonics.

## Output
If there is no way to assign the frequencies without interference, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $f_1, f_2, \dots, f_n$ (each in {1, 2, 3}), where $f_i$ is the carrier frequency assigned to data stream $i$. If there are multiple valid assignments, any valid assignment is accepted.

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
