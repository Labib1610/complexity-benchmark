# Problem A — Optical Network Maintenance Schedule

Time limit: 5 s
Memory limit: 256 MB

## Description
A telecommunications provider is scheduling maintenance for its regional optical network. The network consists of optical switches connected by bidirectional data links. The hardware is standardized such that every switch terminates exactly three data links.

Maintenance is executed in distinct time shifts. When a link undergoes maintenance, it is disabled for the duration of that shift. To prevent localized outages, safety protocols dictate that a switch cannot have two or more of its links disabled in the same shift. Because every switch relies on exactly three links, each of its links must be assigned to a different shift. 

The entire maintenance operation must be completed within exactly three shifts. Determine whether a valid shift assignment exists for all links in the network, and if so, provide the schedule.

## Input
The first line contains two integers **n** and **m** (n is even, m = 3n/2, 2 ≤ n ≤ 2000), representing the number of optical switches and data links, respectively.
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u < v ≤ n), representing a data link connecting switch **u** and switch **v**.

## Output
If a valid schedule exists, print `YES` on the first line. On the second line, print **m** integers from the set {1, 2, 3} representing the shift assigned to each link, in the same order the links were provided in the input. If no such schedule exists, print `NO`.

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
