# Problem A — Synthetic Genome Viability

Time limit: 2 s   Memory limit: 256 MB

## Description
A bioengineering lab is designing a synthetic organism with a custom sequence of $n$ genes. During the synthesis process, every single gene must be permanently set to one of two states: activated or suppressed.

The organism's survival depends on $m$ critical cellular pathways. Each pathway relies on exactly three specific regulatory requirements. A requirement specifies that a particular gene must be in a certain state (for instance, "Gene 4 must be activated" or "Gene 7 must be suppressed"). For a pathway to function normally, at least one of its three regulatory requirements must be met by the organism's actual gene states. If none of the three requirements are met, the pathway fails, leading to non-viability. Because these pathways govern overlapping biological functions, the same gene may be involved in multiple pathways, and different pathways might require the same gene to be in opposite states.

Your task is to determine if there is a complete genetic sequence—assigning an activated or suppressed state to all $n$ genes—that allows all $m$ cellular pathways to function simultaneously. If such a sequence is possible, you must output it. Otherwise, you must declare that the organism cannot be viable.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$), representing the number of genes and the number of cellular pathways, respectively.
Each of the following $m$ lines describes a pathway and contains exactly three non-zero signed integers $l_1, l_2, l_3$ ($|l_i| \le n$). 
A positive integer $i$ represents a requirement that gene $i$ is activated. A negative integer $-i$ represents a requirement that gene $i$ is suppressed.

## Output
If no genetic sequence can keep all pathways functioning, print `NO` on a single line.
If a viable sequence exists, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{0, 1\}$). Here, $s_i = 1$ means gene $i$ is activated, and $s_i = 0$ means gene $i$ is suppressed. If multiple viable sequences exist, any of them will be accepted.

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

## Note
Each pathway is always governed by exactly three regulatory requirements. A single pathway might depend on the same gene more than once.
