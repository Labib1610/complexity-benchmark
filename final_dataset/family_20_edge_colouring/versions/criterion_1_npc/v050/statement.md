# Problem A — Pipeline Pressure Testing Phases

Time limit: 5 s   Memory limit: 256 MB

## Description
A municipal utility oversees a highly standardized pipeline infrastructure. The system is built with strict uniformity: every intersection serves as the endpoint for precisely three pipeline segments. Due to this architectural rule, a system comprising $n$ intersections will always contain exactly $3n/2$ segments, and $n$ is inherently an even number.

To ensure structural integrity, every segment must undergo a pressure test during one of three distinct testing phases. However, a strict isolation requirement applies at the intersections: if two segments meet at the same intersection, they cannot be tested in the same phase, as the simultaneous stress would compromise the intersection's seals.

Because there are exactly three testing phases and every intersection connects to exactly three segments, this isolation requirement dictates that at any given intersection, the three connected segments must all be tested in completely different phases. 

Despite this rigid local requirement, the overall layout of the infrastructure might prevent a valid testing schedule from being established. Your task is to allocate each pipeline segment to one of the three testing phases such that no two segments sharing an intersection are assigned the same phase, or to determine that the infrastructure's layout renders this impossible.

## Input
The first line contains two integers $n$ and $m$ ($n$ is even, $m = 3n/2$, $2 \le n \le 2000$), representing the number of intersections and the number of pipeline segments.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u < v \le n$), representing a segment between intersection $u$ and intersection $v$. The input is guaranteed to describe an infrastructure where every intersection connects to exactly three segments.

## Output
If a valid testing schedule exists, print `YES` on the first line. On the second line, print $m$ integers from $\{1, 2, 3\}$, representing the phase assigned to each segment in the order they appear in the input. If multiple valid assignments exist, you may output any of them.
If no such schedule is possible, print `NO`.

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
