# Unanimous Committee

Time limit: 5 s   Memory limit: 256 MB

## Description

You are analyzing a legislative body consisting of **n** politicians, numbered 1 to **n**. An upcoming resolution requires each politician to cast a vote of either *Yea* or *Nay*. Initially, each politician is free to vote independently.

To influence the outcome, you can arrange binding pacts between certain pairs of politicians. There are **m** available pacts you can broker. The $i$-th available pact, if arranged, enforces a strict rule: politician **u** and politician **v** must cast the exact same vote. Arranging this pact requires a lobbying expenditure of **w**.

When multiple pacts are arranged, the only permissible voting outcomes for the entire legislative body are those that satisfy all the arranged pacts simultaneously.

You are given a specific committee of **t** key politicians. Your goal is to arrange a subset of the available pacts such that, in every permissible voting outcome for the legislative body, the **t** key politicians are guaranteed to vote identically (i.e., they all vote *Yea* or they all vote *Nay*). 

Determine the minimum total lobbying expenditure required to arrange a subset of pacts that achieves this guarantee.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the identification numbers of the key politicians.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): an available pact between politician **u** and politician **v**, and its lobbying expenditure **w**.
The provided set of available pacts is sufficient to guarantee the committee votes identically.

## Output

Print a single integer: the minimum total lobbying expenditure required to guarantee that the key politicians cast the exact same vote.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note

In Example 1, arranging the pacts involving politician 4 (between 1 and 4, 2 and 4, and 3 and 4 at an expenditure of 1 + 1 + 1 = 3) restricts the valid voting outcomes such that politicians 1, 2, 3, and 4 must all cast the same vote. Consequently, any valid voting outcome will have the key politicians (1, 2, and 3) voting identically. This incurs a lower expenditure than arranging pacts directly among the key politicians.

In Example 3, there is only one key politician. If there is only one key index, a single politician always agrees with themselves, so no pacts need to be arranged. The minimum expenditure is therefore 0.