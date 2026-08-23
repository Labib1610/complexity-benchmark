# Bio-reactor Calibration

Time limit: 1 s
Memory limit: 256 MB

You are calibrating a bio-reactor that contains $n$ distinct microbial cultures. Each culture must be fed a nutrient solution at either flow rate 1 or flow rate 2.

The bio-reactor monitors $m$ symbiotic links. Each link connects a specific pair of cultures. For a symbiotic link to thrive, the combined nutrient flow rate supplied to the two connected cultures must be exactly 3 units. If the total flow rate for any link is 2 units or 4 units, the symbiosis collapses.

Your task is to determine a valid flow rate (1 or 2) for all $n$ cultures that maintains all symbiotic links. If multiple valid configurations exist, the system defaults to the lexicographically smallest sequence of flow rates (meaning the sequence $f_1, f_2, \dots, f_n$ must be as small as possible when compared element by element from culture 1 to culture $n$).

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of cultures and the number of symbiotic links.
Each of the following $m$ lines contains two integers $u$ and $v$, indicating a symbiotic link between culture $u$ and culture $v$.

## Output
If no valid flow rate assignment can sustain the bio-reactor, output a single line containing `NO`.
If a valid configuration exists, output `YES` on the first line. On the second line, output $n$ integers $f_1, f_2, \dots, f_n$ (each being 1 or 2), representing the lexicographically smallest valid assignment.

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