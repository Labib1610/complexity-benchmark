# Problem A — Deep-Space Array

Time limit: 2 s   Memory limit: 256 MB

A deep-space array is composed of $n$ communication relays, indexed from 1 to $n$. The array's physical layout causes electromagnetic interference between specific pairs of relays. You are given a comprehensive list of $m$ such interfering pairs.

Every relay in the array is capable of operating on exactly one of three distinct frequency bands, denoted by the integers 1, 2, and 3. Safety protocols dictate that if any two relays from the interference list are tuned to the exact same frequency band, the resulting feedback will damage the array.

Your objective is to determine if a safe configuration exists for the entire array. If a safe configuration is possible, you must assign a frequency band to each relay. Because the initialization protocol resolves assignments sequentially, whenever multiple safe configurations exist, you must provide the one that yields the lexicographically smallest sequence of bands. That is, minimize the band for relay 1; in the event of a tie, minimize the band for relay 2, and so on.

## Input
The first line contains two integers $n$ and $m$ — the number of relays and the number of interfering pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the following $m$ lines contains two integers $u$ and $v$ — a pair of relays that will interfere with each other.

## Output
If there is no way to configure the relays safely, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $b_1, b_2, \dots, b_n$ (where each $b_i \in \{1, 2, 3\}$), representing the frequency band assigned to relay $i$. If there are multiple safe configurations, output the sequence that is lexicographically smallest.

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
