# Problem A — Hopper Allocation

Time limit: 2 s
Memory limit: 256 MB

An automated dispensing system processes $n$ distinct pharmaceutical ingredients. The system distributes these ingredients among three isolated holding hoppers, which are mechanically designated as hopper 1, hopper 2, and hopper 3.

Due to cross-contamination risks, specific pairs of ingredients will degrade if they are loaded into the same holding hopper. You must assign every ingredient to exactly one of the three hoppers such that no two ingredients that pose a mutual cross-contamination risk share a hopper.

To standardize loading procedures across multiple facilities, the system enforces a strict priority rule for valid assignments. The configuration must be chosen such that the sequence of hopper numbers assigned to ingredients $1$ through $n$ is lexicographically minimized. This means the system prioritizes placing ingredient 1 into the lowest-numbered hopper possible, then ingredient 2 into the lowest-numbered hopper possible, and so forth, while still ensuring a completely safe arrangement for all ingredients.

If no safe configuration exists for the given ingredients and contamination risks, the system must reject the batch.

## Input
The first line contains two integers $n$ and $m$ — the number of ingredients and the number of cross-contamination risks ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of ingredients that pose a cross-contamination risk.

## Output
If no safe hopper assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $h_1, h_2, \dots, h_n$ (each in $\{1, 2, 3\}$), where $h_i$ is the hopper assigned to ingredient $i$. This sequence must be the lexicographically smallest valid configuration.

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
