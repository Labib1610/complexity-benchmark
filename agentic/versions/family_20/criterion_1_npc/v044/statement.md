# Problem A — Synchronous Phase Routing on a Uniform Network

Time limit: 5 s   Memory limit: 256 MB

## Description
A strictly engineered synchronous data network consists of routing hubs and bidirectional channels. To guarantee perfect load balancing, the network topology has been built to be perfectly uniform: every single hub is an endpoint for exactly three channels. 

Data transmission is divided into three distinct, rotating time phases (Phase 1, Phase 2, and Phase 3). Each channel must be permanently assigned to operate in exactly one of these three phases. 

To prevent buffer overflow and ensure smooth data flow, the network requires perfect local synchronization at every hub. Specifically, the three channels connected to any given hub must operate in three distinct phases. Because every hub has exactly three connections and there are exactly three phases available, a valid synchronization perfectly distributes the load: at every single hub, exactly one channel activates in Phase 1, one in Phase 2, and one in Phase 3. 

This strict topological regularity was designed to make the network highly structured and evenly distributed. Your task is to find a phase assignment for every channel that achieves this perfect local balance, or report if a structural flaw makes it impossible. 

## Input
The first line contains two integers $n$ and $m$ ($n$ is even, $m = 3n/2$, $2 \le n \le 2000$), representing the number of hubs and the number of channels, respectively. Hubs are numbered from 1 to $n$.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u < v \le n$), indicating a channel connecting hub $u$ and hub $v$. It is guaranteed that every hub appears in exactly three channels.

## Output
If a valid phase assignment exists, print `YES` on the first line. On the second line, print $m$ integers from the set `{1, 2, 3}`, representing the phase assigned to each channel in the order they were given in the input. If multiple valid assignments exist, any of them will be accepted.
If no such assignment is possible, print `NO`.

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
