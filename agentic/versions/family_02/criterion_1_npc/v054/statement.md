# Problem A — Exhibition Lighting

Time limit: 2 s   Memory limit: 256 MB

## Description

You are configuring the lighting for an art exhibition. The exhibition floor contains $n$ display zones. The lighting control board features exactly 6 banks of 15 switches each, establishing the maximum number of zones the facility can support. The facility always has at least one active zone. For each zone, you must select one of two lighting modes: warm (represented by 1) or cool (represented by 0). Every zone must be assigned exactly one mode.

The exhibition's artistic director has provided a set of $m$ viewing perspectives. The director's planning software stores these perspectives in up to 16 memory pages, each holding exactly 25 entries, establishing the maximum possible number of perspectives. It is also possible for the director to provide an empty list of perspectives. Each perspective lists exactly three ideal lighting conditions for specific zones. A perspective is considered visually complete if at least one of its three ideal conditions is realized in your configuration. It fails only if your configuration contradicts all three of its conditions.

An ideal condition is given as a non-zero integer $c$. Its absolute value $|c|$ identifies the zone number. If $c > 0$, the condition requires zone $c$ to be warm (1). If $c < 0$, the condition requires zone $|c|$ to be cool (0). Note that a perspective might reference the same zone multiple times.

Your goal is to find a single lighting configuration for all $n$ zones that makes every single viewing perspective visually complete.

## Input
The first line contains two integers $n$ and $m$, representing the number of display zones and the number of viewing perspectives, respectively. The exact bounds for $n$ and $m$ must be derived from the physical and software limits described above.
Each of the following $m$ lines contains three non-zero integers $l_1, l_2, l_3$, representing the three ideal conditions for that perspective. The absolute value of any condition will never exceed $n$.

## Output
If it is impossible to satisfy every viewing perspective simultaneously, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{0, 1\}$). The value $s_i$ indicates the chosen lighting mode for zone $i$. Any valid configuration will be accepted.

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
