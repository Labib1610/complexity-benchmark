# Problem A — Gallery Illumination

Time limit: 2 s   Memory limit: 256 MB

## Description

You are finalizing the lighting design for an art gallery containing $n$ distinct display zones. For each zone, you must choose exactly one of two color temperatures for its spotlights: warm (represented as 1) or cool (represented as 0). No zone can be left unlit, and no other temperatures are available.

The gallery's curator has established a list of $m$ visual anchors to guide visitors through the space. Each visual anchor is defined by a set of three preferred lighting states across the gallery. An anchor is considered successful as long as it gets some of what it prefers—it only fails if all three of its specified lighting states are absent from your final design. 

A preferred lighting state is denoted by a non-zero integer $c$. If $c > 0$, the state requests that zone $c$ uses warm lighting (1). If $c < 0$, the state requests that zone $|c|$ uses cool lighting (0).

Your task is to determine whether it is possible to select a color temperature for every single one of the $n$ zones such that every single visual anchor is successful. If such a design exists, you must provide one.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$), representing the number of display zones and the number of visual anchors, respectively.
Each of the next $m$ lines contains three non-zero integers $l_1, l_2, l_3$, where $|l_i| \le n$. These represent the three preferred lighting states for that visual anchor. 

## Output
If no lighting design exists that makes all anchors successful simultaneously, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{0, 1\}$). The value $s_i$ represents the chosen color temperature for zone $i$. Any valid design will be accepted.

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
Each visual anchor specifies exactly three preferred states. The same zone may be referenced more than once within a single anchor's preferences.
