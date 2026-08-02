# Signal Channel Allocation

Time limit: 1 s   Memory limit: 256 MB

An environmental monitoring network comprises $N$ observation posts, labeled $1$ through $N$. Each post must be configured to transmit on one of two available frequency bands, designated as channel 1 or channel 2.

Due to regional radio interference, certain pairs of posts suffer from mutual cross-talk. To maintain clear communications, any two posts that share a cross-talk link must operate on different frequency channels (one on channel 1 and the other on channel 2).

Your task is to determine whether a valid assignment of channels exists for all posts. If multiple valid channel assignments are possible, choose the sequence $s_1, s_2, \dots, s_N$ that is lexicographically smallest. If no valid assignment exists, report that it cannot be done.

## Input
The first line contains two integers $N$ and $M$. The network infrastructure supports up to two hundred thousand posts ($1 \le N \le 200\,000$), and the system tracks up to two hundred thousand cross-talk links ($0 \le M \le 200\,000$).

Each of the next $M$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le N, u \neq v$), representing a cross-talk link between post $u$ and post $v$.

## Output
If no valid channel assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $N$ space-separated integers $s_1, s_2, \dots, s_N$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid channel assignment sequence for posts $1$ through $N$.

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
