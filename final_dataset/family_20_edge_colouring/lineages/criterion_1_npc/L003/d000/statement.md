# Problem A — Transmission Network Maintenance Scheduling

Time limit: 5 s
Memory limit: 256 MB

## Description
A utility company manages a transmission network consisting of stations connected by bidirectional lines. The network's topology is strictly uniform: every station serves as an endpoint for exactly the same number of lines. Since the network contains $n$ stations and $m$ lines, this uniformity dictates the exact number of connections at every station.

Routine maintenance must be performed on every line, which requires taking the line offline for exactly one shift. To prevent grid instability, safety regulations dictate that no station may have more than one of its connected lines taken offline during the same shift. 

The company wishes to complete the maintenance as quickly as possible. Therefore, the total number of shifts allocated for the entire project exactly matches the number of lines connected to any single station. 

Determine whether it is possible to assign a shift to every line such that the safety regulation is satisfied at all stations simultaneously. 

## Input
The first line contains two integers $n$ and $m$ ($n$ is even, $m = 3n/2$, $2 \le n \le 2000$), representing the number of stations and the number of lines, respectively.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u < v \le n$), indicating a line connecting station $u$ and station $v$.

## Output
If a valid schedule exists, print `YES` on the first line. On the second line, print $m$ integers, each chosen from $\{1, 2, 3\}$, representing the shift assigned to each line in the order they appear in the input. If no such schedule is possible, print `NO`.

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
