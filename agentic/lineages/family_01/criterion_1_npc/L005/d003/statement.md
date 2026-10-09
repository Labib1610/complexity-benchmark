# Problem A — Museum Curation

Time limit: 2 s   Memory limit: 256 MB

You are organizing a highly anticipated exhibition featuring $n$ interactive installations. The venue is divided into exactly three acoustic pavilions, designated as Pavilion 1, Pavilion 2, and Pavilion 3.

Every installation must be placed in exactly one of these pavilions. However, the interactive audio elements of certain installations operate on overlapping frequencies. You have compiled a list of $m$ pairs of installations that will cause acoustic interference if they are placed in the same pavilion. 

You must determine whether it is possible to distribute all the installations across the three pavilions such that no acoustic interference occurs. 

## Input
The first line contains two integers $n$ and $m$ — the number of installations and the number of interfering pairs ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the subsequent $m$ lines contains two integers $u$ and $v$, representing a pair of installations that cannot share the same pavilion. Installations are indexed from 1 to $n$.

## Output
If no such distribution is possible, output NO on a single line.
Otherwise, output YES on the first line. On the second line, output $n$ integers $c_1 \ c_2 \dots c_n$ (each being 1, 2, or 3), where $c_i$ is the pavilion assigned to installation $i$. If multiple valid distributions exist, you may output any of them.

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