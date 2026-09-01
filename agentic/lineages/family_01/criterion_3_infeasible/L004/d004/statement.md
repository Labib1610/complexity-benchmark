# Critical Interference

Time limit: 2 s
Memory limit: 256 MB

A proposed communications standard attempts to allocate $n$ transceivers (labeled 1 through $n$) into exactly two distinct frequency bands. However, testing has revealed $m$ specific bidirectional interference links between pairs of transceivers. If two linked transceivers operate on the same frequency band, the signal degrades entirely.

The standard's allocation constraints are fundamentally impossible to satisfy. Your objective is to isolate the root cause of this failure. Specifically, you must locate a subset of exactly three transceivers which, in isolation, cannot be validly assigned to the two frequency bands. That is, no matter how you assign each of these three specific transceivers to one of the two bands, at least one band will always end up containing a pair of transceivers that share an interference link.

The existence of such a subset proves that two frequency bands are not enough. It is guaranteed that at least one such subset is present in the network.

## Input
The first line contains the transceiver count $n$ and the interference link count $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
The following $m$ lines each detail a pair of transceivers $u$ and $v$ that mutually interfere.
At least one subset of three transceivers satisfying the impossibility condition is guaranteed to exist.

## Output
Provide the labels of the three transceivers forming the subset, printed on a single line in ascending numerical order.
In the event that several such subsets exist, you must resolve the ambiguity by selecting the subset that includes the transceiver with the absolute lowest label. Should multiple subsets share this lowest-labeled transceiver, further narrow your selection to those whose second-lowest label is as small as possible. If ambiguity still persists, choose the subset whose highest label is minimal.

## Example 1
### Input
```
4 5
1 2
1 3
2 3
2 4
3 4
```
### Output
```
1 2 3
```

## Example 2
### Input
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
### Output
```
1 2 4
```