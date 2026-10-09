# Problem A — Corporate Consolidation

Time limit: 5 s   Memory limit: 256 MB

## Description

The economy consists of **n** independent startup companies, numbered 1 to n. Initially, each startup is owned by its own separate corporation (meaning there are $n$ distinct corporations, each owning exactly one startup).

A specific group of **t** startups are designated as **key assets**. Your objective is to execute a sequence of corporate mergers so that all **t** key assets end up owned by the *same* single corporation. 

You have a list of **m** available merger deals. Each deal is described by a primary startup **u**, a secondary startup **v**, and a consulting fee **w**. If you choose to execute this deal, you pay the fee **w**, and the corporation that currently owns **u** merges with the corporation that currently owns **v** into a single combined corporation. (If **u** and **v** are already owned by the same corporation, the corporate structure remains unchanged, though the fee is still paid if you execute the deal). 

You may execute any combination of the available deals, paying the sum of their fees. You are welcome to involve startups that are not key assets if merging them helps consolidate the key assets at a lower total cost.

Find the minimum total consulting fee required to ensure that all **t** key assets are owned by the same corporation.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line lists **t** distinct integers representing the ids of the key assets.
The following **m** lines each contain three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000). These represent a merger deal involving the corporation owning **u** and the corporation owning **v**, which can be executed for a fee of **w**.
It is guaranteed that it is possible to consolidate all key assets using the available deals.

## Output

Output a single integer representing the minimum total consulting fee to achieve the consolidation goal.

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

In Example 1, executing the three deals involving startup 4 (total fee 1+1+1 = 3) merges the corporations owning 1, 2, 3, and 4 into a single entity. This is cheaper than executing deals to merge the key assets directly (which would cost 2+2=4). 
In Example 3, there is only one key asset. It is already owned by its own corporation, so no deals need to be executed.