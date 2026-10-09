# Problem A — Frequency Tuning in the Transfer Hub Network

Time limit: 5 s
Memory limit: 256 MB

## Description
An automated facility moves items using a network of conveyor belts between transfer hubs. The facility's layout is perfectly uniform: every hub serves as an endpoint for the exact same number of belts. You can deduce this exact number from the fact that the total number of belts is exactly 1.5 times the number of hubs.

To prevent control signal interference, each belt must be configured to operate on one of three distinct frequency channels (labeled 1, 2, and 3). The hardware at each hub requires that all belts connecting to it must operate on completely different frequencies. If any two belts sharing a hub were to use the same frequency channel, the hub's routing sensors would fail. 

Because of the uniform design, the number of available frequency channels perfectly matches the number of belts meeting at each hub. You must determine if there is a valid frequency configuration for the entire facility. If it is possible, provide a valid assignment for every belt. A single unavoidable frequency clash makes the whole configuration impossible.

## Input
The first line contains two integers `n` and `m` (`n` even, `m = 3n/2`, `2 <= n <= 2000`), representing the number of hubs and belts, respectively.
Each of the next `m` lines contains two integers `u` and `v` (`1 <= u < v <= n`), indicating a belt connecting hub `u` and hub `v`.

## Output
If a valid configuration exists, print `YES` on the first line. On the second line, print `m` integers, each chosen from `{1, 2, 3}`, representing the frequency assigned to each belt in the order they were given in the input. If no such configuration is possible, print `NO`.

## Example
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
YES
1 2 3 3 2 1
```
