# Problem C — Too Many Corridors

Time limit: 2 s   Memory limit: 256 MB

## Description

A building has **n** junctions (numbered 1..n) connected by **m** corridors, and a budget of **k** guards. A guard at a junction watches every corridor touching it.

Two corridors are **independent** if they share no junction. If you can find a set of independent corridors, each of them needs its own separate guard (no single guard can watch two of them), so their count is a lower bound on the number of guards required.

In the input you are given, the layout contains at least **k+1** pairwise independent corridors, which proves that **k** guards can never watch everything.

Output any **k+1** pairwise independent corridors.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 1 ≤ m ≤ 200000, 0 ≤ k ≤ 100000).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): a corridor. No corridor is listed twice. It is guaranteed that at least **k+1** pairwise independent corridors exist.

## Output

Print **k+1** lines, each containing two integers `u v` describing a chosen corridor, such that all printed corridors are actual corridors and no two of them share a junction.

## Examples

### Example 1

**Input**
```
6 4 2
1 2
3 4
5 6
1 3
```

**Output**
```
1 2
3 4
5 6
```

### Example 2

**Input**
```
4 3 1
1 2
3 4
2 3
```

**Output**
```
1 2
3 4
```

## Note

In Example 1, the three corridors (1,2), (3,4), (5,6) share no junctions, so three separate guards would be required — more than the budget of 2.
