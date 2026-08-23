# Signal Amplifiers

Time limit: 1 s
Memory limit: 256 MB

A communication grid consists of $n$ signal amplifiers, indexed from 1 to $n$. Within this grid, there are $m$ critical data links, each operating between a specific pair of amplifiers.

You must assign a power tier to every amplifier in the grid. The available power tiers are strictly 1 and 2. The stability of the grid relies entirely on avoiding interference along the data links. When two amplifiers are joined by a link, their combined signal is processed by taking the bitwise AND of their assigned power tiers.

A link is perfectly stable if and only if this bitwise AND evaluates to exactly 0. Any non-zero result indicates harmful signal interference, causing the link to drop.

Determine if it is possible to assign a power tier to each of the $n$ amplifiers so that all $m$ data links are stable at the same time. If a valid configuration exists, you must provide the lexicographically smallest assignment sequence. A sequence of power tiers $s_1, \dots, s_n$ is lexicographically smaller than another valid sequence $t_1, \dots, t_n$ if $s_i < t_i$ at the first index $i$ where the two sequences differ.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), which denote the total number of amplifiers and the number of data links, respectively.
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), specifying a data link connecting amplifier $u$ and amplifier $v$.

## Output
If no valid assignment of power tiers (1 and 2) can make all $m$ links evaluate to a bitwise AND of 0, output a single line with the word `NO`.
If a stable configuration is possible, print `YES` on the first line. On the second line, output $n$ integers $p_1 \dots p_n$ (where each $p_i \in \{1, 2\}$), representing the lexicographically smallest valid sequence of power tiers.

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