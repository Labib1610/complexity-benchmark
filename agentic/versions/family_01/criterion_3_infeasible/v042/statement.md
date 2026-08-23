# Problem C — Broadcast Channel Certification

Time limit: 2 s   Memory limit: 256 MB

A media company is trying to schedule $n$ live broadcast events across two available satellite channels. However, the scheduling team claims that the current timetable is impossible to accommodate with only two channels. To formally certify this impossibility to management, they must provide a concrete counterexample.

An impossibility is proven if there are three events that all mutually overlap in time with one another. Since every pair within this triplet overlaps, no two of these three events can share a channel, meaning they would require at least three separate channels. You are given the list of all pairs of events that overlap. It is guaranteed that at least one such triplet of mutually overlapping events exists in the schedule. Your task is to identify one such triplet to serve as the certificate of impossibility.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2\cdot 10^5)$), representing the number of broadcast events and the number of overlapping event pairs, respectively.
Each of the following $m$ lines provides two integers $u$ and $v$ — indicating that event $u$ and event $v$ overlap.
It is guaranteed that there is at least one set of three events that mutually overlap.

## Output
Output three integers $a$, $b$, and $c$ on a single line, with $a < b < c$, such that the pairs $a$–$b$, $a$–$c$, and $b$–$c$ are all listed as overlapping in the input. Output the lexicographically smallest such triplet (minimize $a$; in case of a tie, minimize $b$; if still tied, minimize $c$).

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
