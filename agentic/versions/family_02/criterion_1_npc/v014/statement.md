# Problem A — Pipeline Valve Configuration

Time limit: 2 s
Memory limit: 256 MB

## Description
A fluid distribution network is controlled by a set of **n** motorized valves. Every valve must be definitively set to either OPEN or CLOSED before operations begin; intermediate states are impossible. The safety protocol dictates a series of **m** pressure relief criteria. 

Each criterion lists exactly three valve-state requirements. A requirement specifies a particular valve and the state (OPEN or CLOSED) it needs to be in. A criterion is considered satisfied if **at least one** of its three requirements matches the actual configuration of the network. The criterion does not care if more than one requirement is met, but if all three fail to match the physical configuration, the criterion is violated. 

The network is highly interconnected. A single valve might be required to be OPEN by several different criteria, and CLOSED by others. Your objective is to determine whether it is possible to find a single, global configuration for all **n** valves that simultaneously satisfies every single criterion in the safety protocol. If such a configuration exists, you must provide it. 

The physical infrastructure of the distribution board provides exactly 90 terminal blocks, limiting the network to a maximum of 90 motorized valves (there is always at least one). Furthermore, the safety protocol is stored on a legacy controller whose memory bank can hold a maximum of 400 criteria (a protocol may also be entirely empty).

## Input
The first line contains two integers $n$ and $m$. The bounds for these values are dictated by the physical and memory constraints described above.
Each of the subsequent $m$ lines corresponds to a single criterion and contains three non-zero integers $l_1, l_2, l_3$. 
The absolute value $|l_i|$ represents a valid 1-based index of a valve in the network (meaning it will never exceed $n$). A positive integer means the criterion requires that valve to be OPEN, while a negative integer means it requires that valve to be CLOSED. Exactly three requirements are given per criterion, and a valve index may appear multiple times within the same criterion.

## Output
If there is no global configuration that satisfies all criteria, print a single line containing `NO`.
If a valid configuration exists, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (each either `0` or `1`), where $s_i$ represents the assigned state of valve $i$ (`1` for OPEN, `0` for CLOSED). Any valid configuration is accepted.

## Example 1
Input:
```
3 2
1 2 3
-1 2 -3
```
Output:
```
YES
0 0 1
```

## Example 2
Input:
```
1 2
1 1 1
-1 -1 -1
```
Output:
```
NO
```
