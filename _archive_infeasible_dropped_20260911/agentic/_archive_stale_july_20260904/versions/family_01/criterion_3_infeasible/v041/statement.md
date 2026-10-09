# Problem C — Proof of Impossibility

Time limit: 2 s
Memory limit: 256 MB

The shipping department has exactly two secure containers available for the upcoming transport. However, it has been determined that the current load is impossible to safely pack. Your task is to find the proof of this impossibility. 

You are provided a list of item pairs that interact violently and must never be placed in the same container. It is guaranteed that the manifest contains at least one group of three items where every item in the group interacts violently with both of the other two. Any such group makes it impossible to divide the items into just two containers. You must output one such group of three items.

## Input
The first line contains two integers n and m (3 ≤ n ≤ 2000, 3 ≤ m ≤ min(n·(n−1)/2, 2·10⁵)), representing the total number of items and the number of violent interactions. Items are numbered from 1 to n.
Each of the next m lines contains two integers x y — a pair of items that interact violently.
It is guaranteed that at least one such group of three items exists.

## Output
Print three integers a b c on one line with a < b < c such that all three pairs a–b, a–c, and b–c interact violently. Output the lexicographically smallest such group (smallest a; ties by smallest b; then smallest c).

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
